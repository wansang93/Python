# 컴퓨터 비전에서 배운 알고리즘들()

TODO: 버그 확인 후 올릴 예정

## 1. Bug check

### 1-1. 파일을 열었는지 확인

```python
def is_open_file(fname):
    if not fname:
        status.configure(text='Open is failed. Please try again')
        return False
    return True
```

### 1-2. 파일 저장 유무 확인

```python
def is_save_file(fname):
    if not fname:
        status.configure(text=f'Save is failed. Please try again')
        return False
    return True
```

### 1-3. 빈 이미지 확인

```python
def is_empty_image():
    global out_image
    if len(out_image) == 0:
        tkinter.messagebox.showinfo(
            title='Error',
            message='The image is empty, Please open image')
        return True
    return False
```

## 2. FILE I/O

파일 Open의 순서는 Open -> Load -> Equal -> Display New -> Display Out 입니다.

### 2-1. malloc(메모리 확보)

```python

```

### 2-2. Open Image

```python

```

### 2-3. Load Image

```python

```

### 2-4. Equal Image

```python

```

### 2-5. Display New Image

```python

```

### 2-6. Display Out Image

```python

```

### 2-7. Save Image

```python

```

## 3. Pixel

### 3-1. Brighten/Darken

```python

```

### 3-2. Invert

```python

```

### 3-3. Parabola

```python

```

### 3-4. Morphing Image

```python

```

## 4. Statistics

### 4-1. Black & White

```python

```

### 4-2. Zoom Out(Image Averaging)

```python

```

### 4-3. Zoom In(Bilinear Interpolation)

```python

```

### 4-4. Histogram

```python

```

### 4-5. Histogram Custom

```python

```

### 4-6. Stretch

```python

```

### 4-7. End In

```python

```

### 4-8. Equalize

```python

```

## 5. Geometry

### 5-1. Upside Down

```python

```

### 5-2. Move

```python

```

### 5-3. Zoom Out

```python

```

### 5-4. Zoom In

```python

```

### 5-5. Rotate

```python

```

## 6. Area

### 6-1. Mask

```python

```

## 7. Format

### 7-1. Save Temp Image

```python

```

### 7-2. Get Avg, Max, Min

```python

```

### 7-3. Upload in MySQL

```python

```

### 7-4. Download from MySQL

```python

```

### 7-5. Save as CSV

```python

```

### 7-6. Open CSV File

```python

```

### 7-8. Save as Excel

```python

```

### 7-9. Save as Excel Art

```python

```

### 7-10. Open Excel File

```python

```

### 7-11. Load Excel

```python

```
