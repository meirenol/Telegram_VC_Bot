HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    API_ID = int(environ["4828785"])
    API_HASH = environ["542ae0f2a6bf570a56aea2b3d919f1cf"]
    SUDO_CHAT_ID = int(
        environ["-1001361350253"]
    )  # Chat where the bot will play the music.
    SUDOERS = list(
        int(x) for x in environ.get("SUDOERS", "").split()
    )  # Users which have special control over the bot.
    SESSION_STRING = environ["1BVtsOGUBu6GJnEu3OJShQz_Axte2elzjvw8fXlH1nSNN7GQEryOkO7wpIEnG_4R22gRHuc_YH2QqPsIJUoCSJWlV6-VEZDRRriFWeXhfGiEt0-Jx8A4nuFiOmWFLZGjQIoKOzWcJs91-dy0Sije9FSBdD-mNEQeH0g5VowZp_2PDsmcj_MvQmETpOSYi7oJZUARe0TNQ8OuISGA-4LQK0wFqFV8Z7f7JMjC01IfUkhNjlW0c_G4FBjtt4L0buvXAgpQgDZUl3Nvz9LpxZ3uPopNLLVH6-V6PZo5j4xQyTbdGf2FwPtMCXNzb8n9Z4N2PslA4mROM71JIksrZt53pZ7zluFOAtVw="]  # Check Readme for session
    ARQ_API_KEY = environ["X-API-KEY: ZOZCZV-NHGMNH-BAYELJ-XAZFQA-ARQ"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    SUDOERS = [1243703097, 13216546]
    ARQ_API_KEY = "Get this from @ARQRobot"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
