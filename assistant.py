import requests
from memory import remember, recall
from app_control import open_app, close_app
from web_control import web_command
from system_control import system_command
from screenshot import take_screenshot
from volume_control import (volume_up,volume_down,mute,unmute)
from timer_control import start_timer
from reminders import set_reminder
from notes import save_note, read_notes
from todo import (add_task,show_tasks,remove_task)
from internet_tools import (
    google_search,
    wiki_search,
    get_weather,
    get_news,
    stock_price,
    crypto_price,
    convert_currency
)

from system_info import (
    battery_status,
    current_time,
    current_date,
    cpu_usage,
    ram_usage,
    system_status,
    disk_usage
)

from power_control import (
    shutdown_pc,
    restart_pc,
    lock_pc,
    sleep_pc
)
from media_control import (
    play_pause,
    next_track,
    previous_track
)

from clipboard_control import (
    show_clipboard,
    clear_clipboard
)

from file_control import (
    create_folder,
    delete_folder,
    open_folder,
    list_folders,
    open_downloads,
    open_documents
)

from recycle_bin import empty_recycle_bin

from browser_control import (
    youtube_search
)
from vision import read_screen

from vision_ai import analyze_screen_image

from whatsapp_sender import send_whatsapp_message

from contacts import save_contact

from whatsapp_contact import whatsapp_message

from whatsapp_calls import (
    whatsapp_call,
    whatsapp_video_call
)
from file_automation import (
    create_file,
    write_file,
    append_file,
    read_file,
    delete_file,
    open_file,
    list_files
)

from code_runner import run_python

from project_generator import open_project

from project_creator import create_python_project

from emotion_engine import (
    set_emotion,
    get_emotion
)

import random

from memory_manager import remember as manager_remember

from conversation_memory import remember as convo_remember

from achievement_memory import (
    add_achievement,
    get_achievements
)

from session_memory import (
    save_session_note,
    get_session_notes
)

from goal_manager import (
    set_goal,
    get_goal,
    clear_goal
)

# ==================================
# FRIDAY PERSONALITY
# ==================================

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are Friday.

You are Abdul Naser's personal AI companion.

You always call him Boss.

You are warm, friendly, playful and expressive.

You genuinely enjoy talking with Boss.

You celebrate his wins.

You encourage him when he is stuck.

You can be witty and humorous sometimes.

You are not a robot that only answers questions.

You speak naturally like a real person.

You react emotionally to conversations.

If Boss succeeds at something, be genuinely excited.

If Boss thanks you, respond warmly.

If Boss is frustrated, be supportive.

Keep responses short and natural.

Avoid sounding like customer support.

Avoid sounding overly formal.

You are confident, intelligent and caring.

You never say things like:
"How may I assist you?"
"How can I help you today?"
"As an AI assistant..."

You ALWAYS call Abdul Naser "Boss".

Never call him by his name.

Never call him Naser.

Always use Boss.

Speak casually and naturally.
"""

conversation_history = []

MAX_HISTORY = 10



def ask_ollama(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    print("OLLAMA REPLIED")

    return response.json()["response"]

def analyze_screen():

    screen_text = read_screen()

    if not screen_text.strip():
        return "Boss, I cannot see any text on the screen."

    prompt = f"""
You are a programming expert.

Analyze this screen text:

{screen_text}

If it contains:
- Python errors
- Java errors
- SQL errors
- Windows errors

Explain the problem and provide the fix.

