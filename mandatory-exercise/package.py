# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackExercise(CMakePackage):
    """This is an exercise package aiming at a better understanding of Spack, Docker, CMake and Dependencies"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"

    maintainers("FabioTucciarone")
    license("Creative Commons", checked_by="FabioTucciarone")

    version("0.3.0", sha256="c179ccc9d56b724fcb7eeff8cebbc1afe2797929b99aa6e7d9b8478a014f2d02")
    version("0.2.0", sha256="010c900a3d4770116844636b89c1e42b1920f27c3da615543fb14f2ae9bb7f64")
    version("0.1.0", sha256="f1c212a58376fd78e9854576627e6927d7cb93ccffe3a162b1664570c491e3a7")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    variant("boost", default=True, description="SpackExercise with Boost support")
    depends_on("boost@1.65.1:", when="@0.2.0:")
    
    variant("yamlcpp", default=True, description="SpackExercise with yaml-cpp support")
    depends_on("yaml-cpp@0.7.0:", when="@0.3.0:")