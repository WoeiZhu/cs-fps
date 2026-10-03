# 用法：python3 build.py [game.js] [輸出.html]
# 以原始的 ../threejs-fps.html 為外殼（CSS、HUD 容器），把 game.js（已排版的完整打包程式）與 extra.css 塞回去。
# game.js 末端有 window.__game 測試掛鉤，發佈前可留可拿掉，不影響遊戲。
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'shell.html'), encoding='utf-8').read()
a = s.index('<script>') + 8; b = s.rindex('</script>')
js = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'game.js'), encoding='utf-8').read()
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, '..', 'index.html')
css = open(os.path.join(here, 'extra.css'), encoding='utf-8').read()
open(out, 'w', encoding='utf-8').write(s[:a].replace('</style>', css + '\n</style>', 1) + '\n' + js + '\n' + s[b:])
