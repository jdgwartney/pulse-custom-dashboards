from distutils.core import setup

setup(
    name='tspdash',
    version='0.0.1',
    url="https://github.com/boundary/pulse-custom-dashboards",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tspdash', ],
#    entry_points={
#        'console_scripts': [
#            'actionhandler = boundary.webhook_handler:main',
#        ],
#    },
#    scripts=[
#        'tsp-cli-env.sh',
#   ],
#    package_data={'boundary': ['templates/*']},
    license='Apache 2',
    description='Flash application for creating custom dashboards in TrueSight Pulse',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
