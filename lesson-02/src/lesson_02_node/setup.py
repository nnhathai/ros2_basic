from setuptools import find_packages, setup

package_name = 'lesson_02_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='haint@phenikaa-x.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_vel_publisher = lesson_02_node.turtle_vel_publisher:main',
            'turtle_vel_subscriber = lesson_02_node.turtle_vel_subscriber:main',
        ],
    },
)
