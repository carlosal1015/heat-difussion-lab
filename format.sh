#!/bin/bash

isort src/*.py --float-to-top
black src/*.py
pyupgrade src/*.py --py312-plus