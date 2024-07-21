#!/bin/bash
sudo lsof -t -i:80 | xargs -r sudo kill -9
