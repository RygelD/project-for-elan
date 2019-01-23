__version__ = 0.0
a = '''
#!/user/bin/env python3

# 2019 Rygel Dagenais
# The 'run' script for future games
# NOTICE:
# TO PLAY GAMES, YOU MUST DOWNLOAD PYTHON 3.6 OR NEWER FROM PYTHON.ORG and INSTALL IT
# YOU MUST ALSO TAKE THE FILES OUT OF THE FOLDER AND ONTO THE DESKTOP

# Compatible with: UPV 0.0

import sys
__version__ = 0.0
if __name__ == '__main__':

    if len(sys.argv) > 1:
        c = sys.argv[1]
        q = str(sys.argv[1])
        q.pop(1)
        q.pop(0)
        lef = str(q)
        left = lef[1:-1]
        eval('from ' + c +' import game as g')
        eval('g.run(' + left + ')')
'''
f = open('~/RygelGameLauncherScript','w')
f.write(a)
f.close()
