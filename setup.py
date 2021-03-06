#!/usr/bin/env python

from distutils.core import setup

setup(name="PySynth",
        version="1.2",
        description="A simple music synthesizer for Python",
        author="Martin C. Doege",
        author_email="mdoege@compuserve.com",
	url="http://mdoege.github.io/PySynth/",
        py_modules=["pysynth", "pysynth_b", "pysynth_s", "pysynth_e", "pysynth_beeper", "play_wav", "mixfiles", "mkfreq", "demosongs"],
	scripts=["read_abc.py", "nokiacomposer2wav.py", "test_nokiacomposer2wav.py", "menv.py"],
)

