#!/bin/bash

kill $(lsof -i:5001 -t)