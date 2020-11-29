from conans import ConanFile, CMake, tools
import os

class OpenCVConan(ConanFile):
    name = "opencv"
    version = "4.5.0"
    license = "BSD-3-Clause"
    homepage = "https://github.com/opencv/opencv"
    author = "Conan Community"
    topics = ("opencv", "computer-vision",
              "image-processing", "deep-learning")
    extension = "tar.gz"
    settings = "os", "compiler", "build_type", "arch"
    options = {"with_cuda" : [True, False]}
    default_options = {"with_cuda": True}

    def source(self):
        tools.download(F"{self.homepage}/archive/{self.version}.{self.extension}",
                       F"{self.name}-{self.version}.{self.extension}")
        tools.untargz(F"{self.name}-{self.version}.{self.extension}")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose = True

        print(self.settings)
        if self.settings.arch == "armv8":
            cmake.definitions["WITH_IPP"] = "OFF"

        cmake.configure(source_dir=F"../{self.name}-{self.version}", build_dir="build", args = ["-j8"])
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):

        pass