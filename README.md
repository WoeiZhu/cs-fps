# CS FPS

CS 風格的 three.js 第一人稱射擊遊戲，整個遊戲就是一個 HTML 檔（`index.html`），電腦和手機都能玩。

**線上遊玩：** https://woeizhu.github.io/cs-fps/

## 操作

電腦：WASD 移動、滑鼠轉視角、左鍵射擊、右鍵瞄準、R 換彈、Space 跳、Ctrl/C 蹲、Shift 衝刺、1/2/3 換槍、Esc 暫停。

手機／平板（建議橫向）：左半邊拖曳移動（推到底往前是衝刺），右半邊拖曳轉視角，按住射擊鍵開槍（可邊按邊拖曳），瞄準和蹲點一下切換，另有換彈、跳、換槍、暫停鍵。網址加 `?touch=1` 或 `?touch=0` 可強制開關觸控介面。

## 原始碼

`src/game.js`（排版後的完整打包程式）與 `src/extra.css` 是可編輯的原始碼，`python3 src/build.py` 以 `src/shell.html` 為外殼重新產生 `index.html`。
