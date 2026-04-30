from distutils.core import setup


setup(
    name="husassistent-800",
    version="1.1.0",
    description="Husassistent 800 VT100",
    author="DragonMinded, modified by Mater242",
    license="Public Domain",
    packages=[
        "vthass",
    ],
    install_requires=[
        req for req in open("requirements.txt").read().split("\n") if len(req) > 0
    ],
    python_requires=">3.8",
    entry_points={
        "console_scripts": [
            "husassistent-800 = vthass.__main__:cli",
        ],
    },
)
