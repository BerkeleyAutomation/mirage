from setuptools import setup

package_name = 'xembody_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lawrence',
    maintainer_email='chenyunliang12345@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'xembody_publisher = xembody_publisher.xembody_publisher:main'
        ],
    },
)
