<div align="center">

<img src="estm_logo.png" alt="EST Meknès" height="90" />

# 👁️ Computer Vision from Scratch

### Image Segmentation & Contour Detection

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1000&color=00F5FF&center=true&vCenter=true&width=700&height=40&lines=Segmentation+implemented+from+scratch;Contour+detection+implemented+from+scratch;Load+%E2%86%92+Process+%E2%86%92+Compare+%E2%86%92+Save" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/From%20Scratch-00BFFF?style=for-the-badge" />

</div>

---

## 📖 About

A small image-processing application with two core features, both implemented **from scratch**:

- **Image segmentation**: splits an image into distinct regions and produces a segmented result.
- **Contour detection**: highlights the edges and outlines of the objects in an image.

The goal of the project is to really understand how these algorithms work under the hood, instead of relying on high-level library functions. The algorithms are built with **NumPy** and **Pillow** (no OpenCV), and everything is driven by a simple graphical interface built with **CustomTkinter**.

Developed at **EST Meknès**, as part of my DUT in Artificial Intelligence & Emerging Technologies (IATE).

---

## ✨ Features

| Action | What it does |
| :-- | :-- |
| 📂 **Load image** | Opens an image from your computer and displays it |
| 🔍 **Detect contours** | Computes the contours of the loaded image and shows the result |
| 🧩 **Segment image** | Segments the loaded image and shows the resulting image |
| 💾 **Save image** | Saves the resulting image to your computer |

---

## 🖼️ Demo

| Original image | Contour detection | Segmentation |
| :--: | :--: | :--: |
| <img src="screen_img_ori.PNG" width="280" /> | <img src="screen_detection_contours.PNG" width="280" /> | <img src="screen_img_segmente.PNG" width="280" /> |

---

## 🗂️ Project structure

```text
computer-vision-from-scratch/
├── main.py            # application entry point (CustomTkinter interface)
├── segmentation.py    # image segmentation
├── edges.py           # contour (edge) detection
├── filters.py         # image filters (Gaussian blur, median filter)
├── utilis.py          # helper functions (grayscale conversion, PIL/array conversion)
├── rapport_vision.pdf # project report
└── screen_*.PNG       # screenshots of the application
```

---

## 🚀 How to run

1. Clone the repository:

```bash
git clone https://github.com/ilyasNajim/computer-vision-from-scratch.git
cd computer-vision-from-scratch
```

2. Make sure **Python 3** is installed, then install the dependencies:

```bash
pip install numpy pillow customtkinter
```

3. Start the application:

```bash
python main.py
```

---

## 📄 Report

The full project report is available here: [rapport_vision.pdf](rapport_vision.pdf)

---

## 👤 Author

**Ilyas Najim** · AI & ML engineering student

<a href="https://www.linkedin.com/in/ilyas-najim-050215359/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://github.com/ilyasNajim"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
