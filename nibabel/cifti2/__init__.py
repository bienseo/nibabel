# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""CIfTI format IO

.. currentmodule:: nibabel.cifti2

.. autosummary::
   :toctree: ../generated

   cifti2
"""

from .parse_cifti2 import Cifti2Extension
from .cifti2 import (Cifti2MetaData, Cifti2Header, Cifti2Image, Cifti2Label,
                     Cifti2LabelTable, Cifti2VertexIndices,
                     Cifti2VoxelIndicesIJK, Cifti2BrainModel, Cifti2Matrix,
                     Cifti2MatrixIndicesMap, Cifti2NamedMap, Cifti2Parcel,
                     Cifti2Surface,
                     Cifti2TransformationMatrixVoxelIndicesIJKtoXYZ,
                     Cifti2Vertices, Cifti2Volume, CIFTI_BRAIN_STRUCTURES,
                     Cifti2HeaderError, CIFTI_MODEL_TYPES, load, save)
