from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="0.1",
    packages=find_packages(include=["study_reminders", "study_reminders.*"]),
    include_package_data=True,
    description="A package managing student study reminders",
    author="Mayen E",
    author_email="maywer2001@gmail.com",
    install_requires=['schedule'],
    entry_points={
        "console_scripts": [
            "study-reminder=study_reminders.main:main"
        ]
    }
)