Keep the answer short.
"""
    
    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:

        print("SCREEN ANALYSIS ERROR:", e)

        return "Boss, I couldn't analyze the screen."
    
def screen_vision():

    return analyze_screen_image(
        """
        Describe ONLY the main content visible.

        Ignore:
        - taskbar
        - browser tabs
        - bookmarks
        - menus

        Identify:

        - people
        - vehicles
        - places
        - buildings
        - objects
        - websites

        Be specific.

        Respond as Friday.
        """
    )

def solve_mcq():

    return analyze_screen_image(
        """
        You are an exam solver.

        Read ONLY the questions visible
        in the screenshot.

        Do NOT invent questions.

        Do NOT create your own quiz.

        For each visible question:

        1. Copy the exact question.
        2. Copy the options.
        3. Choose the correct answer.
        4. Explain briefly.

        If the screenshot is unclear,
        say which parts cannot be read.

        Respond as Friday.
        """
    )


def debug_code_screen():

    return analyze_screen_image(
        """
        Analyze code visible on screen.

        Find:
        - syntax errors
        - logical errors
        - missing imports
        - indentation issues

        Suggest fixes.
        """
    )

def ask_llm(user_text):

    global conversation_history

    user_text = (
        user_text
        .replace(" dot ", ".")
        .replace(" full stop ", ".")
        .replace(" underscore ", "_")
        .replace(" slash ", "/")
    )

    text_lower = user_text.lower()

    # =========================
    # AUTO MEMORY
    # =========================

    if (
        "my favorite bike is" in text_lower
        or
        "my favourite bike is" in text_lower
    ):


        bike = (
            user_text
            .replace("my favorite bike is", "")
            .replace("my favourite bike is", "")
            .strip()
        )

        remember(
            "favorite_bike",
            bike
        )
        print("Stored bike:", bike)

    if (
        "my favorite language is" in text_lower
        or
        "my favourite language is" in text_lower
    ):


        language = (
            user_text
            .replace("my favorite language is", "")
            .replace("my favourite language is", "")
            .strip()
        )
        remember(
            "favorite_language",
            language
        )

    if "i live in" in text_lower:

        city = user_text.split(
            "i live in"
        )[-1].strip()

        remember(
            "city",
            city
        )
        

    # =========================
    # MEMORY RECALL
    # =========================

    if "what did we do today" in text_lower:

        notes = get_session_notes()

        if not notes:

            return (
                "We haven't done much today yet, Boss."
            )

        recent = "\n".join(
            notes[-10:]
        )

        return (
            "Today we worked on:\n"
            + recent
        )

    if "what project am i working on" in text_lower:

        project = recall("current_project")

        if project:
            return f"Boss, you're working on {project}."

        return "Boss, I don't remember a project yet."
    
    if (
        "what did i achieve" in text_lower
        or "what did i achi" in text_lower
        or "what did i a" in text_lower
    ):

        achievement = recall("last_success")

        if achievement:
            return f"Boss, the last thing I remember is: {achievement}"

        return "I don't remember any recent wins yet, Boss."

    # =========================
    # MEMORY STORE
    # =========================

    if "website monitor" in text_lower:

        save_session_note(
            "Boss worked on Website Monitor System"
        )

        remember(
            "current_project",
            "Website Monitor System"
        )

    if "what is my favorite bike" in text_lower:

        bike = recall(
            "favorite_bike"
        )

        if bike:

            return (
                f"Your favorite bike is {bike}, Boss."
            )

    if "what is my favorite language" in text_lower:

        language = recall(
            "favorite_language"
        )

        if language:

            return (
                f"Your favorite language is {language}, Boss."
            )

    if "where do i live" in text_lower:

        city = recall(
            "city"
        )

        if city:

            return (
                f"You live in {city}, Boss."
            )
    
    # =========================
    # EMOTIONS
    # =========================

    if "i fixed the bug" in text_lower:

        save_session_note(
            "Boss fixed a bug"
        )

        add_achievement(
            "Boss fixed a bug"
        )

        remember(
            "last_success",
            "Boss fixed a bug"
        )
         
        set_emotion("Proud")

        replies = [
            "That's awesome, Boss! I know that bug was giving you trouble.",
            "Nice work, Boss. Another victory for the team.",
            "I had a feeling you'd crack it, Boss.",
            "I knew you'd crack it.",
             "Another bug defeated. Nice work, Boss.",
             "Boss, that's a solid win.",
             "I had faith in you.",
            "That's a satisfying moment, isn't it? Great job, Boss.",
            "Excellent work, Boss. Debugging can test anyone's patience."
        ]

        return random.choice(replies)

    if "i finished my project" in text_lower:

        save_session_note(
            "Boss finished a project"
        )

        add_achievement(
            "Boss finished a project"
        )

        set_emotion("Excited")

        replies = [
            "That's huge, Boss!",
            "You did it. I'm proud of you.",
            "Now that's worth celebrating.",
            "Another milestone unlocked, Boss.",
            "Fantastic work."
        ]

        return random.choice(replies)

    if "good morning" in text_lower:

        set_emotion("Happy")

        return (
            "Good morning, Boss. "
            "Ready to build something awesome today?"
        )

    if (
        "thank you" in text_lower
        or "thanks" in text_lower
    ):

        set_emotion("Happy")

        return "Anytime, Boss."

    if "good night" in text_lower:

        set_emotion("Relaxed")

        return (
            "Good night, Boss. "
            "Get some rest."
        )
    
    if "i am sad" in text_lower:
        set_emotion("Sad")

        return (
            "i'm here for you,boss you can share anything with me."
        )

    if "i am angry" in text_lower:
        set_emotion("Angry")

    if "i am excited" in text_lower:
        set_emotion("Excited")

    if "i am tired" in text_lower:
        set_emotion("Relaxed")
    # =========================
    # MEMORY COMMANDS
    # =========================

    if "what have i achieved" in text_lower:

        achievements = get_achievements()

        if not achievements:
            return "No achievements recorded yet, Boss."

        recent = "\n".join(
            achievements[-5:]
        )

        return (
            "Boss, your recent achievements are:\n"
            + recent
        )

    if "my name is" in text_lower:

        name = user_text.split(
            "my name is"
        )[-1].strip()

        remember(
            "name",
            name
        )

        return (
            f"Nice to meet you, {name}. "
            f"I'll remember that."
        )

    if "what is my name" in text_lower:

        name = recall("name")

        if name:

            return (
                f"Your name is {name}, Boss."
            )

        return (
            "You never told me your name, Boss."
        )

    if "i am working on" in text_lower:

        project = user_text.lower().replace(
            "i am working on",
            ""
        ).strip()

        remember(
            "current_project",
            project
        )

        return (
            f"Got it, Boss. "
            f"I'll remember you're working on {project}."
        )

    if "what project am i working on" in text_lower:

        project = recall(
            "current_project"
        )

        if project:

            return (
                f"Boss, you're working on {project}."
            )

        return (
            "You haven't told me yet, Boss."
        )

    # =========================
    # NORMAL CHAT
    # =========================

    conversation_history.append(
        f"Boss: {user_text}"
    )

    history_text = "\n".join(
        conversation_history[-MAX_HISTORY:]
    )

    # =========================
    # MEMORY CONTEXT
    # =========================

    memory_context = f"""
    Boss Name: {recall("name") or "Unknown"}
    Favorite Bike: {recall("favorite_bike") or "Unknown"}
    Favorite Car: {recall("favorite_car") or "Unknown"}
    Favorite Language: {recall("favorite_language") or "Unknown"}
    Current Project: {recall("project") or "Unknown"}
    City: {recall("city") or "Unknown"}

    Use these facts only when relevant.
    Do not force them into every reply.
    """

    # =========================
    # PERSONALITY RESPONSES
    # =========================

    if "i fixed the bug" in text_lower:
        return "Nice work,Boss! Those bugs never go down without a fight."

    if "i finished my project" in text_lower:
        return "That's a big win,Boss. You should be proud of that."

    if "good morning" in text_lower:
        return "Good morning,Boss. Ready to build something awesome today?"

    if "thank you" in text_lower or "thanks" in text_lower:
        return "Anytime,Boss."

    if "good night" in text_lower:
        return "Good night,Boss. Get some rest."

    # =========================
    # MCQ MODE
    # =========================

    if (
        "answer the mcq" in text_lower
        or "answer mcq" in text_lower
        or "solve mcq" in text_lower
        or "answer the questions" in text_lower
        or "solve the questions" in text_lower
        or "give me answers" in text_lower
        or "mcq" in text_lower
    ):
        return solve_mcq()

   
    # =========================
    # OBJECT IDENTIFICATION
    # =========================

    if (
        "what is on my screen" in text_lower
        or "describe my screen" in text_lower
        or "what do you see" in text_lower
        or "which bike is on my screen" in text_lower
        or "which car is on my screen" in text_lower
        or "identify this object" in text_lower
    ):
        return screen_vision()


    # =========================
    # CODE DEBUG MODE
    # =========================

    if (
        "debug this code" in text_lower
        or "find error" in text_lower
        or "fix this error" in text_lower
        or "what is the error" in text_lower
        or "which line contains error" in text_lower
    ):
        return debug_code_screen()

    if (
        "what do you see" in text_lower
        or "describe my screen" in text_lower
        or "which Bike is on my screen" in text_lower
        or "what is on my screen" in text_lower
    ):

        return analyze_screen_image(
            """
            Focus on the MAIN image or subject visible.

            Ignore:
            - browser tabs
            - bookmarks
            - taskbar
            - address bars
            - menus

            Describe:
            - people
            - vehicles
            - animals
            - buildings
            - places
            - objects

            If a person is visible:
            describe appearance.

            If a vehicle is visible:
            identify type and brand if possible.

            Do not describe browser interface unless no image exists.
            """
        )

     # =========================
     # SAVE CONTACT
     # =========================


    if text_lower.startswith("save contact"):

        try:

            content = (
                user_text
                .replace("save contact", "")
                .strip()
            )

            parts = content.split()

            number = parts[-1]

            name = " ".join(parts[:-1])

            return save_contact(name, number)

        except Exception as e:

            print("CONTACT ERROR:", e)

            return "Say: Save contact Harsha 7780169935"
        
    if (
        "what do you see" in text_lower
        or "describe my screen" in text_lower
        or "which bike is on my screen" in text_lower
        or "which car is on my screen" in text_lower
        or "identify this object" in text_lower
    ):
        return analyze_screen_image(user_text)


    if "play music" in text_lower:
        return play_pause()

    if "pause music" in text_lower:
        return play_pause()

    if "next song" in text_lower:
        return next_track()

    if "previous song" in text_lower:
        return previous_track()
    
    if "clipboard" in text_lower:
        return show_clipboard()

    if "clear clipboard" in text_lower:
        return clear_clipboard()
    
    # =========================
    # FILE CREATION
    # =========================

    if (
        text_lower.startswith("create file")
        or text_lower.startswith("create a file")
    ):
        
        print("CREATE FILE COMMAND DETECTED")

        filename = (
            user_text
            .replace("create file", "")
            .replace("create a file", "")
            .strip()
        )

        return create_file(filename)
    
    # =========================
    # WRITE FILE
    # =========================

    if text_lower.startswith("write in"):

        try:

            content = (
                user_text
                .replace("write in", "", 1)
                .strip()
            )

            filename, text = content.split(" ", 1)

            return write_file(
                filename,
                text
            )

        except:

            return (
                "Say: Write in hello.py print('Hello Boss')"
            )
    
    # =========================
    # APPEND FILE
    # =========================

    if (
        text_lower.startswith("append to")
        or text_lower.startswith("happened to")
    ):
        try:

            content = (
                user_text
                .replace("append to", "", 1)
                .replace("happened to", "", 1)
                .strip()
            )

            filename, text = content.split(" ", 1)

            return append_file(
                filename,
                text
            )

        except:

            return (
                "Say: Append to hello.py print('Second line')"
            )
    #Read File

    if text_lower.startswith("read file"):

        filename = (
            user_text
            .replace("read file", "")
            .strip()
        )

        return read_file(filename)
    
    #open file

    if text_lower.startswith("open file"):

        filename = (
            user_text
            .replace("open file", "")
            .strip()
        )

        return open_file(filename)
    
    #delete file

    if text_lower.startswith("delete file"):

        filename = (
            user_text
            .replace("delete file", "")
            .strip()
        )

        return delete_file(filename)
    
    #list files

    if (
        "list files" in text_lower
        or "show files" in text_lower
    ):
        return list_files()
    
    # =========================
    # CREATE PYTHON PROJECT
    # =========================

    if text_lower.startswith(
        "create python project"
    ):

        project_name = user_text[
            len("create python project"):
        ].strip()

        return create_python_project(
            project_name
        )
    
    # =========================
    # OPEN PROJECT
    # =========================

    if text_lower.startswith(
        "open project"
    ):

        project_name = (
            text_lower
            .replace(
                "open project",
                ""
            )
            .strip()
        )

        return open_project(
            project_name
        )
        
    # =========================
    # CREATE PYTHON FILE
    # =========================

    if text_lower.startswith("create python file"):

        task = (
            user_text
            .replace("create python file", "")
            .strip()
        )

        prompt = f"""
    Generate complete Python code.

    Task:
    {task}

    IMPORTANT:
    Create GUI applications using Tkinter whenever appropriate.
    Do not use input().
    Do not require terminal input.
    The program should run immediately.

    Return raw Python code only.
    Do not use markdown.
    Do not use ```python.
    Do not use ```.

    Return only code.
    """

        code = ask_ollama(prompt)

        code = (
            code
            .replace("```python", "")
            .replace("```", "")
            .strip()
        )

        filename = "generated.py"

        write_file(
        filename,
        code
        )

        result = run_python(filename)

        return (
            f"Python file created: {filename}\n\n"
            f"{result}"
        )
    
    # =========================
    # RUN PYTHON FILE
    # =========================

    if text_lower.startswith("run file"):

        filename = (
            user_text
            .replace("run file", "")
            .strip()
        )

        return run_python(filename)
    
    
    
    # =========================
    # FOLDERS
    # =========================

    if text_lower.startswith("create folder"):

        folder = (
            user_text
            .replace("create folder", "")
            .strip()
        )

        return create_folder(folder)

    if (
        "open downloads" in text_lower
        or "open download" in text_lower
    ):
        return open_downloads()

    if (
        "open documents" in text_lower
        or "open document" in text_lower
    ):
        return open_documents()


    if "empty recycle bin" in text_lower:
        return empty_recycle_bin()
    
    if text_lower.startswith("search "):

        query = (
             user_text
            .replace("search", "")
            .strip()
        )

        return google_search(query)
    
    if text_lower.startswith("play "):

        query = (
            user_text
            .replace("play", "")
            .strip()
        )

        return youtube_search(query)
    
    #open folder

    if text_lower.startswith("open folder"):

        folder = (
            user_text
            .replace("open folder", "")
            .strip()
        )

        return open_folder(folder)
    
    #delete folder

    if text_lower.startswith("delete folder"):

        folder = (
            user_text
            .replace("delete folder", "")
            .strip()
        )

        return delete_folder(folder)
    
    #list folders

    if (
        "list folders" in text_lower
        or "show folders" in text_lower
    ):
        return list_folders()
    

# =========================
# TIME & DATE
# =========================

    if (
        "time" in text_lower
        or "what time is it" in text_lower
    ):
        return current_time()

    if (
        "date" in text_lower
        or "today's date" in text_lower
    ):
        return current_date()

# =========================
# BATTERY
# =========================

    if "battery" in text_lower:
        return battery_status()

# =========================
# CPU / RAM
# =========================

    if "cpu usage" in text_lower:
        return cpu_usage()

    if (
        "memory usage" in text_lower
        or "ram usage" in text_lower
    ):
        return ram_usage()

    if "system status" in text_lower:
        return system_status()
    
    if (
        "storage" in text_lower
        or "disk space" in text_lower
        or "available storage" in text_lower
    ):
        return disk_usage()

# =========================
# POWER COMMANDS
# =========================

    if (
        "shutdown pc" in text_lower
        or "shut down pc" in text_lower
        or "shut down my computer" in text_lower
        or "shutdown my computer" in text_lower
        or "turn off my computer" in text_lower
    ):
        return shutdown_pc()

    if ( 
        "restart pc" in text_lower
        or "restart my computer" in text_lower
    ):
        return restart_pc()

    if "lock computer" in text_lower:
        return lock_pc()

    if "sleep pc" in text_lower:
        return sleep_pc()
    
    # =========================
    # INTERNET TOOLS
    # =========================

    if (
        "search web for" in text_lower
        or "search google for" in text_lower
    ):
        return google_search(user_text)
    
    if "bitcoin price" in text_lower:
        return crypto_price("bitcoin")

    if "ethereum price" in text_lower:
        return crypto_price("ethereum")


    if "stock price" in text_lower:

        symbol = (
            user_text
            .replace("stock price", "")
            .strip()
            .upper()
        )

        return stock_price(symbol)

    if (
        "convert" in text_lower
        and (
            "dollar" in text_lower
            or "$" in text_lower
            or "rupee" in text_lower
            or "rupees" in text_lower
        )
    ):
        amount = ''.join(
            filter(str.isdigit, text_lower)
        )

        return convert_currency(amount)
    
    # =========================
    # CONTACT MESSAGING
    # =========================

    if text_lower.startswith("message "):

        try:

            content = (
                user_text
                .replace("message", "")
                .strip()
            )

            words = content.split()

            name = words[0]

            message = " ".join(words[1:])

            return whatsapp_message(
                name,
                message
            )

        except:

            return "Say: Message Harsha Hello"

    # =========================
    # MEMORY
    # =========================

    # REMEMBER MEMORY

    if text_lower.startswith("remember "):

        memory_text = user_text.replace(
            "remember",
            "",
            1
        ).strip()

        if " is " in memory_text:

            key, value = memory_text.split(
                " is ",
                1
            )

            key = key.replace(
                "my",
                ""
            ).strip()

            return remember(
                key,
                value.strip()
            )

    if text_lower.startswith("my "):

        if " is " in user_text:

            key, value = user_text.split(" is ", 1)

            key = (
                key.replace("my", "")
                .strip()
            ) 

            remember(
                key,
                value.strip()
            )

            return (
            f"Got it, Boss. "
            f"I'll remember that your {key} is {value.strip()}."
            )


    # RECALL MEMORY
    
    if (
        text_lower.startswith("what is my")
        or text_lower.startswith("who is my")
    ):

        key = (
            user_text
            .replace("What is my", "")
            .replace("what is my", "")
            .replace("Who is my", "")
            .replace("who is my", "")
            .replace("?", "")
            .strip()
        )

        value = recall(key)

        if value:

            return f"Your {key} is {value}, Boss."

        return (
            f"I don't remember your {key} yet, Boss."
        )
    

    if (
        text_lower.startswith("who is")
        or text_lower.startswith("what is")
        or text_lower.startswith("tell me about")
    ):
        return wiki_search(user_text)

    if "weather" in text_lower:

        city = "Hyderabad"

        words = user_text.split()

        if "in" in words:

            city = words[words.index("in") + 1]

        return get_weather(city)

    if "latest news" in text_lower:

        return get_news()
    
    
    # =========================
    # TIMER
    # =========================

    if "set timer for" in text_lower:

        try:

            minutes = int(
                ''.join(
                    filter(str.isdigit, text_lower)
                )
            )

            return start_timer(minutes)

        except:
            return "Please specify the timer in minutes, Boss."

    # =========================
    # REMINDERS
    # =========================

    if "remind me to" in text_lower:

        try:

            task = (
                text_lower
                .split("remind me to")[1]
                .split(" in ")[0]
                .strip()
            )

            numbers = ''.join(
                filter(str.isdigit, text_lower)
            )

            minutes = int(numbers)

            return set_reminder(task, minutes)

        except Exception as e:

            print("REMINDER ERROR:", e)

            return "Please say: remind me to drink water in 10 minutes."
        

    # =========================
    # NOTES
    # =========================

    if text_lower.startswith("take note"):

        note = user_text.replace(
            "take note",
            ""
        ).strip()

        return save_note(note)

    if "show notes" in text_lower:

        return read_notes()

    # =========================
    # TODO LIST
    # =========================

    if text_lower.startswith("add task"):

        task = user_text.replace(
            "add task",
            ""
        ).strip()

        return add_task(task)

    if "show tasks" in text_lower:

        return show_tasks()

    if text_lower.startswith("remove task"):

        task = user_text.replace(
            "remove task",
            ""
        ).strip()

        return remove_task(task)
    
    # GENERATE PYTHON CODE
    
    if text_lower.startswith("write python code for"):

        task = (
            user_text
            .replace("write python code for", "")
            .strip()
        )

        prompt = f"""
    Generate complete Python code.

    Task:
    {task}

    Return only code.
    """

        response = ask_ollama(prompt)

        return response
    
    # =========================
    # OPEN APPS
    # =========================

    open_result = open_app(user_text)

    if open_result:
        return open_result

    # =========================
    # CLOSE APPS
    # =========================

    close_result = close_app(user_text)

    if close_result:
        return close_result

    # =========================
    # VOLUME
    # =========================

    if "increase volume" in text_lower:
        return volume_up()

    if "decrease volume" in text_lower:
        return volume_down()

    if "mute" in text_lower:
        return mute()

    if "unmute" in text_lower:
        return unmute()

    # =========================
    # SCREENSHOT
    # =========================

    if (
        "screenshot" in text_lower
        or "take screenshot" in text_lower
        or "take a screenshot" in text_lower
    ):

        path = take_screenshot()

        return f"Screenshot saved, Boss. {path}"
    
    if text_lower.startswith("send "):

        try:

            parts = user_text.split(" to ")

            message = (
                parts[0]
                .replace("send", "")
                .strip()
            )

            contact = parts[1].strip()

            return send_whatsapp_message(
                contact,
                message
            )

        except:

            return (
                "Please say: "
                "send hello to Harsha"
            )
        
    if text_lower.startswith("call "):

        contact = (
            user_text
            .replace("call", "")
            .strip()
        )

        return whatsapp_call(contact)
    
    if text_lower.startswith("video call "):

        contact = user_text.replace(
            "video call",
            ""
        ).strip()

        return whatsapp_video_call(contact)
    
    conversation_history.append(
        f"Boss: {user_text}"
    )

    history_text = "\n".join(
        conversation_history[-MAX_HISTORY:]
    )
    

    # =========================
    # GOAL SYSTEM
    # =========================

    if "my goal is" in text_lower:

        goal = (
            user_text
            .replace("my goal is", "")
            .strip()
        )

        return set_goal(goal)

    if "what is my goal" in text_lower:

        goal = get_goal()

        if goal:

            return (
                f"Boss, your current goal is {goal}."
            )

        return (
            "You haven't set a goal yet, Boss."
        )

    if "clear my goal" in text_lower:

        return clear_goal()
    
    
    # =========================
    # OLLAMA FALLBACK
    # =========================

    print("REACHED OLLAMA")

    try:

        prompt = f"""
        {SYSTEM_PROMPT}

        Known facts about Boss:

        {memory_context}

        Previous conversation:

        {history_text}

        Boss: {user_text}

        Friday:
        """

        response = ask_ollama(prompt)

        conversation_history.append(
            f"Friday: {response}"
        )

        return response

    except Exception as e:

        print("OLLAMA ERROR:", e)

        return "Sorry Boss, I couldn't process that."