python3 -c "import sysconfig; print(sysconfig.get_config_var('INCLUDEPY'))"
/home/pronics/miniconda3/envs/myenv/include/python3.11
python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))"
/home/pronics/miniconda3/envs/myenv/lib
python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBRARY'))"
libpython3.11.a

cython --embed -o Main.c Main.py

gcc -o main main.c -I/home/pronics/miniconda3/envs/myenv/include/python3.11 \
    -L/home/pronics/miniconda3/envs/myenv/lib -lpython3.11 -lpthread -lm -lutil -ldl -fPIE -pie

gcc -o main Main.c -I/home/pronics/miniconda3/envs/myenv/include/python3.11     -L/home/pronics/miniconda3/envs/myenv/lib -lpython3.11 -lpthread -lm -lutil -ldl -fPIE -pie

pyinstaller --onefile --noconsole --debug=all --hidden-import=import_all --add-data "/home/pronics/Desktop/Duy-Nguyen-Project/data_txt/data_4cam.db:." Main.py

rm -rf Main.spec build dist

pyinstaller --onefile --noconsole --debug=all --log-level=DEBUG\
  --hidden-import=fontconfig  \
  --add-data "/home/pronics/Desktop/Duy-Nguyen-Project/data_txt/data_4cam.db:." \
  --add-data "/home/pronics/Desktop/Duy-Nguyen-Project/data_txt/data_cam1.db:." \
  Main.py

strace -f ./dist/Main 2>&1 | grep "No such file"
fc-cache -fv
sudo apt install --reinstall fontconfig

nuitka --onefile --standalone  --static-libpython=no --enable-plugin=pyqt5 --include-data-dir=data_txt=data_txt Main.py
 nuitka --onefile --standalone --static-libpython=no --enable-plugin=pyqt5 --include-module=PyQt5.sip Main.py

nuitka --onefile --standalone  --static-libpython=no --enable-plugin=pyqt5 --include-data-dir=data_txt=data_txt -include-data-dir=data_calib=data_calib  Main.py


nuitka --onefile --standalone \
		--static-libpython=no \
		--enable-plugin=pyqt5  \
    --include-package=onnxruntime \
    --include-package=tensorflow \
    --include-package=cv2 \
    --module-parameter=numba-disable-jit=yes \
    --noinclude-numba-mode=nofollow \
    --include-data-dir=/usr/local/cuda-12.2=cuda \
		--include-data-dir=data_txt=data_txt \
		--include-data-dir=data_calib=data_calib  \
		--include-data-dir=picture=picture \
		--include-data-dir=data_NG=data_NG  \
		--include-data-dir=icons=icons  \
		Main.py

numpy                        1.23.5

nuitka --onefile --standalone \
    --static-libpython=no \
    --enable-plugin=pyqt5 \
    --include-qt-plugins=all \
    --enable-plugin=numpy \
    --enable-plugin=tensorflow \
    --include-package=onnxruntime \
    --include-package=tensorflow \
    --include-package=cv2 \
    --module-parameter=numba-disable-jit=yes \
    --noinclude-numba-mode=nofollow \
    --include-data-dir=/usr/local/cuda-12.2=cuda \
    --include-data-dir=data_txt=data_txt \
    --include-data-dir=data_calib=data_calib \
    --include-data-dir=picture=picture \
    --include-data-dir=data_NG=data_NG \
    --include-data-dir=icons=icons \
    Main.py

nuitka --onefile --standalone \
    --jobs=auto \
    --static-libpython=no \
    --enable-plugin=pyqt5 \
    --include-qt-plugins=all \
    --enable-plugin=numpy \
    --include-package=onnxruntime \
    --module-parameter=numba-disable-jit=yes \
    --noinclude-numba-mode=nofollow \
    --include-data-dir=/usr/local/cuda-12.2=cuda \
    --include-data-dir=data_txt=data_txt \
    --include-data-dir=data_calib=data_calib \
    --include-data-dir=picture=picture \
    --include-data-dir=data_NG=data_NG \
    --include-data-dir=icons=icons \
    Main.py

nuitka --standalone \
    --jobs=$(( $(nproc) * 4 / 5 )) \
    --static-libpython=no \
    --enable-plugin=pyqt5 \
    --include-qt-plugins=all \
    --enable-plugin=numpy \
    --nofollow-import-to=tensorflow\
    --include-package=onnxruntime \
    --include-module=pypylon \
    --include-package-data=pypylon \
    --module-parameter=numba-disable-jit=yes \
    --noinclude-numba-mode=nofollow \
    --include-data-dir=/usr/local/cuda-12.2=cuda \
    --include-data-dir=data_txt=data_txt \
    --include-data-dir=data_calib=data_calib \
    --include-data-dir=picture=picture \
    --include-data-dir=data_NG=data_NG \
    --include-data-dir=icons=icons \
    --include-data-files=model_add_1.onnx=model_add_1.onnx \
    --include-data-files=main_gui.ui=main_gui.ui \
    --include-data-files=icons.qrc=icons.qrc \
    --include-data-files=icons_rc.py=icons_rc.py \
    Main.py

nuitka --standalone \
    --jobs=$(( $(nproc) * 4 / 5 )) \
    --static-libpython=no \
    --enable-plugin=pyqt5 \
    --include-qt-plugins=all \
    --enable-plugin=numpy \
    --include-package=pypylon \
    --include-data-dir=/opt/pylon=opt/pylon \
    --nofollow-import-to=tensorflow \
    --include-package=onnxruntime \
    --module-parameter=numba-disable-jit=yes \
    --noinclude-numba-mode=nofollow \
    --include-data-dir=/usr/local/cuda-12.2=cuda \
    --include-data-dir=data_txt=data_txt \
    --include-data-dir=data_calib=data_calib \
    --include-data-dir=picture=picture \
    --include-data-dir=data_NG=data_NG \
    --include-data-dir=icons=icons \
    --include-data-files=model_add_1.onnx=model_add_1.onnx \
    --include-data-files=main_gui.ui=main_gui.ui \
    --include-data-files=icons.qrc=icons.qrc \
    --include-data-files=icons_rc.py=icons_rc.py \
    Main.py


nuitka --onefile --standalone \
        --jobs=$(( $(nproc) * 4 / 5 )) \
		--static-libpython=no \
		--enable-plugin=pyqt5  \
        --nofollow-import-to=tensorflow \
        --include-package=onnxruntime \
		--noinclude-numba-mode=nofollow \
        --include-data-dir=/usr/local/cuda-12.2=cuda \
        --include-data-dir=data_txt=data_txt \
        --include-data-dir=data_calib=data_calib \
        --include-data-dir=picture=picture \
        --include-data-dir=data_NG=data_NG \
        --include-data-dir=icons=icons \
        --include-data-files=model_add_1.onnx=model_add_1.onnx \
        --include-data-files=main_gui.ui=main_gui.ui \
        --include-data-files=icons.qrc=icons.qrc \
        --include-data-files=icons_rc.py=icons_rc.py \
        Main.py


$(nproc)

# from PyQt5.QtCore import QLibraryInfo
# print(QLibraryInfo.location(QLibraryInfo.PluginsPath))
# /home/pronics/miniconda3/envs/lib_DuyNguyen/lib/python3.10/site-packages/PyQt5/Qt5/plugins

from PyQt5.QtCore import QLibraryInfo, QStandardPaths

plugins_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
print(plugins_path)
/home/pronics/Desktop/Duy-Nguyen-Project/Main.py