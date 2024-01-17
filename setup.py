import setuptools
import shutil
import os

try:
    package_dataFiles = []
    files = ['EasyMidiFileParserCpp.dll',
            'FluidsynthMIDIPlayer.dll',
            'libfluidsynth-3.dll', 
            'libgcc_s_sjlj-1.dll',
            'libglib-2.0-0.dll',
            'libgobject-2.0-0.dll',
            'libgomp-1.dll',
            'libgthread-2.0-0.dll',
            'libinstpatch-2.dll',
            'libintl-8.dll',
            'libsndfile-1.dll',
            'libstdc++-6.dll',
            'libwinpthread-1.dll']

    for file in files:
        dllPath = os.path.join(os.path.dirname(__file__), "../../../../Build/Modules/RuntimeModules/FluidsynthMIDIPlayer/Release/" + file)
        shutil.copyfile(dllPath, "PyMIDIMusic/dll/" + file)
        package_dataFiles.append("PyMIDIMusic/dll/" + file)

except:
    package_dataFiles = []
    files = ['libEasyMidiFileParserCpp.so',
            'libFluidsynthMIDIPlayer.so']

    for file in files:
        dllPath = os.path.join(os.path.dirname(__file__), "../../../../Build/Modules/RuntimeModules/FluidsynthMIDIPlayer/" + file)
        shutil.copyfile(dllPath, os.path.join(os.path.dirname(__file__), "PyMIDIMusic/dll/" + file))
        package_dataFiles.append("PyMIDIMusic/dll/" + file)

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyMIDIMusic',
    author='Progz',
    version = '0.0.1',
    author_email='progz.email@gmail.com',
    description='Python Wrapper of EasyMidiFileParserCpp',
    keywords='example, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ThomasProg/PyEasyMidiFileParserCpp',
    project_urls={
        'Documentation': 'https://github.com/ThomasProg/PyEasyMidiFileParserCpp',
        'Bug Reports':
        'https://github.com/ThomasProg/PyEasyMidiFileParserCpp/issues',
        'Source Code': 'https://github.com/ThomasProg/PyEasyMidiFileParserCpp',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    packages=['PyMIDIMusic'],
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
    include_package_data=True,
    package_data={"PyMIDIMusic": package_dataFiles},
)