from writeUtils import *
from vector import * 

def writeBMP(filename, width, height, framebuffer):
    f = open(filename, 'bw')

    # pixel header
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + width * height * 3))
    f.write(word(0))
    f.write(word(0))
    f.write(dword(14 + 40))

    # info header
    f.write(dword(40))
    f.write(dword(width))
    f.write(dword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(width * height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # pixel data
    for y in range(height):
      for x in range(width):
        f.write(framebuffer[y][x])

    f.close()

def reflect(I, N):
  return (I - N * 2 * (N @ I) ).normalize()

def refract(I, N, roi):
  etai = 1  # para el aire
  etat = roi
  cosi = (I @ N) * -1

  if cosi < 0:
    cosi *= -1
    etai *= -1
    etat *= -1
    N *= -1
    
  eta = etai/etat
  k = 1 - eta ** 2 * (1 - cosi ** 2)

  if k < 0:
    return V3(0, 0, 0)

  cost = k ** 0.5
  return ((I * eta) + (N * (eta * cosi - cost))).normalize()





