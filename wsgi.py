#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:54:22 2024

@author: alexswaine
"""

from app.app import server

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)
