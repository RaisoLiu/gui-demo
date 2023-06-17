# Video Color Replacer GUI

此專案提供一個圖形化介面，用於載入視頻檔案，隨機選擇一些幀，並將指定的顏色替換為另一種顏色。
此專案目的是提供我一個 python GUI 的練習與範例，屬於 Bodypart Latent From Video (BLFV) 開發前的練習！

## 專案結構

- `main.py`: 主程式檔案，用於啟動GUI。
- `video_processing`: 包含視頻處理相關的模組。
  - `video_loader.py`: 包含從視頻檔案中讀取幀的函數。
  - `frame_selector.py`: 包含從視頻幀中隨機選擇幀的函數。
  - `color_replacer.py`: 包含替換影像中指定顏色的函數。
- `ui`: 包含GUI相關的模組。
  - `application_window.py`: 包含主要的GUI類別 `ApplicationWindow`。

## 使用方法

首先，請確保你已經安裝了所有必要的依賴包，包括 `numpy`, `cv2`, `tkinter`, `PIL`。你可以使用以下命令來安裝：

```
pip install numpy opencv-python python-tk pillow
```

然後，只需執行 `main.py` 檔案即可啟動GUI：

```
python main.py
```

在GUI中，你可以使用 "Load video" 按鈕來載入視頻檔案，使用 "Select color" 按鈕來選擇要替換的顏色，以及使用 "Next frame" 按鈕來切換到下一幀。

