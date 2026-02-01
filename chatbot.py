import json
import re

with open("data/university_data.json", encoding="utf-8") as f:
    DATA = json.load(f)

last_school = None
last_program = None


# ---------------- CONFIG ----------------

SCHOOL_DEFAULT_PROGRAM = {
    "architecture": "barch",
    "engineering": "btech",
    "management": "mba",
    "law": "ba_llb",
    "pharmacy": "bpharm",
    "science": "bsc",
    "humanities": "ba"
}

ALIASES = {
    "architecture": ["architecture", "arch"],
    "engineering": ["engineering", "engineer"],
    "management": ["management", "mba", "business"],
    "law": ["law", "legal"],
    "pharmacy": ["pharmacy", "pharma"],
    "science": ["science", "sciences"],
    "humanities": ["humanities", "arts"],

    "barch": ["barch"],
    "march": ["march", "m.arch"],
    "btech": ["btech", "b.tech"],
    "mtech": ["mtech", "m.tech"],
    "mba": ["mba"],
    "bba": ["bba"],
    "ba_llb": ["ba llb"],
    "llm": ["llm"],
    "bpharm": ["bpharm"],
    "mpharm": ["mpharm"],
    "bsc": ["bsc"],
    "msc": ["msc"],
    "ba": ["ba"],
    "ma": ["ma"]
}

INTENT_KEYWORDS = {
    "fees": ["fees", "fee", "cost", "per year", "total"],
    "eligibility": ["eligibility", "eligible", "requirement"],
    "duration": ["duration", "years", "how long"],
    "career_scope": ["career", "career scope", "jobs", "placements"],
    "specializations": ["specialization", "specializations", "branches"],
    "entrance_exams": ["entrance", "exam", "nata", "jee"]
}


# ---------------- HELPERS ----------------

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def detect_intent(text):
    for key, words in INTENT_KEYWORDS.items():
        if any(w in text for w in words):
            return key
    return None


def match_alias(tokens):
    for key, aliases in ALIASES.items():
        if any(t in aliases for t in tokens):
            return key
    return None


def find_program_and_school(tokens):
    for school, sdata in DATA.items():
        for pkey in sdata["programs"]:
            if pkey in tokens:
                return school, pkey
    return None, None


# ---------------- CORE LOGIC ----------------

def get_response(user_input):
    global last_school, last_program
    text = user_input.lower()
    tokens = tokenize(text)
    intent = detect_intent(text)

    # Greeting
    if any(t in ["hi", "hello", "hey"] for t in tokens):
        return (
            "Hi, I’m your University Admissions Assistant.\n"
            "You can ask naturally like:\n"
            "- btech fees\n"
            "- career scope of architecture\n"
            "- eligibility mba\n"
            "- engineering programs"
        )

    # Detect explicit program
    school, program = find_program_and_school(tokens)

    # Detect aliases
    alias = match_alias(tokens)
    if alias in DATA:
        school = alias
        program = SCHOOL_DEFAULT_PROGRAM.get(school)

    elif alias:
        for s, sdata in DATA.items():
            if alias in sdata["programs"]:
                school = s
                program = alias

    # Use memory
    school = school or last_school
    program = program or last_program

    if school:
        last_school = school
    if program:
        last_program = program

    # If only school asked
    if school and not program:
        programs = DATA[school]["programs"].values()
        return (
            f"{school.title()} offers the following programs:\n- "
            + "\n- ".join(p["name"] for p in programs)
        )

    if not school or not program:
        return (
            "I couldn’t understand that.\n"
            "Try asking like:\n"
            "- btech fees\n"
            "- architecture programs\n"
            "- career scope of mba"
        )

    prog = DATA[school]["programs"][program]

    # If intent exists & field exists in JSON
    if intent and intent in prog:
        value = prog[intent]
        if isinstance(value, list):
            return f"{intent.replace('_',' ').title()}:\n- " + "\n- ".join(value)
        return f"{intent.replace('_',' ').title()}: {value}"

    # Special handling
    if intent == "specializations" and "specializations" in prog:
        return "Specializations:\n- " + "\n- ".join(prog["specializations"])

    # Default full overview
    response = [f"{prog['name']}"]
    for key, value in prog.items():
        if key == "name":
            continue
        if isinstance(value, list):
            response.append(f"{key.replace('_',' ').title()}:\n- " + "\n- ".join(value))
        else:
            response.append(f"{key.replace('_',' ').title()}: {value}")

    return "\n".join(response)
