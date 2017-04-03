import setuptools


setuptools.setup(
    name="adrian.cgen",
    version="1.0.0",
    packages=setuptools.find_packages(),
    install_requires=["paka.funcreg"],
    extras_require={"testing": []},
    include_package_data=True,
    namespace_packages=["adrian"],
    zip_safe=False,
    url="https://github.com/adrian-lang/adrian.cgen",
    keywords="c codegen",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"],
    license="BSD",
    author="Adrian language team",
    author_email="i@93z.org")
