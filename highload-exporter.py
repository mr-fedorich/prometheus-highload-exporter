#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Desc: Exporter for prometheus. Monitoring of heavy processes that load memory and cpu. Toplist.
# Repo: https://github.com/mr-fedorich/prometheus-highload-exporter
# Maintainer: mr.fedorich

import subprocess, os, sys

name = sys.argv[1]
export = sys.argv[2]

process = subprocess.Popen('ps -eo pid,cmd,%'+ export + ' --sort=-%'+ export +' | head', shell=True, stdout=subprocess.PIPE)
out = process.stdout.readlines()
i = 1

path = "/var/lib/prometheus/node_exporter/textfile_collector/"

file = open(path+export+".$$$", "w")
while i < len(out):
    pids = out[i].strip().split(" ", 1)[0]
    result = out[i].split()[1]
    cpu = out[i][-5:].strip()

    cmd = subprocess.Popen('ps -fp '+ pids+ ' -o cmd', shell=True, stdout=subprocess.PIPE)
    cmdout = cmd.stdout.readlines()
    s = 1
    while s < len(cmdout):
	command = cmdout[s].strip()
	template = name + '{metric="'+ result.strip() + '",cmd="'+ command +'"} ' + cpu.strip()
	print template
	s += 1
	file.write(template+"\n")
    i += 1
file.close()

os.rename(path+export+".$$$", path+export+".prom")
subprocess.call("chown prometheus:prometheus " + path + export + ".prom", shell=True)

