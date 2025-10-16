from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="0.2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    description="A package managing student study reminders",
    author="Mayen E",
    author_email="maywer2001@gmail.com",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "study-reminder=study_reminders.main:main"
        ]
    }
)