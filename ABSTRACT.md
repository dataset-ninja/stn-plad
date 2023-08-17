The authors of the original paper developed the **STN Power Line Assets Dataset** to address the need for a reliable dataset for power line inspection using UAVs. The dataset contains high-resolution and real-world images of multiple high-voltage power line components, with 2,409 annotated objects classified into five classes: *transmission tower*, *insulator*, *spacer*, *tower plate*, and *Stockbridge damper*. These objects vary in size, orientation, illumination, angulation, and background.

Power line companies are increasingly using UAVs for inspection processes to avoid endangering workers who would otherwise have to climb high voltage power line towers. Detecting and classifying assets in power transmission lines is a crucial task for inspection purposes, but the scarcity of public data related to power line assets has hindered progress in this area. This dataset aims to facilitate research and advancements in this field.

Power grid blackouts can have severe consequences, affecting critical services such as hospitals, water supplies, and telecommunication. To prevent such situations, regular maintenance of power line equipment is essential. Traditionally, this involved manual inspection by teams, with workers climbing transmission towers to check their condition. However, this process is time-consuming, risky, and costly.

To improve the efficiency and safety of power line inspection, computer vision technologies, particularly deep learning networks, can be applied. Automating the detection of power line assets using UAVs reduces safety risks and allows for a more direct analysis of detected components. This dataset plays a crucial role in training deep learning networks, ensuring accuracy in the detection and classification of power line components.

The images in the dataset were captured using a DJI Phantom 4 Pro 1 drone, following a set of policies for data collection to ensure variability and consistency. Certified drone pilots captured the images, maintaining a similar distance to the transmission tower in wide shots to ensure high-resolution quality. The equipped camera is a DJI FC6310 and it can take pictures with a resolution of 5472×3078 (3:2) or 5472×3648 (16:9). Viewing angles, daytime, weather, angulation, and illumination conditions were varied to enhance the learning process for neural network models. Multiple transmission towers were photographed to capture variations in background and power line components.

The dataset contains 133 captured images with 2,409 annotated objects. Each object was carefully surrounded with a bounding box by two annotators to maintain consistency and accuracy. The dataset may seem small in terms of the total number of images, but it contains a reasonable amount of data considering the high-resolution nature of the images and the substantial number of object instances present in each image.