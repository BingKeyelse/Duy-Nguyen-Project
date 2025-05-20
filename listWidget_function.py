from import_all import*

class ListWidget():
    def __init__(self, parent: "MainWindow"):

        self.parent = parent

        self.list_NG_cam1()
        self.parent.ui.list_ng1cam.clicked.connect(self.show_img_NG_cam1)
        self.parent.ui.but_up_ng1cam.clicked.connect(self.up_currentRow_cam1)
        self.parent.ui.but_down_ng1cam.clicked.connect(self.down_currentRow_cam1)

        self.list_NG_4cam()
        self.parent.ui.list_ng4cam.clicked.connect(self.show_img_NG_4cam)
        self.parent.ui.but_up_ng4cam.clicked.connect(self.up_currentRow_4cam)
        self.parent.ui.but_down_ng4cam.clicked.connect(self.down_currentRow_4cam)


    def list_NG_cam1(self):

        filenames = self.parent.get_recent_filenames(self.parent.database[0])

        # Xóa danh sách cũ trước khi thêm mới
        self.parent.ui.list_ng1cam.clear() 
        if filenames:
            self.parent.ui.list_ng1cam.addItems(filenames)  # Thêm dữ liệu vào QListWidget
            print(f"✅ Đã tải NG cam 1 co {len(filenames)} file vào ListWidget")
        else:
            print("⚠️ Không có file nào trong database!")

    def list_NG_4cam(self):

        filenames = self.parent.get_recent_filenames(self.parent.database[1])

        # Xóa danh sách cũ trước khi thêm mới
        self.parent.ui.list_ng4cam.clear() 
        if filenames:
            self.parent.ui.list_ng4cam.addItems(filenames)  # Thêm dữ liệu vào QListWidget
            print(f"✅ Đã tải NG 4 cam co {len(filenames)} file vào ListWidget")
        else:
            print("⚠️ Không có file nào trong database!")

    def show_img_NG_cam1(self):
        item_img_ng = self.parent.ui.list_ng1cam.currentItem()
        if item_img_ng is not None:
            item_img_ng = item_img_ng.text()
            # print(self.parent.real_path_ng_cam1)
            # Lấy link 2 cái ảnh
            link_real_image= os.path.join(self.parent.real_path_ng_cam1, item_img_ng)
            link_virtual_image= os.path.join(self.parent.virtual_path_ng_cam1, item_img_ng)

            real_image=cv2.imread(link_real_image)
            virtual_image=cv2.imread(link_virtual_image)

            UI_of_main_gui.show_image_3chanel(self.parent,real_image, self.parent.ui.show_pic_real_ng1cam)
            UI_of_main_gui.show_image_3chanel(self.parent,virtual_image, self.parent.ui.show_pic_result_ng1cam)

    def show_img_NG_4cam(self):
        item_img_ng = self.parent.ui.list_ng4cam.currentItem()
        if item_img_ng is not None:
            item_img_ng = item_img_ng.text()

            # Lấy link 2 cái ảnh
            pic_real=[self.parent.ui.show_pic_real_1_ng4cam, self.parent.ui.show_pic_real_2_ng4cam,
                      self.parent.ui.show_pic_real_3_ng4cam, self.parent.ui.show_pic_real_4_ng4cam]
            
            pic_result=[self.parent.ui.show_pic_result_1_ng4cam, self.parent.ui.show_pic_result_2_ng4cam,
                        self.parent.ui.show_pic_result_3_ng4cam, self.parent.ui.show_pic_result_4_ng4cam]
            
            for i in range(2,6):
                link_real_path_ng4cam= os.path.join(self.parent.real_path_ng_4cam, f"cam{i}", item_img_ng)
                link_virtual_ng4cam= os.path.join(self.parent.virtual_path_ng_4cam, f"cam{i}", item_img_ng)

                real_image=cv2.imread(link_real_path_ng4cam)
                virtual_image=cv2.imread(link_virtual_ng4cam)

                UI_of_main_gui.show_image_3chanel(self.parent,real_image, pic_real[i-2] )
                UI_of_main_gui.show_image_3chanel(self.parent,virtual_image, pic_result[i-2])

    def up_currentRow_cam1(self):
        # count= self.ui.listWidget_NG.count()
        current_row= self.parent.ui.list_ng1cam.currentRow()
        if current_row>=1:
            current_row-=1
            self.parent.ui.list_ng1cam.setCurrentRow(current_row)
            self.show_img_NG_cam1()

    def up_currentRow_4cam(self):
        current_row= self.parent.ui.list_ng4cam.currentRow()
        if current_row>=1:
            current_row-=1
            self.parent.ui.list_ng4cam.setCurrentRow(current_row)
            self.show_img_NG_4cam()

    def down_currentRow_cam1(self):
        #### Xem so luong file trong path
        count_limit= self.parent.ui.list_ng1cam.count()

        current_row= self.parent.ui.list_ng1cam.currentRow()
        # print(current_row)
        if current_row< min(199, count_limit - 1):
            current_row+=1
            self.parent.ui.list_ng1cam.setCurrentRow(current_row)
            self.show_img_NG_cam1()

    def down_currentRow_4cam(self):
        #### Xem so luong file trong path
        count_limit= self.parent.ui.list_ng4cam.count()

        current_row= self.parent.ui.list_ng4cam.currentRow()
        # print(current_row)
        if current_row< min(199, count_limit - 1):
            current_row+=1
            self.parent.ui.list_ng4cam.setCurrentRow(current_row)
            self.show_img_NG_4cam()

    

