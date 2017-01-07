#!/usr/bin/env python3

from lib.pyratemp import pyratemp
import shm

templates = [
    ('../copter/src/shmdef.cpp.template', '../copter/src/shmdef.cpp'),
    ('../copter/src/shmdef.h.template', '../copter/src/shmdef.h'),
    ('../client/shmdef.go.template', '../client/shmdef.go'),
]

if __name__ == '__main__':
    for t in templates:
        pt = pyratemp.Template(filename=t[0])
        with open(t[1], 'w') as out:
            out.write(pt(shm=shm.shm))
