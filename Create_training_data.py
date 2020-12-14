training_data = []
for img in tqdm(os.listdir(TRAIN_DIR)):
	label = label_img(img)
	path = os.path.join(TRAIN_DIR,img)
	img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (IMG_SIZE,IMG_SIZE))
	training_data.append([np.array(img),np.array(label)])
shuffle(training_data)
np.save('train_data.npy',training_data)
