from setuptools import setup, find_packages

setup(
    name='PDF-ColorInverter',
    version='1.0.0',
    description='A tool to invert colors of PDF files',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF',
        'img2pdf'
    ],
    entry_points={
        'console_scripts': [
            'pdf_color_inverter=pdf_color_inverter:main'
        ]
    }
)
