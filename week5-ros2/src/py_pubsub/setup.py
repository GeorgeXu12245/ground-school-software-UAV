maintainer='GeorgeXu',
maintainer_email='george_xu@berkeley.edu',
description='Examples of minimal publisher/subscriber using rclpy',
license='Apache-2.0',
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},
