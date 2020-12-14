testing_data = []
for img in tqdm(os.listdir(TEST_DIR)):
	path = os.path.join(TEST_DIR,img)
	img_num = img.split('.')[0]
	img = cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE),(IMG_SIZE,IMG_SIZE))
	testing_data.append([np.array(img),img_num])
np.save('test_data.npy',testing_data)