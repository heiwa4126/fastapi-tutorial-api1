#!/bin/sh
cd $(dirname $0)
uvicorn main:app --reload
