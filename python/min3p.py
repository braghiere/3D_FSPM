from __future__ import print_function, absolute_import, division
import _min3p
import f90wrap.runtime
import logging

class Biol(f90wrap.runtime.FortranModule):
    """
    Module biol
    
    
    Defined at ../src/biol.f lines 1-140
    
    """
    @property
    def root_uptake(self):
        """
        Element root_uptake ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 24
        
        """
        return _min3p.f90wrap_biol__get__root_uptake()
    
    @root_uptake.setter
    def root_uptake(self, root_uptake):
        _min3p.f90wrap_biol__set__root_uptake(root_uptake)
    
    @property
    def vegetation_growth(self):
        """
        Element vegetation_growth ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 25
        
        """
        return _min3p.f90wrap_biol__get__vegetation_growth()
    
    @vegetation_growth.setter
    def vegetation_growth(self, vegetation_growth):
        _min3p.f90wrap_biol__set__vegetation_growth(vegetation_growth)
    
    @property
    def passive_uptake(self):
        """
        Element passive_uptake ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 26
        
        """
        return _min3p.f90wrap_biol__get__passive_uptake()
    
    @passive_uptake.setter
    def passive_uptake(self, passive_uptake):
        _min3p.f90wrap_biol__set__passive_uptake(passive_uptake)
    
    @property
    def update_root_rld(self):
        """
        Element update_root_rld ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 28
        
        """
        return _min3p.f90wrap_biol__get__update_root_rld()
    
    @update_root_rld.setter
    def update_root_rld(self, update_root_rld):
        _min3p.f90wrap_biol__set__update_root_rld(update_root_rld)
    
    @property
    def inside_rld(self):
        """
        Element inside_rld ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 29
        
        """
        return _min3p.f90wrap_biol__get__inside_rld()
    
    @inside_rld.setter
    def inside_rld(self, inside_rld):
        _min3p.f90wrap_biol__set__inside_rld(inside_rld)
    
    @property
    def coupled_archi_rld(self):
        """
        Element coupled_archi_rld ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 30
        
        """
        return _min3p.f90wrap_biol__get__coupled_archi_rld()
    
    @coupled_archi_rld.setter
    def coupled_archi_rld(self, coupled_archi_rld):
        _min3p.f90wrap_biol__set__coupled_archi_rld(coupled_archi_rld)
    
    @property
    def maillage_rld_coupled(self):
        """
        Element maillage_rld_coupled ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 32
        
        """
        return _min3p.f90wrap_biol__get__maillage_rld_coupled()
    
    @maillage_rld_coupled.setter
    def maillage_rld_coupled(self, maillage_rld_coupled):
        _min3p.f90wrap_biol__set__maillage_rld_coupled(maillage_rld_coupled)
    
    @property
    def file_rlddata(self):
        """
        Element file_rlddata ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 33
        
        """
        return _min3p.f90wrap_biol__get__file_rlddata()
    
    @file_rlddata.setter
    def file_rlddata(self, file_rlddata):
        _min3p.f90wrap_biol__set__file_rlddata(file_rlddata)
    
    @property
    def rootdensitynill(self):
        """
        Element rootdensitynill ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 34
        
        """
        return _min3p.f90wrap_biol__get__rootdensitynill()
    
    @rootdensitynill.setter
    def rootdensitynill(self, rootdensitynill):
        _min3p.f90wrap_biol__set__rootdensitynill(rootdensitynill)
    
    @property
    def pet(self):
        """
        Element pet ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 62
        
        """
        return _min3p.f90wrap_biol__get__pet()
    
    @pet.setter
    def pet(self, pet):
        _min3p.f90wrap_biol__set__pet(pet)
    
    @property
    def pe_soil(self):
        """
        Element pe_soil ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 63
        
        """
        return _min3p.f90wrap_biol__get__pe_soil()
    
    @pe_soil.setter
    def pe_soil(self, pe_soil):
        _min3p.f90wrap_biol__set__pe_soil(pe_soil)
    
    @property
    def scale_tree_growth(self):
        """
        Element scale_tree_growth ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 64
        
        """
        return _min3p.f90wrap_biol__get__scale_tree_growth()
    
    @scale_tree_growth.setter
    def scale_tree_growth(self, scale_tree_growth):
        _min3p.f90wrap_biol__set__scale_tree_growth(scale_tree_growth)
    
    @property
    def canopy_int(self):
        """
        Element canopy_int ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 65
        
        """
        return _min3p.f90wrap_biol__get__canopy_int()
    
    @canopy_int.setter
    def canopy_int(self, canopy_int):
        _min3p.f90wrap_biol__set__canopy_int(canopy_int)
    
    @property
    def time_soi(self):
        """
        Element time_soi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 66
        
        """
        return _min3p.f90wrap_biol__get__time_soi()
    
    @time_soi.setter
    def time_soi(self, time_soi):
        _min3p.f90wrap_biol__set__time_soi(time_soi)
    
    @property
    def time_rld(self):
        """
        Element time_rld ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 67
        
        """
        return _min3p.f90wrap_biol__get__time_rld()
    
    @time_rld.setter
    def time_rld(self, time_rld):
        _min3p.f90wrap_biol__set__time_rld(time_rld)
    
    @property
    def isoi(self):
        """
        Element isoi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/biol.f line 69
        
        """
        return _min3p.f90wrap_biol__get__isoi()
    
    @isoi.setter
    def isoi(self, isoi):
        _min3p.f90wrap_biol__set__isoi(isoi)
    
    @property
    def irld(self):
        """
        Element irld ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/biol.f line 70
        
        """
        return _min3p.f90wrap_biol__get__irld()
    
    @irld.setter
    def irld(self, irld):
        _min3p.f90wrap_biol__set__irld(irld)
    
    @property
    def irlddata(self):
        """
        Element irlddata ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/biol.f line 71
        
        """
        return _min3p.f90wrap_biol__get__irlddata()
    
    @irlddata.setter
    def irlddata(self, irlddata):
        _min3p.f90wrap_biol__set__irlddata(irlddata)
    
    @property
    def h1lim(self):
        """
        Element h1lim ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 115
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__h1lim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            h1lim = self._arrays[array_handle]
        else:
            h1lim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__h1lim)
            self._arrays[array_handle] = h1lim
        return h1lim
    
    @h1lim.setter
    def h1lim(self, h1lim):
        self.h1lim[...] = h1lim
    
    @property
    def h1field(self):
        """
        Element h1field ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 116
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__h1field(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            h1field = self._arrays[array_handle]
        else:
            h1field = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__h1field)
            self._arrays[array_handle] = h1field
        return h1field
    
    @h1field.setter
    def h1field(self, h1field):
        self.h1field[...] = h1field
    
    @property
    def h1opt(self):
        """
        Element h1opt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 117
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__h1opt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            h1opt = self._arrays[array_handle]
        else:
            h1opt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__h1opt)
            self._arrays[array_handle] = h1opt
        return h1opt
    
    @h1opt.setter
    def h1opt(self, h1opt):
        self.h1opt[...] = h1opt
    
    @property
    def satwlim(self):
        """
        Element satwlim ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 118
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__satwlim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwlim = self._arrays[array_handle]
        else:
            satwlim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__satwlim)
            self._arrays[array_handle] = satwlim
        return satwlim
    
    @satwlim.setter
    def satwlim(self, satwlim):
        self.satwlim[...] = satwlim
    
    @property
    def satwfield(self):
        """
        Element satwfield ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 119
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__satwfield(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwfield = self._arrays[array_handle]
        else:
            satwfield = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__satwfield)
            self._arrays[array_handle] = satwfield
        return satwfield
    
    @satwfield.setter
    def satwfield(self, satwfield):
        self.satwfield[...] = satwfield
    
    @property
    def satwopt(self):
        """
        Element satwopt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 120
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__satwopt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwopt = self._arrays[array_handle]
        else:
            satwopt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__satwopt)
            self._arrays[array_handle] = satwopt
        return satwopt
    
    @satwopt.setter
    def satwopt(self, satwopt):
        self.satwopt[...] = satwopt
    
    @property
    def satwh1(self):
        """
        Element satwh1 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 121
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__satwh1(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwh1 = self._arrays[array_handle]
        else:
            satwh1 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__satwh1)
            self._arrays[array_handle] = satwh1
        return satwh1
    
    @satwh1.setter
    def satwh1(self, satwh1):
        self.satwh1[...] = satwh1
    
    @property
    def rootdiff(self):
        """
        Element rootdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 122
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__rootdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rootdiff = self._arrays[array_handle]
        else:
            rootdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__rootdiff)
            self._arrays[array_handle] = rootdiff
        return rootdiff
    
    @rootdiff.setter
    def rootdiff(self, rootdiff):
        self.rootdiff[...] = rootdiff
    
    @property
    def totrootdiff(self):
        """
        Element totrootdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 123
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__totrootdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totrootdiff = self._arrays[array_handle]
        else:
            totrootdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__totrootdiff)
            self._arrays[array_handle] = totrootdiff
        return totrootdiff
    
    @totrootdiff.setter
    def totrootdiff(self, totrootdiff):
        self.totrootdiff[...] = totrootdiff
    
    @property
    def rootlengthdens(self):
        """
        Element rootlengthdens ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 124
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__rootlengthdens(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rootlengthdens = self._arrays[array_handle]
        else:
            rootlengthdens = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__rootlengthdens)
            self._arrays[array_handle] = rootlengthdens
        return rootlengthdens
    
    @rootlengthdens.setter
    def rootlengthdens(self, rootlengthdens):
        self.rootlengthdens[...] = rootlengthdens
    
    @property
    def rld(self):
        """
        Element rld ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 125
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__rld(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rld = self._arrays[array_handle]
        else:
            rld = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__rld)
            self._arrays[array_handle] = rld
        return rld
    
    @rld.setter
    def rld(self, rld):
        self.rld[...] = rld
    
    @property
    def rldbck(self):
        """
        Element rldbck ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 126
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__rldbck(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rldbck = self._arrays[array_handle]
        else:
            rldbck = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__rldbck)
            self._arrays[array_handle] = rldbck
        return rldbck
    
    @rldbck.setter
    def rldbck(self, rldbck):
        self.rldbck[...] = rldbck
    
    @property
    def water_red_factor(self):
        """
        Element water_red_factor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 127
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__water_red_factor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            water_red_factor = self._arrays[array_handle]
        else:
            water_red_factor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__water_red_factor)
            self._arrays[array_handle] = water_red_factor
        return water_red_factor
    
    @water_red_factor.setter
    def water_red_factor(self, water_red_factor):
        self.water_red_factor[...] = water_red_factor
    
    @property
    def uptakefactor(self):
        """
        Element uptakefactor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 128
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__uptakefactor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            uptakefactor = self._arrays[array_handle]
        else:
            uptakefactor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__uptakefactor)
            self._arrays[array_handle] = uptakefactor
        return uptakefactor
    
    @uptakefactor.setter
    def uptakefactor(self, uptakefactor):
        self.uptakefactor[...] = uptakefactor
    
    @property
    def puf(self):
        """
        Element puf ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 129
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_biol__array__puf(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            puf = self._arrays[array_handle]
        else:
            puf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_biol__array__puf)
            self._arrays[array_handle] = puf
        return puf
    
    @puf.setter
    def puf(self, puf):
        self.puf[...] = puf
    
    @property
    def canopy_evap_factor(self):
        """
        Element canopy_evap_factor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 130
        
        """
        return _min3p.f90wrap_biol__get__canopy_evap_factor()
    
    @canopy_evap_factor.setter
    def canopy_evap_factor(self, canopy_evap_factor):
        _min3p.f90wrap_biol__set__canopy_evap_factor(canopy_evap_factor)
    
    @property
    def rew0(self):
        """
        Element rew0 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 131
        
        """
        return _min3p.f90wrap_biol__get__rew0()
    
    @rew0.setter
    def rew0(self, rew0):
        _min3p.f90wrap_biol__set__rew0(rew0)
    
    @property
    def p1(self):
        """
        Element p1 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 132
        
        """
        return _min3p.f90wrap_biol__get__p1()
    
    @p1.setter
    def p1(self, p1):
        _min3p.f90wrap_biol__set__p1(p1)
    
    @property
    def rewm(self):
        """
        Element rewm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 133
        
        """
        return _min3p.f90wrap_biol__get__rewm()
    
    @rewm.setter
    def rewm(self, rewm):
        _min3p.f90wrap_biol__set__rewm(rewm)
    
    @property
    def v_prop(self):
        """
        Element v_prop ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/biol.f line 134
        
        """
        return _min3p.f90wrap_biol__get__v_prop()
    
    @v_prop.setter
    def v_prop(self, v_prop):
        _min3p.f90wrap_biol__set__v_prop(v_prop)
    
    @property
    def cmws(self):
        """
        Element cmws ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/biol.f line 136
        
        """
        return _min3p.f90wrap_biol__get__cmws()
    
    @cmws.setter
    def cmws(self, cmws):
        _min3p.f90wrap_biol__set__cmws(cmws)
    
    @property
    def compt_rld_coupled(self):
        """
        Element compt_rld_coupled ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/biol.f line 137
        
        """
        return _min3p.f90wrap_biol__get__compt_rld_coupled()
    
    @compt_rld_coupled.setter
    def compt_rld_coupled(self, compt_rld_coupled):
        _min3p.f90wrap_biol__set__compt_rld_coupled(compt_rld_coupled)
    
    @property
    def rootlengthdens_field(self):
        """
        Element rootlengthdens_field ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 139
        
        """
        return _min3p.f90wrap_biol__get__rootlengthdens_field()
    
    @rootlengthdens_field.setter
    def rootlengthdens_field(self, rootlengthdens_field):
        _min3p.f90wrap_biol__set__rootlengthdens_field(rootlengthdens_field)
    
    @property
    def randomdistrib_root(self):
        """
        Element randomdistrib_root ftype=logical pytype=bool
        
        
        Defined at ../src/biol.f line 140
        
        """
        return _min3p.f90wrap_biol__get__randomdistrib_root()
    
    @randomdistrib_root.setter
    def randomdistrib_root(self, randomdistrib_root):
        _min3p.f90wrap_biol__set__randomdistrib_root(randomdistrib_root)
    
    def __str__(self):
        ret = ['<biol>{\n']
        ret.append('    root_uptake : ')
        ret.append(repr(self.root_uptake))
        ret.append(',\n    vegetation_growth : ')
        ret.append(repr(self.vegetation_growth))
        ret.append(',\n    passive_uptake : ')
        ret.append(repr(self.passive_uptake))
        ret.append(',\n    update_root_rld : ')
        ret.append(repr(self.update_root_rld))
        ret.append(',\n    inside_rld : ')
        ret.append(repr(self.inside_rld))
        ret.append(',\n    coupled_archi_rld : ')
        ret.append(repr(self.coupled_archi_rld))
        ret.append(',\n    maillage_rld_coupled : ')
        ret.append(repr(self.maillage_rld_coupled))
        ret.append(',\n    file_rlddata : ')
        ret.append(repr(self.file_rlddata))
        ret.append(',\n    rootdensitynill : ')
        ret.append(repr(self.rootdensitynill))
        ret.append(',\n    pet : ')
        ret.append(repr(self.pet))
        ret.append(',\n    pe_soil : ')
        ret.append(repr(self.pe_soil))
        ret.append(',\n    scale_tree_growth : ')
        ret.append(repr(self.scale_tree_growth))
        ret.append(',\n    canopy_int : ')
        ret.append(repr(self.canopy_int))
        ret.append(',\n    time_soi : ')
        ret.append(repr(self.time_soi))
        ret.append(',\n    time_rld : ')
        ret.append(repr(self.time_rld))
        ret.append(',\n    isoi : ')
        ret.append(repr(self.isoi))
        ret.append(',\n    irld : ')
        ret.append(repr(self.irld))
        ret.append(',\n    irlddata : ')
        ret.append(repr(self.irlddata))
        ret.append(',\n    h1lim : ')
        ret.append(repr(self.h1lim))
        ret.append(',\n    h1field : ')
        ret.append(repr(self.h1field))
        ret.append(',\n    h1opt : ')
        ret.append(repr(self.h1opt))
        ret.append(',\n    satwlim : ')
        ret.append(repr(self.satwlim))
        ret.append(',\n    satwfield : ')
        ret.append(repr(self.satwfield))
        ret.append(',\n    satwopt : ')
        ret.append(repr(self.satwopt))
        ret.append(',\n    satwh1 : ')
        ret.append(repr(self.satwh1))
        ret.append(',\n    rootdiff : ')
        ret.append(repr(self.rootdiff))
        ret.append(',\n    totrootdiff : ')
        ret.append(repr(self.totrootdiff))
        ret.append(',\n    rootlengthdens : ')
        ret.append(repr(self.rootlengthdens))
        ret.append(',\n    rld : ')
        ret.append(repr(self.rld))
        ret.append(',\n    rldbck : ')
        ret.append(repr(self.rldbck))
        ret.append(',\n    water_red_factor : ')
        ret.append(repr(self.water_red_factor))
        ret.append(',\n    uptakefactor : ')
        ret.append(repr(self.uptakefactor))
        ret.append(',\n    puf : ')
        ret.append(repr(self.puf))
        ret.append(',\n    canopy_evap_factor : ')
        ret.append(repr(self.canopy_evap_factor))
        ret.append(',\n    rew0 : ')
        ret.append(repr(self.rew0))
        ret.append(',\n    p1 : ')
        ret.append(repr(self.p1))
        ret.append(',\n    rewm : ')
        ret.append(repr(self.rewm))
        ret.append(',\n    v_prop : ')
        ret.append(repr(self.v_prop))
        ret.append(',\n    cmws : ')
        ret.append(repr(self.cmws))
        ret.append(',\n    compt_rld_coupled : ')
        ret.append(repr(self.compt_rld_coupled))
        ret.append(',\n    rootlengthdens_field : ')
        ret.append(repr(self.rootlengthdens_field))
        ret.append(',\n    randomdistrib_root : ')
        ret.append(repr(self.randomdistrib_root))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

biol = Biol()

class Chem(f90wrap.runtime.FortranModule):
    """
    Module chem
    
    
    Defined at ../src/chem.f lines 1-1738
    
    """
    @property
    def acth2omin(self):
        """
        Element acth2omin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 168
        
        """
        return _min3p.f90wrap_chem__get__acth2omin()
    
    @acth2omin.setter
    def acth2omin(self, acth2omin):
        _min3p.f90wrap_chem__set__acth2omin(acth2omin)
    
    @property
    def dinc_lc(self):
        """
        Element dinc_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 169
        
        """
        return _min3p.f90wrap_chem__get__dinc_lc()
    
    @dinc_lc.setter
    def dinc_lc(self, dinc_lc):
        _min3p.f90wrap_chem__set__dinc_lc(dinc_lc)
    
    @property
    def ph_fixed(self):
        """
        Element ph_fixed ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 170
        
        """
        return _min3p.f90wrap_chem__get__ph_fixed()
    
    @ph_fixed.setter
    def ph_fixed(self, ph_fixed):
        _min3p.f90wrap_chem__set__ph_fixed(ph_fixed)
    
    @property
    def ph_inc(self):
        """
        Element ph_inc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 171
        
        """
        return _min3p.f90wrap_chem__get__ph_inc()
    
    @ph_inc.setter
    def ph_inc(self, ph_inc):
        _min3p.f90wrap_chem__set__ph_inc(ph_inc)
    
    @property
    def ph_start(self):
        """
        Element ph_start ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 172
        
        """
        return _min3p.f90wrap_chem__get__ph_start()
    
    @ph_start.setter
    def ph_start(self, ph_start):
        _min3p.f90wrap_chem__set__ph_start(ph_start)
    
    @property
    def ph_stop(self):
        """
        Element ph_stop ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 173
        
        """
        return _min3p.f90wrap_chem__get__ph_stop()
    
    @ph_stop.setter
    def ph_stop(self, ph_stop):
        _min3p.f90wrap_chem__set__ph_stop(ph_stop)
    
    @property
    def sionmax(self):
        """
        Element sionmax ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 174
        
        """
        return _min3p.f90wrap_chem__get__sionmax()
    
    @sionmax.setter
    def sionmax(self, sionmax):
        _min3p.f90wrap_chem__set__sionmax(sionmax)
    
    @property
    def srelfac_lc(self):
        """
        Element srelfac_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 175
        
        """
        return _min3p.f90wrap_chem__get__srelfac_lc()
    
    @srelfac_lc.setter
    def srelfac_lc(self, srelfac_lc):
        _min3p.f90wrap_chem__set__srelfac_lc(srelfac_lc)
    
    @property
    def tempc(self):
        """
        Element tempc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 176
        
        """
        return _min3p.f90wrap_chem__get__tempc()
    
    @tempc.setter
    def tempc(self, tempc):
        _min3p.f90wrap_chem__set__tempc(tempc)
    
    @property
    def tempk(self):
        """
        Element tempk ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 177
        
        """
        return _min3p.f90wrap_chem__get__tempk()
    
    @tempk.setter
    def tempk(self, tempk):
        _min3p.f90wrap_chem__set__tempk(tempk)
    
    @property
    def tfinal_lc(self):
        """
        Element tfinal_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 178
        
        """
        return _min3p.f90wrap_chem__get__tfinal_lc()
    
    @tfinal_lc.setter
    def tfinal_lc(self, tfinal_lc):
        _min3p.f90wrap_chem__set__tfinal_lc(tfinal_lc)
    
    @property
    def tinyrate(self):
        """
        Element tinyrate ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 179
        
        """
        return _min3p.f90wrap_chem__get__tinyrate()
    
    @tinyrate.setter
    def tinyrate(self, tinyrate):
        _min3p.f90wrap_chem__set__tinyrate(tinyrate)
    
    @property
    def time_factor_lc(self):
        """
        Element time_factor_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 180
        
        """
        return _min3p.f90wrap_chem__get__time_factor_lc()
    
    @time_factor_lc.setter
    def time_factor_lc(self, time_factor_lc):
        _min3p.f90wrap_chem__set__time_factor_lc(time_factor_lc)
    
    @property
    def tol_lc(self):
        """
        Element tol_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 181
        
        """
        return _min3p.f90wrap_chem__get__tol_lc()
    
    @tol_lc.setter
    def tol_lc(self, tol_lc):
        _min3p.f90wrap_chem__set__tol_lc(tol_lc)
    
    @property
    def ncorder(self):
        """
        Element ncorder ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 183
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ncorder(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ncorder = self._arrays[array_handle]
        else:
            ncorder = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ncorder)
            self._arrays[array_handle] = ncorder
        return ncorder
    
    @ncorder.setter
    def ncorder(self, ncorder):
        self.ncorder[...] = ncorder
    
    @property
    def iph_steps(self):
        """
        Element iph_steps ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 185
        
        """
        return _min3p.f90wrap_chem__get__iph_steps()
    
    @iph_steps.setter
    def iph_steps(self, iph_steps):
        _min3p.f90wrap_chem__set__iph_steps(iph_steps)
    
    @property
    def maxit_lc(self):
        """
        Element maxit_lc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 186
        
        """
        return _min3p.f90wrap_chem__get__maxit_lc()
    
    @maxit_lc.setter
    def maxit_lc(self, maxit_lc):
        _min3p.f90wrap_chem__set__maxit_lc(maxit_lc)
    
    @property
    def idetail_lc(self):
        """
        Element idetail_lc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 187
        
        """
        return _min3p.f90wrap_chem__get__idetail_lc()
    
    @idetail_lc.setter
    def idetail_lc(self, idetail_lc):
        _min3p.f90wrap_chem__set__idetail_lc(idetail_lc)
    
    @property
    def ittot_lc(self):
        """
        Element ittot_lc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 188
        
        """
        return _min3p.f90wrap_chem__get__ittot_lc()
    
    @ittot_lc.setter
    def ittot_lc(self, ittot_lc):
        _min3p.f90wrap_chem__set__ittot_lc(ittot_lc)
    
    @property
    def iter_lc(self):
        """
        Element iter_lc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 189
        
        """
        return _min3p.f90wrap_chem__get__iter_lc()
    
    @iter_lc.setter
    def iter_lc(self, iter_lc):
        _min3p.f90wrap_chem__set__iter_lc(iter_lc)
    
    @property
    def naq(self):
        """
        Element naq ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 190
        
        """
        return _min3p.f90wrap_chem__get__naq()
    
    @naq.setter
    def naq(self, naq):
        _min3p.f90wrap_chem__set__naq(naq)
    
    @property
    def nc(self):
        """
        Element nc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 191
        
        """
        return _min3p.f90wrap_chem__get__nc()
    
    @nc.setter
    def nc(self, nc):
        _min3p.f90wrap_chem__set__nc(nc)
    
    @property
    def nx(self):
        """
        Element nx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 192
        
        """
        return _min3p.f90wrap_chem__get__nx()
    
    @nx.setter
    def nx(self, nx):
        _min3p.f90wrap_chem__set__nx(nx)
    
    @property
    def nm(self):
        """
        Element nm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 193
        
        """
        return _min3p.f90wrap_chem__get__nm()
    
    @nm.setter
    def nm(self, nm):
        _min3p.f90wrap_chem__set__nm(nm)
    
    @property
    def nmx(self):
        """
        Element nmx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 194
        
        """
        return _min3p.f90wrap_chem__get__nmx()
    
    @nmx.setter
    def nmx(self, nmx):
        _min3p.f90wrap_chem__set__nmx(nmx)
    
    @property
    def nopu(self):
        """
        Element nopu ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 195
        
        """
        return _min3p.f90wrap_chem__get__nopu()
    
    @nopu.setter
    def nopu(self, nopu):
        _min3p.f90wrap_chem__set__nopu(nopu)
    
    @property
    def ng(self):
        """
        Element ng ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 196
        
        """
        return _min3p.f90wrap_chem__get__ng()
    
    @ng.setter
    def ng(self, ng):
        _min3p.f90wrap_chem__set__ng(ng)
    
    @property
    def nr(self):
        """
        Element nr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 197
        
        """
        return _min3p.f90wrap_chem__get__nr()
    
    @nr.setter
    def nr(self, nr):
        _min3p.f90wrap_chem__set__nr(nr)
    
    @property
    def nph_steps(self):
        """
        Element nph_steps ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 198
        
        """
        return _min3p.f90wrap_chem__get__nph_steps()
    
    @nph_steps.setter
    def nph_steps(self, nph_steps):
        _min3p.f90wrap_chem__set__nph_steps(nph_steps)
    
    @property
    def ivolindice(self):
        """
        Element ivolindice ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 200
        
        """
        return _min3p.f90wrap_chem__get__ivolindice()
    
    @ivolindice.setter
    def ivolindice(self, ivolindice):
        _min3p.f90wrap_chem__set__ivolindice(ivolindice)
    
    @property
    def minequil(self):
        """
        Element minequil ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 202
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__minequil(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            minequil = self._arrays[array_handle]
        else:
            minequil = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__minequil)
            self._arrays[array_handle] = minequil
        return minequil
    
    @minequil.setter
    def minequil(self, minequil):
        self.minequil[...] = minequil
    
    @property
    def compute_alkalinity(self):
        """
        Element compute_alkalinity ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 204
        
        """
        return _min3p.f90wrap_chem__get__compute_alkalinity()
    
    @compute_alkalinity.setter
    def compute_alkalinity(self, compute_alkalinity):
        _min3p.f90wrap_chem__set__compute_alkalinity(compute_alkalinity)
    
    @property
    def explicit_surface(self):
        """
        Element explicit_surface ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 205
        
        """
        return _min3p.f90wrap_chem__get__explicit_surface()
    
    @explicit_surface.setter
    def explicit_surface(self, explicit_surface):
        _min3p.f90wrap_chem__set__explicit_surface(explicit_surface)
    
    @property
    def finite_minerals(self):
        """
        Element finite_minerals ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 206
        
        """
        return _min3p.f90wrap_chem__get__finite_minerals()
    
    @finite_minerals.setter
    def finite_minerals(self, finite_minerals):
        _min3p.f90wrap_chem__set__finite_minerals(finite_minerals)
    
    @property
    def implicit_surface(self):
        """
        Element implicit_surface ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 207
        
        """
        return _min3p.f90wrap_chem__get__implicit_surface()
    
    @implicit_surface.setter
    def implicit_surface(self, implicit_surface):
        _min3p.f90wrap_chem__set__implicit_surface(implicit_surface)
    
    @property
    def new_database(self):
        """
        Element new_database ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 208
        
        """
        return _min3p.f90wrap_chem__get__new_database()
    
    @new_database.setter
    def new_database(self, new_database):
        _min3p.f90wrap_chem__set__new_database(new_database)
    
    @property
    def ph_sweep(self):
        """
        Element ph_sweep ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 209
        
        """
        return _min3p.f90wrap_chem__get__ph_sweep()
    
    @ph_sweep.setter
    def ph_sweep(self, ph_sweep):
        _min3p.f90wrap_chem__set__ph_sweep(ph_sweep)
    
    @property
    def reactive_minerals(self):
        """
        Element reactive_minerals ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 210
        
        """
        return _min3p.f90wrap_chem__get__reactive_minerals()
    
    @reactive_minerals.setter
    def reactive_minerals(self, reactive_minerals):
        _min3p.f90wrap_chem__set__reactive_minerals(reactive_minerals)
    
    @property
    def redox_equil_lc(self):
        """
        Element redox_equil_lc ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 211
        
        """
        return _min3p.f90wrap_chem__get__redox_equil_lc()
    
    @redox_equil_lc.setter
    def redox_equil_lc(self, redox_equil_lc):
        _min3p.f90wrap_chem__set__redox_equil_lc(redox_equil_lc)
    
    @property
    def search_database(self):
        """
        Element search_database ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 212
        
        """
        return _min3p.f90wrap_chem__get__search_database()
    
    @search_database.setter
    def search_database(self, search_database):
        _min3p.f90wrap_chem__set__search_database(search_database)
    
    @property
    def specified_ph(self):
        """
        Element specified_ph ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 213
        
        """
        return _min3p.f90wrap_chem__get__specified_ph()
    
    @specified_ph.setter
    def specified_ph(self, specified_ph):
        _min3p.f90wrap_chem__set__specified_ph(specified_ph)
    
    @property
    def temp_corr(self):
        """
        Element temp_corr ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 214
        
        """
        return _min3p.f90wrap_chem__get__temp_corr()
    
    @temp_corr.setter
    def temp_corr(self, temp_corr):
        _min3p.f90wrap_chem__set__temp_corr(temp_corr)
    
    @property
    def temp_field(self):
        """
        Element temp_field ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 215
        
        """
        return _min3p.f90wrap_chem__get__temp_field()
    
    @temp_field.setter
    def temp_field(self, temp_field):
        _min3p.f90wrap_chem__set__temp_field(temp_field)
    
    @property
    def tstart_to_equil(self):
        """
        Element tstart_to_equil ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 216
        
        """
        return _min3p.f90wrap_chem__get__tstart_to_equil()
    
    @tstart_to_equil.setter
    def tstart_to_equil(self, tstart_to_equil):
        _min3p.f90wrap_chem__set__tstart_to_equil(tstart_to_equil)
    
    @property
    def tstart_to_tfinal(self):
        """
        Element tstart_to_tfinal ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 217
        
        """
        return _min3p.f90wrap_chem__get__tstart_to_tfinal()
    
    @tstart_to_tfinal.setter
    def tstart_to_tfinal(self, tstart_to_tfinal):
        _min3p.f90wrap_chem__set__tstart_to_tfinal(tstart_to_tfinal)
    
    @property
    def adav(self):
        """
        Element adav ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 268
        
        """
        return _min3p.f90wrap_chem__get__adav()
    
    @adav.setter
    def adav(self, adav):
        _min3p.f90wrap_chem__set__adav(adav)
    
    @property
    def avog_const(self):
        """
        Element avog_const ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 269
        
        """
        return _min3p.f90wrap_chem__get__avog_const()
    
    @avog_const.setter
    def avog_const(self, avog_const):
        _min3p.f90wrap_chem__set__avog_const(avog_const)
    
    @property
    def bdav(self):
        """
        Element bdav ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 270
        
        """
        return _min3p.f90wrap_chem__get__bdav()
    
    @bdav.setter
    def bdav(self, bdav):
        _min3p.f90wrap_chem__set__bdav(bdav)
    
    @property
    def diel_const(self):
        """
        Element diel_const ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 271
        
        """
        return _min3p.f90wrap_chem__get__diel_const()
    
    @diel_const.setter
    def diel_const(self, diel_const):
        _min3p.f90wrap_chem__set__diel_const(diel_const)
    
    @property
    def dhad(self):
        """
        Element dhad ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 272
        
        """
        return _min3p.f90wrap_chem__get__dhad()
    
    @dhad.setter
    def dhad(self, dhad):
        _min3p.f90wrap_chem__set__dhad(dhad)
    
    @property
    def dhbd(self):
        """
        Element dhbd ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 273
        
        """
        return _min3p.f90wrap_chem__get__dhbd()
    
    @dhbd.setter
    def dhbd(self, dhbd):
        _min3p.f90wrap_chem__set__dhbd(dhbd)
    
    @property
    def ehfac(self):
        """
        Element ehfac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 274
        
        """
        return _min3p.f90wrap_chem__get__ehfac()
    
    @ehfac.setter
    def ehfac(self, ehfac):
        _min3p.f90wrap_chem__set__ehfac(ehfac)
    
    @property
    def farad_const(self):
        """
        Element farad_const ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 275
        
        """
        return _min3p.f90wrap_chem__get__farad_const()
    
    @farad_const.setter
    def farad_const(self, farad_const):
        _min3p.f90wrap_chem__set__farad_const(farad_const)
    
    @property
    def g_acc(self):
        """
        Element g_acc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 276
        
        """
        return _min3p.f90wrap_chem__get__g_acc()
    
    @g_acc.setter
    def g_acc(self, g_acc):
        _min3p.f90wrap_chem__set__g_acc(g_acc)
    
    @property
    def pa_atm(self):
        """
        Element pa_atm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 277
        
        """
        return _min3p.f90wrap_chem__get__pa_atm()
    
    @pa_atm.setter
    def pa_atm(self, pa_atm):
        _min3p.f90wrap_chem__set__pa_atm(pa_atm)
    
    @property
    def permit_const(self):
        """
        Element permit_const ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 278
        
        """
        return _min3p.f90wrap_chem__get__permit_const()
    
    @permit_const.setter
    def permit_const(self, permit_const):
        _min3p.f90wrap_chem__set__permit_const(permit_const)
    
    @property
    def pres_atm(self):
        """
        Element pres_atm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 279
        
        """
        return _min3p.f90wrap_chem__get__pres_atm()
    
    @pres_atm.setter
    def pres_atm(self, pres_atm):
        _min3p.f90wrap_chem__set__pres_atm(pres_atm)
    
    @property
    def tempcs(self):
        """
        Element tempcs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 280
        
        """
        return _min3p.f90wrap_chem__get__tempcs()
    
    @tempcs.setter
    def tempcs(self, tempcs):
        _min3p.f90wrap_chem__set__tempcs(tempcs)
    
    @property
    def tempks(self):
        """
        Element tempks ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 281
        
        """
        return _min3p.f90wrap_chem__get__tempks()
    
    @tempks.setter
    def tempks(self, tempks):
        _min3p.f90wrap_chem__set__tempks(tempks)
    
    @property
    def tconv(self):
        """
        Element tconv ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 282
        
        """
        return _min3p.f90wrap_chem__get__tconv()
    
    @tconv.setter
    def tconv(self, tconv):
        _min3p.f90wrap_chem__set__tconv(tconv)
    
    @property
    def rgas(self):
        """
        Element rgas ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 283
        
        """
        return _min3p.f90wrap_chem__get__rgas()
    
    @rgas.setter
    def rgas(self, rgas):
        _min3p.f90wrap_chem__set__rgas(rgas)
    
    @property
    def rgascal(self):
        """
        Element rgascal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 284
        
        """
        return _min3p.f90wrap_chem__get__rgascal()
    
    @rgascal.setter
    def rgascal(self, rgascal):
        _min3p.f90wrap_chem__set__rgascal(rgascal)
    
    @property
    def rgasjoule(self):
        """
        Element rgasjoule ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 285
        
        """
        return _min3p.f90wrap_chem__get__rgasjoule()
    
    @rgasjoule.setter
    def rgasjoule(self, rgasjoule):
        _min3p.f90wrap_chem__set__rgasjoule(rgasjoule)
    
    @property
    def rho_w(self):
        """
        Element rho_w ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 286
        
        """
        return _min3p.f90wrap_chem__get__rho_w()
    
    @rho_w.setter
    def rho_w(self, rho_w):
        _min3p.f90wrap_chem__set__rho_w(rho_w)
    
    @property
    def delt_lc(self):
        """
        Element delt_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 304
        
        """
        return _min3p.f90wrap_chem__get__delt_lc()
    
    @delt_lc.setter
    def delt_lc(self, delt_lc):
        _min3p.f90wrap_chem__set__delt_lc(delt_lc)
    
    @property
    def delt_max_lc(self):
        """
        Element delt_max_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 305
        
        """
        return _min3p.f90wrap_chem__get__delt_max_lc()
    
    @delt_max_lc.setter
    def delt_max_lc(self, delt_max_lc):
        _min3p.f90wrap_chem__set__delt_max_lc(delt_max_lc)
    
    @property
    def ntstp_lc(self):
        """
        Element ntstp_lc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 307
        
        """
        return _min3p.f90wrap_chem__get__ntstp_lc()
    
    @ntstp_lc.setter
    def ntstp_lc(self, ntstp_lc):
        _min3p.f90wrap_chem__set__ntstp_lc(ntstp_lc)
    
    @property
    def ilbb(self):
        """
        Element ilbb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 371
        
        """
        return _min3p.f90wrap_chem__get__ilbb()
    
    @ilbb.setter
    def ilbb(self, ilbb):
        _min3p.f90wrap_chem__set__ilbb(ilbb)
    
    @property
    def ilbc(self):
        """
        Element ilbc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 372
        
        """
        return _min3p.f90wrap_chem__get__ilbc()
    
    @ilbc.setter
    def ilbc(self, ilbc):
        _min3p.f90wrap_chem__set__ilbc(ilbc)
    
    @property
    def ilbd(self):
        """
        Element ilbd ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 373
        
        """
        return _min3p.f90wrap_chem__get__ilbd()
    
    @ilbd.setter
    def ilbd(self, ilbd):
        _min3p.f90wrap_chem__set__ilbd(ilbd)
    
    @property
    def ilbg(self):
        """
        Element ilbg ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 374
        
        """
        return _min3p.f90wrap_chem__get__ilbg()
    
    @ilbg.setter
    def ilbg(self, ilbg):
        _min3p.f90wrap_chem__set__ilbg(ilbg)
    
    @property
    def ilbgr(self):
        """
        Element ilbgr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 375
        
        """
        return _min3p.f90wrap_chem__get__ilbgr()
    
    @ilbgr.setter
    def ilbgr(self, ilbgr):
        _min3p.f90wrap_chem__set__ilbgr(ilbgr)
    
    @property
    def ilbm(self):
        """
        Element ilbm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 376
        
        """
        return _min3p.f90wrap_chem__get__ilbm()
    
    @ilbm.setter
    def ilbm(self, ilbm):
        _min3p.f90wrap_chem__set__ilbm(ilbm)
    
    @property
    def ilbi(self):
        """
        Element ilbi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 377
        
        """
        return _min3p.f90wrap_chem__get__ilbi()
    
    @ilbi.setter
    def ilbi(self, ilbi):
        _min3p.f90wrap_chem__set__ilbi(ilbi)
    
    @property
    def ilbs(self):
        """
        Element ilbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 378
        
        """
        return _min3p.f90wrap_chem__get__ilbs()
    
    @ilbs.setter
    def ilbs(self, ilbs):
        _min3p.f90wrap_chem__set__ilbs(ilbs)
    
    @property
    def ilbt(self):
        """
        Element ilbt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 379
        
        """
        return _min3p.f90wrap_chem__get__ilbt()
    
    @ilbt.setter
    def ilbt(self, ilbt):
        _min3p.f90wrap_chem__set__ilbt(ilbt)
    
    @property
    def ilbv(self):
        """
        Element ilbv ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 380
        
        """
        return _min3p.f90wrap_chem__get__ilbv()
    
    @ilbv.setter
    def ilbv(self, ilbv):
        _min3p.f90wrap_chem__set__ilbv(ilbv)
    
    @property
    def ilbx(self):
        """
        Element ilbx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 381
        
        """
        return _min3p.f90wrap_chem__get__ilbx()
    
    @ilbx.setter
    def ilbx(self, ilbx):
        _min3p.f90wrap_chem__set__ilbx(ilbx)
    
    @property
    def lb_output(self):
        """
        Element lb_output ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 383
        
        """
        return _min3p.f90wrap_chem__get__lb_output()
    
    @lb_output.setter
    def lb_output(self, lb_output):
        _min3p.f90wrap_chem__set__lb_output(lb_output)
    
    @property
    def pe_output(self):
        """
        Element pe_output ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 384
        
        """
        return _min3p.f90wrap_chem__get__pe_output()
    
    @pe_output.setter
    def pe_output(self, pe_output):
        _min3p.f90wrap_chem__set__pe_output(pe_output)
    
    @property
    def ph_output(self):
        """
        Element ph_output ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 385
        
        """
        return _min3p.f90wrap_chem__get__ph_output()
    
    @ph_output.setter
    def ph_output(self, ph_output):
        _min3p.f90wrap_chem__set__ph_output(ph_output)
    
    @property
    def actv(self):
        """
        Element actv ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 488
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__actv(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            actv = self._arrays[array_handle]
        else:
            actv = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__actv)
            self._arrays[array_handle] = actv
        return actv
    
    @actv.setter
    def actv(self, actv):
        self.actv[...] = actv
    
    @property
    def alkfacc(self):
        """
        Element alkfacc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 489
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__alkfacc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            alkfacc = self._arrays[array_handle]
        else:
            alkfacc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__alkfacc)
            self._arrays[array_handle] = alkfacc
        return alkfacc
    
    @alkfacc.setter
    def alkfacc(self, alkfacc):
        self.alkfacc[...] = alkfacc
    
    @property
    def alkfacx(self):
        """
        Element alkfacx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 490
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__alkfacx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            alkfacx = self._arrays[array_handle]
        else:
            alkfacx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__alkfacx)
            self._arrays[array_handle] = alkfacx
        return alkfacx
    
    @alkfacx.setter
    def alkfacx(self, alkfacx):
        self.alkfacx[...] = alkfacx
    
    @property
    def totcinit(self):
        """
        Element totcinit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 491
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcinit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcinit = self._arrays[array_handle]
        else:
            totcinit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcinit)
            self._arrays[array_handle] = totcinit
        return totcinit
    
    @totcinit.setter
    def totcinit(self, totcinit):
        self.totcinit[...] = totcinit
    
    @property
    def totcn(self):
        """
        Element totcn ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 492
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcn(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcn = self._arrays[array_handle]
        else:
            totcn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcn)
            self._arrays[array_handle] = totcn
        return totcn
    
    @totcn.setter
    def totcn(self, totcn):
        self.totcn[...] = totcn
    
    @property
    def totcmin(self):
        """
        Element totcmin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 493
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcmin = self._arrays[array_handle]
        else:
            totcmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcmin)
            self._arrays[array_handle] = totcmin
        return totcmin
    
    @totcmin.setter
    def totcmin(self, totcmin):
        self.totcmin[...] = totcmin
    
    @property
    def totco(self):
        """
        Element totco ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 494
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totco(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totco = self._arrays[array_handle]
        else:
            totco = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totco)
            self._arrays[array_handle] = totco
        return totco
    
    @totco.setter
    def totco(self, totco):
        self.totco[...] = totco
    
    @property
    def ccnew(self):
        """
        Element ccnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 495
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ccnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ccnew = self._arrays[array_handle]
        else:
            ccnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ccnew)
            self._arrays[array_handle] = ccnew
        return ccnew
    
    @ccnew.setter
    def ccnew(self, ccnew):
        self.ccnew[...] = ccnew
    
    @property
    def ccold(self):
        """
        Element ccold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 496
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ccold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ccold = self._arrays[array_handle]
        else:
            ccold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ccold)
            self._arrays[array_handle] = ccold
        return ccold
    
    @ccold.setter
    def ccold(self, ccold):
        self.ccold[...] = ccold
    
    @property
    def gamma_l(self):
        """
        Element gamma_l ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 497
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gamma_l(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gamma_l = self._arrays[array_handle]
        else:
            gamma_l = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gamma_l)
            self._arrays[array_handle] = gamma_l
        return gamma_l
    
    @gamma_l.setter
    def gamma_l(self, gamma_l):
        self.gamma_l[...] = gamma_l
    
    @property
    def chargec(self):
        """
        Element chargec ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 498
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chargec(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chargec = self._arrays[array_handle]
        else:
            chargec = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chargec)
            self._arrays[array_handle] = chargec
        return chargec
    
    @chargec.setter
    def chargec(self, chargec):
        self.chargec[...] = chargec
    
    @property
    def gfwc(self):
        """
        Element gfwc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 499
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwc = self._arrays[array_handle]
        else:
            gfwc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwc)
            self._arrays[array_handle] = gfwc
        return gfwc
    
    @gfwc.setter
    def gfwc(self, gfwc):
        self.gfwc[...] = gfwc
    
    @property
    def distcoff_lc(self):
        """
        Element distcoff_lc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 500
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__distcoff_lc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            distcoff_lc = self._arrays[array_handle]
        else:
            distcoff_lc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__distcoff_lc)
            self._arrays[array_handle] = distcoff_lc
        return distcoff_lc
    
    @distcoff_lc.setter
    def distcoff_lc(self, distcoff_lc):
        self.distcoff_lc[...] = distcoff_lc
    
    @property
    def nfr(self):
        """
        Element nfr ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 501
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__nfr(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            nfr = self._arrays[array_handle]
        else:
            nfr = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__nfr)
            self._arrays[array_handle] = nfr
        return nfr
    
    @nfr.setter
    def nfr(self, nfr):
        self.nfr[...] = nfr
    
    @property
    def lang(self):
        """
        Element lang ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 502
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__lang(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            lang = self._arrays[array_handle]
        else:
            lang = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__lang)
            self._arrays[array_handle] = lang
        return lang
    
    @lang.setter
    def lang(self, lang):
        self.lang[...] = lang
    
    @property
    def pdm(self):
        """
        Element pdm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 504
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__pdm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            pdm = self._arrays[array_handle]
        else:
            pdm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__pdm)
            self._arrays[array_handle] = pdm
        return pdm
    
    @pdm.setter
    def pdm(self, pdm):
        self.pdm[...] = pdm
    
    @property
    def dhac(self):
        """
        Element dhac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 505
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhac = self._arrays[array_handle]
        else:
            dhac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhac)
            self._arrays[array_handle] = dhac
        return dhac
    
    @dhac.setter
    def dhac(self, dhac):
        self.dhac[...] = dhac
    
    @property
    def dhbc(self):
        """
        Element dhbc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 506
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhbc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhbc = self._arrays[array_handle]
        else:
            dhbc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhbc)
            self._arrays[array_handle] = dhbc
        return dhbc
    
    @dhbc.setter
    def dhbc(self, dhbc):
        self.dhbc[...] = dhbc
    
    @property
    def cxc(self):
        """
        Element cxc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 507
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cxc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cxc = self._arrays[array_handle]
        else:
            cxc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cxc)
            self._arrays[array_handle] = cxc
        return cxc
    
    @cxc.setter
    def cxc(self, cxc):
        self.cxc[...] = cxc
    
    @property
    def cxmax(self):
        """
        Element cxmax ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 508
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cxmax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cxmax = self._arrays[array_handle]
        else:
            cxmax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cxmax)
            self._arrays[array_handle] = cxmax
        return cxmax
    
    @cxmax.setter
    def cxmax(self, cxmax):
        self.cxmax[...] = cxmax
    
    @property
    def chargex(self):
        """
        Element chargex ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 509
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chargex(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chargex = self._arrays[array_handle]
        else:
            chargex = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chargex)
            self._arrays[array_handle] = chargex
        return chargex
    
    @chargex.setter
    def chargex(self, chargex):
        self.chargex[...] = chargex
    
    @property
    def eqx(self):
        """
        Element eqx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 510
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqx = self._arrays[array_handle]
        else:
            eqx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqx)
            self._arrays[array_handle] = eqx
        return eqx
    
    @eqx.setter
    def eqx(self, eqx):
        self.eqx[...] = eqx
    
    @property
    def eqxs(self):
        """
        Element eqxs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 511
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqxs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqxs = self._arrays[array_handle]
        else:
            eqxs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqxs)
            self._arrays[array_handle] = eqxs
        return eqxs
    
    @eqxs.setter
    def eqxs(self, eqxs):
        self.eqxs[...] = eqxs
    
    @property
    def gfwx(self):
        """
        Element gfwx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 512
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwx = self._arrays[array_handle]
        else:
            gfwx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwx)
            self._arrays[array_handle] = gfwx
        return gfwx
    
    @gfwx.setter
    def gfwx(self, gfwx):
        self.gfwx[...] = gfwx
    
    @property
    def dhcx(self):
        """
        Element dhcx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 513
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcx = self._arrays[array_handle]
        else:
            dhcx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcx)
            self._arrays[array_handle] = dhcx
        return dhcx
    
    @dhcx.setter
    def dhcx(self, dhcx):
        self.dhcx[...] = dhcx
    
    @property
    def dhax(self):
        """
        Element dhax ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 514
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhax = self._arrays[array_handle]
        else:
            dhax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhax)
            self._arrays[array_handle] = dhax
        return dhax
    
    @dhax.setter
    def dhax(self, dhax):
        self.dhax[...] = dhax
    
    @property
    def dhbx(self):
        """
        Element dhbx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 515
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhbx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhbx = self._arrays[array_handle]
        else:
            dhbx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhbx)
            self._arrays[array_handle] = dhbx
        return dhbx
    
    @dhbx.setter
    def dhbx(self, dhbx):
        self.dhbx[...] = dhbx
    
    @property
    def xnux(self):
        """
        Element xnux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 516
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnux = self._arrays[array_handle]
        else:
            xnux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnux)
            self._arrays[array_handle] = xnux
        return xnux
    
    @xnux.setter
    def xnux(self, xnux):
        self.xnux[...] = xnux
    
    @property
    def sion1(self):
        """
        Element sion1 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 518
        
        """
        return _min3p.f90wrap_chem__get__sion1()
    
    @sion1.setter
    def sion1(self, sion1):
        _min3p.f90wrap_chem__set__sion1(sion1)
    
    @property
    def phguess(self):
        """
        Element phguess ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 519
        
        """
        return _min3p.f90wrap_chem__get__phguess()
    
    @phguess.setter
    def phguess(self, phguess):
        _min3p.f90wrap_chem__set__phguess(phguess)
    
    @property
    def iax(self):
        """
        Element iax ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 521
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iax = self._arrays[array_handle]
        else:
            iax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iax)
            self._arrays[array_handle] = iax
        return iax
    
    @iax.setter
    def iax(self, iax):
        self.iax[...] = iax
    
    @property
    def jax(self):
        """
        Element jax ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 522
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jax = self._arrays[array_handle]
        else:
            jax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jax)
            self._arrays[array_handle] = jax
        return jax
    
    @jax.setter
    def jax(self, jax):
        self.jax[...] = jax
    
    @property
    def l_namec(self):
        """
        Element l_namec ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 523
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namec(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namec = self._arrays[array_handle]
        else:
            l_namec = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namec)
            self._arrays[array_handle] = l_namec
        return l_namec
    
    @l_namec.setter
    def l_namec(self, l_namec):
        self.l_namec[...] = l_namec
    
    @property
    def l_namex(self):
        """
        Element l_namex ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 524
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namex(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namex = self._arrays[array_handle]
        else:
            l_namex = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namex)
            self._arrays[array_handle] = l_namex
        return l_namex
    
    @l_namex.setter
    def l_namex(self, l_namex):
        self.l_namex[...] = l_namex
    
    @property
    def cequil_kin(self):
        """
        Element cequil_kin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 708
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cequil_kin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cequil_kin = self._arrays[array_handle]
        else:
            cequil_kin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cequil_kin)
            self._arrays[array_handle] = cequil_kin
        return cequil_kin
    
    @cequil_kin.setter
    def cequil_kin(self, cequil_kin):
        self.cequil_kin[...] = cequil_kin
    
    @property
    def clang_kin(self):
        """
        Element clang_kin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 709
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__clang_kin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            clang_kin = self._arrays[array_handle]
        else:
            clang_kin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__clang_kin)
            self._arrays[array_handle] = clang_kin
        return clang_kin
    
    @clang_kin.setter
    def clang_kin(self, clang_kin):
        self.clang_kin[...] = clang_kin
    
    @property
    def smax_kin(self):
        """
        Element smax_kin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 710
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__smax_kin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            smax_kin = self._arrays[array_handle]
        else:
            smax_kin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__smax_kin)
            self._arrays[array_handle] = smax_kin
        return smax_kin
    
    @smax_kin.setter
    def smax_kin(self, smax_kin):
        self.smax_kin[...] = smax_kin
    
    @property
    def cfreund_kin(self):
        """
        Element cfreund_kin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 711
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cfreund_kin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cfreund_kin = self._arrays[array_handle]
        else:
            cfreund_kin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cfreund_kin)
            self._arrays[array_handle] = cfreund_kin
        return cfreund_kin
    
    @cfreund_kin.setter
    def cfreund_kin(self, cfreund_kin):
        self.cfreund_kin[...] = cfreund_kin
    
    @property
    def exponfreund_kin(self):
        """
        Element exponfreund_kin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 712
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__exponfreund_kin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            exponfreund_kin = self._arrays[array_handle]
        else:
            exponfreund_kin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__exponfreund_kin)
            self._arrays[array_handle] = exponfreund_kin
        return exponfreund_kin
    
    @exponfreund_kin.setter
    def exponfreund_kin(self, exponfreund_kin):
        self.exponfreund_kin[...] = exponfreund_kin
    
    @property
    def eqaq(self):
        """
        Element eqaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 713
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqaq = self._arrays[array_handle]
        else:
            eqaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqaq)
            self._arrays[array_handle] = eqaq
        return eqaq
    
    @eqaq.setter
    def eqaq(self, eqaq):
        self.eqaq[...] = eqaq
    
    @property
    def eqaqs(self):
        """
        Element eqaqs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 714
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqaqs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqaqs = self._arrays[array_handle]
        else:
            eqaqs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqaqs)
            self._arrays[array_handle] = eqaqs
        return eqaqs
    
    @eqaqs.setter
    def eqaqs(self, eqaqs):
        self.eqaqs[...] = eqaqs
    
    @property
    def dgaq(self):
        """
        Element dgaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 715
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dgaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dgaq = self._arrays[array_handle]
        else:
            dgaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dgaq)
            self._arrays[array_handle] = dgaq
        return dgaq
    
    @dgaq.setter
    def dgaq(self, dgaq):
        self.dgaq[...] = dgaq
    
    @property
    def dhaq(self):
        """
        Element dhaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 716
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhaq = self._arrays[array_handle]
        else:
            dhaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhaq)
            self._arrays[array_handle] = dhaq
        return dhaq
    
    @dhaq.setter
    def dhaq(self, dhaq):
        self.dhaq[...] = dhaq
    
    @property
    def dtotaq(self):
        """
        Element dtotaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 717
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotaq = self._arrays[array_handle]
        else:
            dtotaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotaq)
            self._arrays[array_handle] = dtotaq
        return dtotaq
    
    @dtotaq.setter
    def dtotaq(self, dtotaq):
        self.dtotaq[...] = dtotaq
    
    @property
    def faqhc(self):
        """
        Element faqhc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 718
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqhc = self._arrays[array_handle]
        else:
            faqhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqhc)
            self._arrays[array_handle] = faqhc
        return faqhc
    
    @faqhc.setter
    def faqhc(self, faqhc):
        self.faqhc[...] = faqhc
    
    @property
    def faqht(self):
        """
        Element faqht ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 719
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqht(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqht = self._arrays[array_handle]
        else:
            faqht = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqht)
            self._arrays[array_handle] = faqht
        return faqht
    
    @faqht.setter
    def faqht(self, faqht):
        self.faqht[...] = faqht
    
    @property
    def faqhm(self):
        """
        Element faqhm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 720
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqhm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqhm = self._arrays[array_handle]
        else:
            faqhm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqhm)
            self._arrays[array_handle] = faqhm
        return faqhm
    
    @faqhm.setter
    def faqhm(self, faqhm):
        self.faqhm[...] = faqhm
    
    @property
    def faqi(self):
        """
        Element faqi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 721
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqi = self._arrays[array_handle]
        else:
            faqi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqi)
            self._arrays[array_handle] = faqi
        return faqi
    
    @faqi.setter
    def faqi(self, faqi):
        self.faqi[...] = faqi
    
    @property
    def faqic(self):
        """
        Element faqic ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 722
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqic = self._arrays[array_handle]
        else:
            faqic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqic)
            self._arrays[array_handle] = faqic
        return faqic
    
    @faqic.setter
    def faqic(self, faqic):
        self.faqic[...] = faqic
    
    @property
    def faqit(self):
        """
        Element faqit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 723
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqit = self._arrays[array_handle]
        else:
            faqit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqit)
            self._arrays[array_handle] = faqit
        return faqit
    
    @faqit.setter
    def faqit(self, faqit):
        self.faqit[...] = faqit
    
    @property
    def faqim(self):
        """
        Element faqim ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 724
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__faqim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            faqim = self._arrays[array_handle]
        else:
            faqim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__faqim)
            self._arrays[array_handle] = faqim
        return faqim
    
    @faqim.setter
    def faqim(self, faqim):
        self.faqim[...] = faqim
    
    @property
    def ordaqic(self):
        """
        Element ordaqic ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 725
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqic = self._arrays[array_handle]
        else:
            ordaqic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqic)
            self._arrays[array_handle] = ordaqic
        return ordaqic
    
    @ordaqic.setter
    def ordaqic(self, ordaqic):
        self.ordaqic[...] = ordaqic
    
    @property
    def ordaqit(self):
        """
        Element ordaqit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 726
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqit = self._arrays[array_handle]
        else:
            ordaqit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqit)
            self._arrays[array_handle] = ordaqit
        return ordaqit
    
    @ordaqit.setter
    def ordaqit(self, ordaqit):
        self.ordaqit[...] = ordaqit
    
    @property
    def ordaqim(self):
        """
        Element ordaqim ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 727
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqim = self._arrays[array_handle]
        else:
            ordaqim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqim)
            self._arrays[array_handle] = ordaqim
        return ordaqim
    
    @ordaqim.setter
    def ordaqim(self, ordaqim):
        self.ordaqim[...] = ordaqim
    
    @property
    def ordaqhc(self):
        """
        Element ordaqhc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 728
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqhc = self._arrays[array_handle]
        else:
            ordaqhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqhc)
            self._arrays[array_handle] = ordaqhc
        return ordaqhc
    
    @ordaqhc.setter
    def ordaqhc(self, ordaqhc):
        self.ordaqhc[...] = ordaqhc
    
    @property
    def ordaqht(self):
        """
        Element ordaqht ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 729
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqht(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqht = self._arrays[array_handle]
        else:
            ordaqht = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqht)
            self._arrays[array_handle] = ordaqht
        return ordaqht
    
    @ordaqht.setter
    def ordaqht(self, ordaqht):
        self.ordaqht[...] = ordaqht
    
    @property
    def ordaqhm(self):
        """
        Element ordaqhm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 730
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqhm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqhm = self._arrays[array_handle]
        else:
            ordaqhm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqhm)
            self._arrays[array_handle] = ordaqhm
        return ordaqhm
    
    @ordaqhm.setter
    def ordaqhm(self, ordaqhm):
        self.ordaqhm[...] = ordaqhm
    
    @property
    def ordaqt(self):
        """
        Element ordaqt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 731
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqt = self._arrays[array_handle]
        else:
            ordaqt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqt)
            self._arrays[array_handle] = ordaqt
        return ordaqt
    
    @ordaqt.setter
    def ordaqt(self, ordaqt):
        self.ordaqt[...] = ordaqt
    
    @property
    def ordaqc(self):
        """
        Element ordaqc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 732
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqc = self._arrays[array_handle]
        else:
            ordaqc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqc)
            self._arrays[array_handle] = ordaqc
        return ordaqc
    
    @ordaqc.setter
    def ordaqc(self, ordaqc):
        self.ordaqc[...] = ordaqc
    
    @property
    def ordaqx(self):
        """
        Element ordaqx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 733
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqx = self._arrays[array_handle]
        else:
            ordaqx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqx)
            self._arrays[array_handle] = ordaqx
        return ordaqx
    
    @ordaqx.setter
    def ordaqx(self, ordaqx):
        self.ordaqx[...] = ordaqx
    
    @property
    def ordaqm(self):
        """
        Element ordaqm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 734
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordaqm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordaqm = self._arrays[array_handle]
        else:
            ordaqm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordaqm)
            self._arrays[array_handle] = ordaqm
        return ordaqm
    
    @ordaqm.setter
    def ordaqm(self, ordaqm):
        self.ordaqm[...] = ordaqm
    
    @property
    def rateaq(self):
        """
        Element rateaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 735
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rateaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateaq = self._arrays[array_handle]
        else:
            rateaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rateaq)
            self._arrays[array_handle] = rateaq
        return rateaq
    
    @rateaq.setter
    def rateaq(self, rateaq):
        self.rateaq[...] = rateaq
    
    @property
    def ratecaq(self):
        """
        Element ratecaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 736
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ratecaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratecaq = self._arrays[array_handle]
        else:
            ratecaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ratecaq)
            self._arrays[array_handle] = ratecaq
        return ratecaq
    
    @ratecaq.setter
    def ratecaq(self, ratecaq):
        self.ratecaq[...] = ratecaq
    
    @property
    def ratecaqs(self):
        """
        Element ratecaqs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 737
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ratecaqs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratecaqs = self._arrays[array_handle]
        else:
            ratecaqs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ratecaqs)
            self._arrays[array_handle] = ratecaqs
        return ratecaqs
    
    @ratecaqs.setter
    def ratecaqs(self, ratecaqs):
        self.ratecaqs[...] = ratecaqs
    
    @property
    def sataq(self):
        """
        Element sataq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 738
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__sataq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sataq = self._arrays[array_handle]
        else:
            sataq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__sataq)
            self._arrays[array_handle] = sataq
        return sataq
    
    @sataq.setter
    def sataq(self, sataq):
        self.sataq[...] = sataq
    
    @property
    def scalfac_aq(self):
        """
        Element scalfac_aq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 739
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__scalfac_aq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            scalfac_aq = self._arrays[array_handle]
        else:
            scalfac_aq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__scalfac_aq)
            self._arrays[array_handle] = scalfac_aq
        return scalfac_aq
    
    @scalfac_aq.setter
    def scalfac_aq(self, scalfac_aq):
        self.scalfac_aq[...] = scalfac_aq
    
    @property
    def totaq(self):
        """
        Element totaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 740
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totaq = self._arrays[array_handle]
        else:
            totaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totaq)
            self._arrays[array_handle] = totaq
        return totaq
    
    @totaq.setter
    def totaq(self, totaq):
        self.totaq[...] = totaq
    
    @property
    def xnuaq(self):
        """
        Element xnuaq ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 741
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnuaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnuaq = self._arrays[array_handle]
        else:
            xnuaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnuaq)
            self._arrays[array_handle] = xnuaq
        return xnuaq
    
    @xnuaq.setter
    def xnuaq(self, xnuaq):
        self.xnuaq[...] = xnuaq
    
    @property
    def iaaq(self):
        """
        Element iaaq ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 743
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaq = self._arrays[array_handle]
        else:
            iaaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaq)
            self._arrays[array_handle] = iaaq
        return iaaq
    
    @iaaq.setter
    def iaaq(self, iaaq):
        self.iaaq[...] = iaaq
    
    @property
    def iaaqi(self):
        """
        Element iaaqi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 744
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqi = self._arrays[array_handle]
        else:
            iaaqi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqi)
            self._arrays[array_handle] = iaaqi
        return iaaqi
    
    @iaaqi.setter
    def iaaqi(self, iaaqi):
        self.iaaqi[...] = iaaqi
    
    @property
    def iaaqic(self):
        """
        Element iaaqic ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 745
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqic = self._arrays[array_handle]
        else:
            iaaqic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqic)
            self._arrays[array_handle] = iaaqic
        return iaaqic
    
    @iaaqic.setter
    def iaaqic(self, iaaqic):
        self.iaaqic[...] = iaaqic
    
    @property
    def iaaqit(self):
        """
        Element iaaqit ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 746
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqit = self._arrays[array_handle]
        else:
            iaaqit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqit)
            self._arrays[array_handle] = iaaqit
        return iaaqit
    
    @iaaqit.setter
    def iaaqit(self, iaaqit):
        self.iaaqit[...] = iaaqit
    
    @property
    def iaaqim(self):
        """
        Element iaaqim ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 747
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqim = self._arrays[array_handle]
        else:
            iaaqim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqim)
            self._arrays[array_handle] = iaaqim
        return iaaqim
    
    @iaaqim.setter
    def iaaqim(self, iaaqim):
        self.iaaqim[...] = iaaqim
    
    @property
    def iaaqhc(self):
        """
        Element iaaqhc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 748
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqhc = self._arrays[array_handle]
        else:
            iaaqhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqhc)
            self._arrays[array_handle] = iaaqhc
        return iaaqhc
    
    @iaaqhc.setter
    def iaaqhc(self, iaaqhc):
        self.iaaqhc[...] = iaaqhc
    
    @property
    def iaaqht(self):
        """
        Element iaaqht ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 749
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqht(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqht = self._arrays[array_handle]
        else:
            iaaqht = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqht)
            self._arrays[array_handle] = iaaqht
        return iaaqht
    
    @iaaqht.setter
    def iaaqht(self, iaaqht):
        self.iaaqht[...] = iaaqht
    
    @property
    def iaaqhm(self):
        """
        Element iaaqhm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 750
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqhm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqhm = self._arrays[array_handle]
        else:
            iaaqhm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqhm)
            self._arrays[array_handle] = iaaqhm
        return iaaqhm
    
    @iaaqhm.setter
    def iaaqhm(self, iaaqhm):
        self.iaaqhm[...] = iaaqhm
    
    @property
    def iaaqt(self):
        """
        Element iaaqt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 751
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqt = self._arrays[array_handle]
        else:
            iaaqt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqt)
            self._arrays[array_handle] = iaaqt
        return iaaqt
    
    @iaaqt.setter
    def iaaqt(self, iaaqt):
        self.iaaqt[...] = iaaqt
    
    @property
    def iaequil(self):
        """
        Element iaequil ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 752
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaequil(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaequil = self._arrays[array_handle]
        else:
            iaequil = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaequil)
            self._arrays[array_handle] = iaequil
        return iaequil
    
    @iaequil.setter
    def iaequil(self, iaequil):
        self.iaequil[...] = iaequil
    
    @property
    def iaaqc(self):
        """
        Element iaaqc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 753
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqc = self._arrays[array_handle]
        else:
            iaaqc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqc)
            self._arrays[array_handle] = iaaqc
        return iaaqc
    
    @iaaqc.setter
    def iaaqc(self, iaaqc):
        self.iaaqc[...] = iaaqc
    
    @property
    def iaaqx(self):
        """
        Element iaaqx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 754
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqx = self._arrays[array_handle]
        else:
            iaaqx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqx)
            self._arrays[array_handle] = iaaqx
        return iaaqx
    
    @iaaqx.setter
    def iaaqx(self, iaaqx):
        self.iaaqx[...] = iaaqx
    
    @property
    def iaaqm(self):
        """
        Element iaaqm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 755
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaaqm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaaqm = self._arrays[array_handle]
        else:
            iaaqm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaaqm)
            self._arrays[array_handle] = iaaqm
        return iaaqm
    
    @iaaqm.setter
    def iaaqm(self, iaaqm):
        self.iaaqm[...] = iaaqm
    
    @property
    def jaaq(self):
        """
        Element jaaq ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 756
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaq = self._arrays[array_handle]
        else:
            jaaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaq)
            self._arrays[array_handle] = jaaq
        return jaaq
    
    @jaaq.setter
    def jaaq(self, jaaq):
        self.jaaq[...] = jaaq
    
    @property
    def jaaqt(self):
        """
        Element jaaqt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 757
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqt = self._arrays[array_handle]
        else:
            jaaqt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqt)
            self._arrays[array_handle] = jaaqt
        return jaaqt
    
    @jaaqt.setter
    def jaaqt(self, jaaqt):
        self.jaaqt[...] = jaaqt
    
    @property
    def jaequil(self):
        """
        Element jaequil ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 758
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaequil(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaequil = self._arrays[array_handle]
        else:
            jaequil = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaequil)
            self._arrays[array_handle] = jaequil
        return jaequil
    
    @jaequil.setter
    def jaequil(self, jaequil):
        self.jaequil[...] = jaequil
    
    @property
    def jaaqc(self):
        """
        Element jaaqc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 759
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqc = self._arrays[array_handle]
        else:
            jaaqc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqc)
            self._arrays[array_handle] = jaaqc
        return jaaqc
    
    @jaaqc.setter
    def jaaqc(self, jaaqc):
        self.jaaqc[...] = jaaqc
    
    @property
    def jaaqx(self):
        """
        Element jaaqx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 760
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqx = self._arrays[array_handle]
        else:
            jaaqx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqx)
            self._arrays[array_handle] = jaaqx
        return jaaqx
    
    @jaaqx.setter
    def jaaqx(self, jaaqx):
        self.jaaqx[...] = jaaqx
    
    @property
    def jaaqm(self):
        """
        Element jaaqm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 761
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqm = self._arrays[array_handle]
        else:
            jaaqm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqm)
            self._arrays[array_handle] = jaaqm
        return jaaqm
    
    @jaaqm.setter
    def jaaqm(self, jaaqm):
        self.jaaqm[...] = jaaqm
    
    @property
    def jaaqhc(self):
        """
        Element jaaqhc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 762
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqhc = self._arrays[array_handle]
        else:
            jaaqhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqhc)
            self._arrays[array_handle] = jaaqhc
        return jaaqhc
    
    @jaaqhc.setter
    def jaaqhc(self, jaaqhc):
        self.jaaqhc[...] = jaaqhc
    
    @property
    def jaaqht(self):
        """
        Element jaaqht ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 763
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqht(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqht = self._arrays[array_handle]
        else:
            jaaqht = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqht)
            self._arrays[array_handle] = jaaqht
        return jaaqht
    
    @jaaqht.setter
    def jaaqht(self, jaaqht):
        self.jaaqht[...] = jaaqht
    
    @property
    def jaaqhm(self):
        """
        Element jaaqhm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 764
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqhm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqhm = self._arrays[array_handle]
        else:
            jaaqhm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqhm)
            self._arrays[array_handle] = jaaqhm
        return jaaqhm
    
    @jaaqhm.setter
    def jaaqhm(self, jaaqhm):
        self.jaaqhm[...] = jaaqhm
    
    @property
    def jaaqi(self):
        """
        Element jaaqi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 765
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqi = self._arrays[array_handle]
        else:
            jaaqi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqi)
            self._arrays[array_handle] = jaaqi
        return jaaqi
    
    @jaaqi.setter
    def jaaqi(self, jaaqi):
        self.jaaqi[...] = jaaqi
    
    @property
    def jaaqic(self):
        """
        Element jaaqic ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 766
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqic = self._arrays[array_handle]
        else:
            jaaqic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqic)
            self._arrays[array_handle] = jaaqic
        return jaaqic
    
    @jaaqic.setter
    def jaaqic(self, jaaqic):
        self.jaaqic[...] = jaaqic
    
    @property
    def jaaqit(self):
        """
        Element jaaqit ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 767
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqit = self._arrays[array_handle]
        else:
            jaaqit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqit)
            self._arrays[array_handle] = jaaqit
        return jaaqit
    
    @jaaqit.setter
    def jaaqit(self, jaaqit):
        self.jaaqit[...] = jaaqit
    
    @property
    def jaaqim(self):
        """
        Element jaaqim ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 768
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaaqim(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaaqim = self._arrays[array_handle]
        else:
            jaaqim = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaaqim)
            self._arrays[array_handle] = jaaqim
        return jaaqim
    
    @jaaqim.setter
    def jaaqim(self, jaaqim):
        self.jaaqim[...] = jaaqim
    
    @property
    def l_nameaq(self):
        """
        Element l_nameaq ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 769
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_nameaq(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_nameaq = self._arrays[array_handle]
        else:
            l_nameaq = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_nameaq)
            self._arrays[array_handle] = l_nameaq
        return l_nameaq
    
    @l_nameaq.setter
    def l_nameaq(self, l_nameaq):
        self.l_nameaq[...] = l_nameaq
    
    @property
    def bcatfac(self):
        """
        Element bcatfac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 905
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__bcatfac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bcatfac = self._arrays[array_handle]
        else:
            bcatfac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__bcatfac)
            self._arrays[array_handle] = bcatfac
        return bcatfac
    
    @bcatfac.setter
    def bcatfac(self, bcatfac):
        self.bcatfac[...] = bcatfac
    
    @property
    def dhcr(self):
        """
        Element dhcr ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 906
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcr(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcr = self._arrays[array_handle]
        else:
            dhcr = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcr)
            self._arrays[array_handle] = dhcr
        return dhcr
    
    @dhcr.setter
    def dhcr(self, dhcr):
        self.dhcr[...] = dhcr
    
    @property
    def dtotor(self):
        """
        Element dtotor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 907
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotor = self._arrays[array_handle]
        else:
            dtotor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotor)
            self._arrays[array_handle] = dtotor
        return dtotor
    
    @dtotor.setter
    def dtotor(self, dtotor):
        self.dtotor[...] = dtotor
    
    @property
    def eqr(self):
        """
        Element eqr ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 908
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqr(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqr = self._arrays[array_handle]
        else:
            eqr = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqr)
            self._arrays[array_handle] = eqr
        return eqr
    
    @eqr.setter
    def eqr(self, eqr):
        self.eqr[...] = eqr
    
    @property
    def eqrs(self):
        """
        Element eqrs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 909
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqrs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqrs = self._arrays[array_handle]
        else:
            eqrs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqrs)
            self._arrays[array_handle] = eqrs
        return eqrs
    
    @eqrs.setter
    def eqrs(self, eqrs):
        self.eqrs[...] = eqrs
    
    @property
    def chomc(self):
        """
        Element chomc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 910
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chomc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chomc = self._arrays[array_handle]
        else:
            chomc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chomc)
            self._arrays[array_handle] = chomc
        return chomc
    
    @chomc.setter
    def chomc(self, chomc):
        self.chomc[...] = chomc
    
    @property
    def chomt(self):
        """
        Element chomt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 911
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chomt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chomt = self._arrays[array_handle]
        else:
            chomt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chomt)
            self._arrays[array_handle] = chomt
        return chomt
    
    @chomt.setter
    def chomt(self, chomt):
        self.chomt[...] = chomt
    
    @property
    def chomx(self):
        """
        Element chomx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 912
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chomx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chomx = self._arrays[array_handle]
        else:
            chomx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chomx)
            self._arrays[array_handle] = chomx
        return chomx
    
    @chomx.setter
    def chomx(self, chomx):
        self.chomx[...] = chomx
    
    @property
    def ordorc(self):
        """
        Element ordorc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 913
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordorc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordorc = self._arrays[array_handle]
        else:
            ordorc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordorc)
            self._arrays[array_handle] = ordorc
        return ordorc
    
    @ordorc.setter
    def ordorc(self, ordorc):
        self.ordorc[...] = ordorc
    
    @property
    def ordort(self):
        """
        Element ordort ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 914
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordort(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordort = self._arrays[array_handle]
        else:
            ordort = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordort)
            self._arrays[array_handle] = ordort
        return ordort
    
    @ordort.setter
    def ordort(self, ordort):
        self.ordort[...] = ordort
    
    @property
    def ordorx(self):
        """
        Element ordorx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 915
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordorx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordorx = self._arrays[array_handle]
        else:
            ordorx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordorx)
            self._arrays[array_handle] = ordorx
        return ordorx
    
    @ordorx.setter
    def ordorx(self, ordorx):
        self.ordorx[...] = ordorx
    
    @property
    def rateor(self):
        """
        Element rateor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 916
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rateor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateor = self._arrays[array_handle]
        else:
            rateor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rateor)
            self._arrays[array_handle] = rateor
        return rateor
    
    @rateor.setter
    def rateor(self, rateor):
        self.rateor[...] = rateor
    
    @property
    def rateox(self):
        """
        Element rateox ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 917
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rateox(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateox = self._arrays[array_handle]
        else:
            rateox = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rateox)
            self._arrays[array_handle] = rateox
        return rateox
    
    @rateox.setter
    def rateox(self, rateox):
        self.rateox[...] = rateox
    
    @property
    def totor(self):
        """
        Element totor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 918
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totor = self._arrays[array_handle]
        else:
            totor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totor)
            self._arrays[array_handle] = totor
        return totor
    
    @totor.setter
    def totor(self, totor):
        self.totor[...] = totor
    
    @property
    def xnur(self):
        """
        Element xnur ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 919
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnur(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnur = self._arrays[array_handle]
        else:
            xnur = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnur)
            self._arrays[array_handle] = xnur
        return xnur
    
    @xnur.setter
    def xnur(self, xnur):
        self.xnur[...] = xnur
    
    @property
    def iaor(self):
        """
        Element iaor ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 921
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaor = self._arrays[array_handle]
        else:
            iaor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaor)
            self._arrays[array_handle] = iaor
        return iaor
    
    @iaor.setter
    def iaor(self, iaor):
        self.iaor[...] = iaor
    
    @property
    def iaorc(self):
        """
        Element iaorc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 922
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaorc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaorc = self._arrays[array_handle]
        else:
            iaorc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaorc)
            self._arrays[array_handle] = iaorc
        return iaorc
    
    @iaorc.setter
    def iaorc(self, iaorc):
        self.iaorc[...] = iaorc
    
    @property
    def iaort(self):
        """
        Element iaort ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 923
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaort(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaort = self._arrays[array_handle]
        else:
            iaort = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaort)
            self._arrays[array_handle] = iaort
        return iaort
    
    @iaort.setter
    def iaort(self, iaort):
        self.iaort[...] = iaort
    
    @property
    def iaorx(self):
        """
        Element iaorx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 924
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaorx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaorx = self._arrays[array_handle]
        else:
            iaorx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaorx)
            self._arrays[array_handle] = iaorx
        return iaorx
    
    @iaorx.setter
    def iaorx(self, iaorx):
        self.iaorx[...] = iaorx
    
    @property
    def iarc(self):
        """
        Element iarc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 925
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iarc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iarc = self._arrays[array_handle]
        else:
            iarc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iarc)
            self._arrays[array_handle] = iarc
        return iarc
    
    @iarc.setter
    def iarc(self, iarc):
        self.iarc[...] = iarc
    
    @property
    def iars(self):
        """
        Element iars ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 926
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iars(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iars = self._arrays[array_handle]
        else:
            iars = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iars)
            self._arrays[array_handle] = iars
        return iars
    
    @iars.setter
    def iars(self, iars):
        self.iars[...] = iars
    
    @property
    def jaorc(self):
        """
        Element jaorc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 927
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaorc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaorc = self._arrays[array_handle]
        else:
            jaorc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaorc)
            self._arrays[array_handle] = jaorc
        return jaorc
    
    @jaorc.setter
    def jaorc(self, jaorc):
        self.jaorc[...] = jaorc
    
    @property
    def jaort(self):
        """
        Element jaort ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 928
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaort(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaort = self._arrays[array_handle]
        else:
            jaort = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaort)
            self._arrays[array_handle] = jaort
        return jaort
    
    @jaort.setter
    def jaort(self, jaort):
        self.jaort[...] = jaort
    
    @property
    def jaorx(self):
        """
        Element jaorx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 929
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaorx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaorx = self._arrays[array_handle]
        else:
            jaorx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaorx)
            self._arrays[array_handle] = jaorx
        return jaorx
    
    @jaorx.setter
    def jaorx(self, jaorx):
        self.jaorx[...] = jaorx
    
    @property
    def jarc(self):
        """
        Element jarc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 930
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jarc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jarc = self._arrays[array_handle]
        else:
            jarc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jarc)
            self._arrays[array_handle] = jarc
        return jarc
    
    @jarc.setter
    def jarc(self, jarc):
        self.jarc[...] = jarc
    
    @property
    def l_namer(self):
        """
        Element l_namer ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 931
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namer(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namer = self._arrays[array_handle]
        else:
            l_namer = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namer)
            self._arrays[array_handle] = l_namer
        return l_namer
    
    @l_namer.setter
    def l_namer(self, l_namer):
        self.l_namer[...] = l_namer
    
    @property
    def l_namerp(self):
        """
        Element l_namerp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 932
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namerp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namerp = self._arrays[array_handle]
        else:
            l_namerp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namerp)
            self._arrays[array_handle] = l_namerp
        return l_namerp
    
    @l_namerp.setter
    def l_namerp(self, l_namerp):
        self.l_namerp[...] = l_namerp
    
    @property
    def l_namers(self):
        """
        Element l_namers ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 933
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namers(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namers = self._arrays[array_handle]
        else:
            l_namers = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namers)
            self._arrays[array_handle] = l_namers
        return l_namers
    
    @l_namers.setter
    def l_namers(self, l_namers):
        self.l_namers[...] = l_namers
    
    @property
    def ncrc(self):
        """
        Element ncrc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 935
        
        """
        return _min3p.f90wrap_chem__get__ncrc()
    
    @ncrc.setter
    def ncrc(self, ncrc):
        _min3p.f90wrap_chem__set__ncrc(ncrc)
    
    @property
    def nor(self):
        """
        Element nor ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 936
        
        """
        return _min3p.f90wrap_chem__get__nor()
    
    @nor.setter
    def nor(self, nor):
        _min3p.f90wrap_chem__set__nor(nor)
    
    @property
    def norc(self):
        """
        Element norc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 937
        
        """
        return _min3p.f90wrap_chem__get__norc()
    
    @norc.setter
    def norc(self, norc):
        _min3p.f90wrap_chem__set__norc(norc)
    
    @property
    def nort(self):
        """
        Element nort ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 938
        
        """
        return _min3p.f90wrap_chem__get__nort()
    
    @nort.setter
    def nort(self, nort):
        _min3p.f90wrap_chem__set__nort(nort)
    
    @property
    def norx(self):
        """
        Element norx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 939
        
        """
        return _min3p.f90wrap_chem__get__norx()
    
    @norx.setter
    def norx(self, norx):
        _min3p.f90wrap_chem__set__norx(norx)
    
    @property
    def redox_equil(self):
        """
        Element redox_equil ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 941
        
        """
        return _min3p.f90wrap_chem__get__redox_equil()
    
    @redox_equil.setter
    def redox_equil(self, redox_equil):
        _min3p.f90wrap_chem__set__redox_equil(redox_equil)
    
    @property
    def cgc(self):
        """
        Element cgc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1000
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cgc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cgc = self._arrays[array_handle]
        else:
            cgc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cgc)
            self._arrays[array_handle] = cgc
        return cgc
    
    @cgc.setter
    def cgc(self, cgc):
        self.cgc[...] = cgc
    
    @property
    def rateg(self):
        """
        Element rateg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1001
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rateg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateg = self._arrays[array_handle]
        else:
            rateg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rateg)
            self._arrays[array_handle] = rateg
        return rateg
    
    @rateg.setter
    def rateg(self, rateg):
        self.rateg[...] = rateg
    
    @property
    def totgn(self):
        """
        Element totgn ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1002
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totgn(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgn = self._arrays[array_handle]
        else:
            totgn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totgn)
            self._arrays[array_handle] = totgn
        return totgn
    
    @totgn.setter
    def totgn(self, totgn):
        self.totgn[...] = totgn
    
    @property
    def totgo(self):
        """
        Element totgo ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1003
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totgo(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgo = self._arrays[array_handle]
        else:
            totgo = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totgo)
            self._arrays[array_handle] = totgo
        return totgo
    
    @totgo.setter
    def totgo(self, totgo):
        self.totgo[...] = totgo
    
    @property
    def totrateg(self):
        """
        Element totrateg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1004
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totrateg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totrateg = self._arrays[array_handle]
        else:
            totrateg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totrateg)
            self._arrays[array_handle] = totrateg
        return totrateg
    
    @totrateg.setter
    def totrateg(self, totrateg):
        self.totrateg[...] = totrateg
    
    @property
    def gfwg(self):
        """
        Element gfwg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1005
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwg = self._arrays[array_handle]
        else:
            gfwg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwg)
            self._arrays[array_handle] = gfwg
        return gfwg
    
    @gfwg.setter
    def gfwg(self, gfwg):
        self.gfwg[...] = gfwg
    
    @property
    def eqg(self):
        """
        Element eqg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1006
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqg = self._arrays[array_handle]
        else:
            eqg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqg)
            self._arrays[array_handle] = eqg
        return eqg
    
    @eqg.setter
    def eqg(self, eqg):
        self.eqg[...] = eqg
    
    @property
    def eqgs(self):
        """
        Element eqgs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1007
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqgs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqgs = self._arrays[array_handle]
        else:
            eqgs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqgs)
            self._arrays[array_handle] = eqgs
        return eqgs
    
    @eqgs.setter
    def eqgs(self, eqgs):
        self.eqgs[...] = eqgs
    
    @property
    def dhcg(self):
        """
        Element dhcg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1008
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcg = self._arrays[array_handle]
        else:
            dhcg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcg)
            self._arrays[array_handle] = dhcg
        return dhcg
    
    @dhcg.setter
    def dhcg(self, dhcg):
        self.dhcg[...] = dhcg
    
    @property
    def xnug(self):
        """
        Element xnug ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1009
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnug(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnug = self._arrays[array_handle]
        else:
            xnug = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnug)
            self._arrays[array_handle] = xnug
        return xnug
    
    @xnug.setter
    def xnug(self, xnug):
        self.xnug[...] = xnug
    
    @property
    def degas_rate(self):
        """
        Element degas_rate ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1011
        
        """
        return _min3p.f90wrap_chem__get__degas_rate()
    
    @degas_rate.setter
    def degas_rate(self, degas_rate):
        _min3p.f90wrap_chem__set__degas_rate(degas_rate)
    
    @property
    def iaga(self):
        """
        Element iaga ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1013
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaga(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaga = self._arrays[array_handle]
        else:
            iaga = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaga)
            self._arrays[array_handle] = iaga
        return iaga
    
    @iaga.setter
    def iaga(self, iaga):
        self.iaga[...] = iaga
    
    @property
    def jaga(self):
        """
        Element jaga ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1014
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jaga(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaga = self._arrays[array_handle]
        else:
            jaga = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jaga)
            self._arrays[array_handle] = jaga
        return jaga
    
    @jaga.setter
    def jaga(self, jaga):
        self.jaga[...] = jaga
    
    @property
    def l_nameg(self):
        """
        Element l_nameg ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1015
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_nameg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_nameg = self._arrays[array_handle]
        else:
            l_nameg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_nameg)
            self._arrays[array_handle] = l_nameg
        return l_nameg
    
    @l_nameg.setter
    def l_nameg(self, l_nameg):
        self.l_nameg[...] = l_nameg
    
    @property
    def gas_removal(self):
        """
        Element gas_removal ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1017
        
        """
        return _min3p.f90wrap_chem__get__gas_removal()
    
    @gas_removal.setter
    def gas_removal(self, gas_removal):
        _min3p.f90wrap_chem__set__gas_removal(gas_removal)
    
    @property
    def csb(self):
        """
        Element csb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1118
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__csb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            csb = self._arrays[array_handle]
        else:
            csb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__csb)
            self._arrays[array_handle] = csb
        return csb
    
    @csb.setter
    def csb(self, csb):
        self.csb[...] = csb
    
    @property
    def chargesb(self):
        """
        Element chargesb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1119
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chargesb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chargesb = self._arrays[array_handle]
        else:
            chargesb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chargesb)
            self._arrays[array_handle] = chargesb
        return chargesb
    
    @chargesb.setter
    def chargesb(self, chargesb):
        self.chargesb[...] = chargesb
    
    @property
    def totcsn(self):
        """
        Element totcsn ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1122
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcsn(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcsn = self._arrays[array_handle]
        else:
            totcsn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcsn)
            self._arrays[array_handle] = totcsn
        return totcsn
    
    @totcsn.setter
    def totcsn(self, totcsn):
        self.totcsn[...] = totcsn
    
    @property
    def totcso(self):
        """
        Element totcso ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1123
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcso(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcso = self._arrays[array_handle]
        else:
            totcso = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcso)
            self._arrays[array_handle] = totcso
        return totcso
    
    @totcso.setter
    def totcso(self, totcso):
        self.totcso[...] = totcso
    
    @property
    def gfwsb(self):
        """
        Element gfwsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1124
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwsb = self._arrays[array_handle]
        else:
            gfwsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwsb)
            self._arrays[array_handle] = gfwsb
        return gfwsb
    
    @gfwsb.setter
    def gfwsb(self, gfwsb):
        self.gfwsb[...] = gfwsb
    
    @property
    def eqsb(self):
        """
        Element eqsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1125
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqsb = self._arrays[array_handle]
        else:
            eqsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqsb)
            self._arrays[array_handle] = eqsb
        return eqsb
    
    @eqsb.setter
    def eqsb(self, eqsb):
        self.eqsb[...] = eqsb
    
    @property
    def eqsbs(self):
        """
        Element eqsbs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1126
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqsbs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqsbs = self._arrays[array_handle]
        else:
            eqsbs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqsbs)
            self._arrays[array_handle] = eqsbs
        return eqsbs
    
    @eqsbs.setter
    def eqsbs(self, eqsbs):
        self.eqsbs[...] = eqsbs
    
    @property
    def dhcsb(self):
        """
        Element dhcsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1127
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcsb = self._arrays[array_handle]
        else:
            dhcsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcsb)
            self._arrays[array_handle] = dhcsb
        return dhcsb
    
    @dhcsb.setter
    def dhcsb(self, dhcsb):
        self.dhcsb[...] = dhcsb
    
    @property
    def xnusb(self):
        """
        Element xnusb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1128
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnusb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnusb = self._arrays[array_handle]
        else:
            xnusb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnusb)
            self._arrays[array_handle] = xnusb
        return xnusb
    
    @xnusb.setter
    def xnusb(self, xnusb):
        self.xnusb[...] = xnusb
    
    @property
    def site_area(self):
        """
        Element site_area ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1129
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__site_area(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            site_area = self._arrays[array_handle]
        else:
            site_area = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__site_area)
            self._arrays[array_handle] = site_area
        return site_area
    
    @site_area.setter
    def site_area(self, site_area):
        self.site_area[...] = site_area
    
    @property
    def site_dens(self):
        """
        Element site_dens ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1130
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__site_dens(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            site_dens = self._arrays[array_handle]
        else:
            site_dens = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__site_dens)
            self._arrays[array_handle] = site_dens
        return site_dens
    
    @site_dens.setter
    def site_dens(self, site_dens):
        self.site_dens[...] = site_dens
    
    @property
    def site_mass(self):
        """
        Element site_mass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1131
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__site_mass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            site_mass = self._arrays[array_handle]
        else:
            site_mass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__site_mass)
            self._arrays[array_handle] = site_mass
        return site_mass
    
    @site_mass.setter
    def site_mass(self, site_mass):
        self.site_mass[...] = site_mass
    
    @property
    def dcalcpsi(self):
        """
        Element dcalcpsi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1132
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dcalcpsi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dcalcpsi = self._arrays[array_handle]
        else:
            dcalcpsi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dcalcpsi)
            self._arrays[array_handle] = dcalcpsi
        return dcalcpsi
    
    @dcalcpsi.setter
    def dcalcpsi(self, dcalcpsi):
        self.dcalcpsi[...] = dcalcpsi
    
    @property
    def cap1(self):
        """
        Element cap1 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1133
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cap1(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cap1 = self._arrays[array_handle]
        else:
            cap1 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cap1)
            self._arrays[array_handle] = cap1
        return cap1
    
    @cap1.setter
    def cap1(self, cap1):
        self.cap1[...] = cap1
    
    @property
    def cap2(self):
        """
        Element cap2 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1134
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cap2(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cap2 = self._arrays[array_handle]
        else:
            cap2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cap2)
            self._arrays[array_handle] = cap2
        return cap2
    
    @cap2.setter
    def cap2(self, cap2):
        self.cap2[...] = cap2
    
    @property
    def strionsb(self):
        """
        Element strionsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1135
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__strionsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            strionsb = self._arrays[array_handle]
        else:
            strionsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__strionsb)
            self._arrays[array_handle] = strionsb
        return strionsb
    
    @strionsb.setter
    def strionsb(self, strionsb):
        self.strionsb[...] = strionsb
    
    @property
    def surfacensb(self):
        """
        Element surfacensb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1136
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__surfacensb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            surfacensb = self._arrays[array_handle]
        else:
            surfacensb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__surfacensb)
            self._arrays[array_handle] = surfacensb
        return surfacensb
    
    @surfacensb.setter
    def surfacensb(self, surfacensb):
        self.surfacensb[...] = surfacensb
    
    @property
    def calcpsi(self):
        """
        Element calcpsi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1137
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__calcpsi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            calcpsi = self._arrays[array_handle]
        else:
            calcpsi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__calcpsi)
            self._arrays[array_handle] = calcpsi
        return calcpsi
    
    @calcpsi.setter
    def calcpsi(self, calcpsi):
        self.calcpsi[...] = calcpsi
    
    @property
    def totpsi(self):
        """
        Element totpsi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1138
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totpsi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totpsi = self._arrays[array_handle]
        else:
            totpsi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totpsi)
            self._arrays[array_handle] = totpsi
        return totpsi
    
    @totpsi.setter
    def totpsi(self, totpsi):
        self.totpsi[...] = totpsi
    
    @property
    def dtotpsi(self):
        """
        Element dtotpsi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1139
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotpsi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotpsi = self._arrays[array_handle]
        else:
            dtotpsi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotpsi)
            self._arrays[array_handle] = dtotpsi
        return dtotpsi
    
    @dtotpsi.setter
    def dtotpsi(self, dtotpsi):
        self.dtotpsi[...] = dtotpsi
    
    @property
    def dcnew(self):
        """
        Element dcnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1140
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dcnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dcnew = self._arrays[array_handle]
        else:
            dcnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dcnew)
            self._arrays[array_handle] = dcnew
        return dcnew
    
    @dcnew.setter
    def dcnew(self, dcnew):
        self.dcnew[...] = dcnew
    
    @property
    def cec(self):
        """
        Element cec ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1142
        
        """
        return _min3p.f90wrap_chem__get__cec()
    
    @cec.setter
    def cec(self, cec):
        _min3p.f90wrap_chem__set__cec(cec)
    
    @property
    def rhobulk(self):
        """
        Element rhobulk ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1143
        
        """
        return _min3p.f90wrap_chem__get__rhobulk()
    
    @rhobulk.setter
    def rhobulk(self, rhobulk):
        _min3p.f90wrap_chem__set__rhobulk(rhobulk)
    
    @property
    def iaic(self):
        """
        Element iaic ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1144
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iaic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaic = self._arrays[array_handle]
        else:
            iaic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iaic)
            self._arrays[array_handle] = iaic
        return iaic
    
    @iaic.setter
    def iaic(self, iaic):
        self.iaic[...] = iaic
    
    @property
    def iais(self):
        """
        Element iais ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1145
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iais(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iais = self._arrays[array_handle]
        else:
            iais = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iais)
            self._arrays[array_handle] = iais
        return iais
    
    @iais.setter
    def iais(self, iais):
        self.iais[...] = iais
    
    @property
    def iasb(self):
        """
        Element iasb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1146
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iasb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iasb = self._arrays[array_handle]
        else:
            iasb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iasb)
            self._arrays[array_handle] = iasb
        return iasb
    
    @iasb.setter
    def iasb(self, iasb):
        self.iasb[...] = iasb
    
    @property
    def jasb(self):
        """
        Element jasb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1147
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jasb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jasb = self._arrays[array_handle]
        else:
            jasb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jasb)
            self._arrays[array_handle] = jasb
        return jasb
    
    @jasb.setter
    def jasb(self, jasb):
        self.jasb[...] = jasb
    
    @property
    def l_namesb(self):
        """
        Element l_namesb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1148
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namesb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namesb = self._arrays[array_handle]
        else:
            l_namesb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namesb)
            self._arrays[array_handle] = l_namesb
        return l_namesb
    
    @l_namesb.setter
    def l_namesb(self, l_namesb):
        self.l_namesb[...] = l_namesb
    
    @property
    def nsb(self):
        """
        Element nsb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1152
        
        """
        return _min3p.f90wrap_chem__get__nsb()
    
    @nsb.setter
    def nsb(self, nsb):
        _min3p.f90wrap_chem__set__nsb(nsb)
    
    @property
    def nsites(self):
        """
        Element nsites ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1153
        
        """
        return _min3p.f90wrap_chem__get__nsites()
    
    @nsites.setter
    def nsites(self, nsites):
        _min3p.f90wrap_chem__set__nsites(nsites)
    
    @property
    def nsites2(self):
        """
        Element nsites2 ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1154
        
        """
        return _min3p.f90wrap_chem__get__nsites2()
    
    @nsites2.setter
    def nsites2(self, nsites2):
        _min3p.f90wrap_chem__set__nsites2(nsites2)
    
    @property
    def nlinear(self):
        """
        Element nlinear ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1155
        
        """
        return _min3p.f90wrap_chem__get__nlinear()
    
    @nlinear.setter
    def nlinear(self, nlinear):
        _min3p.f90wrap_chem__set__nlinear(nlinear)
    
    @property
    def nelec(self):
        """
        Element nelec ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1156
        
        """
        return _min3p.f90wrap_chem__get__nelec()
    
    @nelec.setter
    def nelec(self, nelec):
        _min3p.f90wrap_chem__set__nelec(nelec)
    
    @property
    def chargencsb(self):
        """
        Element chargencsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1241
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__chargencsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            chargencsb = self._arrays[array_handle]
        else:
            chargencsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__chargencsb)
            self._arrays[array_handle] = chargencsb
        return chargencsb
    
    @chargencsb.setter
    def chargencsb(self, chargencsb):
        self.chargencsb[...] = chargencsb
    
    @property
    def totan(self):
        """
        Element totan ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1242
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totan(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totan = self._arrays[array_handle]
        else:
            totan = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totan)
            self._arrays[array_handle] = totan
        return totan
    
    @totan.setter
    def totan(self, totan):
        self.totan[...] = totan
    
    @property
    def totao(self):
        """
        Element totao ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1243
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totao(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totao = self._arrays[array_handle]
        else:
            totao = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totao)
            self._arrays[array_handle] = totao
        return totao
    
    @totao.setter
    def totao(self, totao):
        self.totao[...] = totao
    
    @property
    def gfwncsb(self):
        """
        Element gfwncsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1244
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwncsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwncsb = self._arrays[array_handle]
        else:
            gfwncsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwncsb)
            self._arrays[array_handle] = gfwncsb
        return gfwncsb
    
    @gfwncsb.setter
    def gfwncsb(self, gfwncsb):
        self.gfwncsb[...] = gfwncsb
    
    @property
    def eqncsb(self):
        """
        Element eqncsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1245
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqncsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqncsb = self._arrays[array_handle]
        else:
            eqncsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqncsb)
            self._arrays[array_handle] = eqncsb
        return eqncsb
    
    @eqncsb.setter
    def eqncsb(self, eqncsb):
        self.eqncsb[...] = eqncsb
    
    @property
    def eqncsbs(self):
        """
        Element eqncsbs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1246
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqncsbs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqncsbs = self._arrays[array_handle]
        else:
            eqncsbs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqncsbs)
            self._arrays[array_handle] = eqncsbs
        return eqncsbs
    
    @eqncsbs.setter
    def eqncsbs(self, eqncsbs):
        self.eqncsbs[...] = eqncsbs
    
    @property
    def dhncsb(self):
        """
        Element dhncsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1247
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhncsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhncsb = self._arrays[array_handle]
        else:
            dhncsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhncsb)
            self._arrays[array_handle] = dhncsb
        return dhncsb
    
    @dhncsb.setter
    def dhncsb(self, dhncsb):
        self.dhncsb[...] = dhncsb
    
    @property
    def xnuncsb(self):
        """
        Element xnuncsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1248
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnuncsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnuncsb = self._arrays[array_handle]
        else:
            xnuncsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnuncsb)
            self._arrays[array_handle] = xnuncsb
        return xnuncsb
    
    @xnuncsb.setter
    def xnuncsb(self, xnuncsb):
        self.xnuncsb[...] = xnuncsb
    
    @property
    def iancsb(self):
        """
        Element iancsb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1251
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iancsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iancsb = self._arrays[array_handle]
        else:
            iancsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iancsb)
            self._arrays[array_handle] = iancsb
        return iancsb
    
    @iancsb.setter
    def iancsb(self, iancsb):
        self.iancsb[...] = iancsb
    
    @property
    def jancsb(self):
        """
        Element jancsb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1252
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jancsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jancsb = self._arrays[array_handle]
        else:
            jancsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jancsb)
            self._arrays[array_handle] = jancsb
        return jancsb
    
    @jancsb.setter
    def jancsb(self, jancsb):
        self.jancsb[...] = jancsb
    
    @property
    def l_nameanc(self):
        """
        Element l_nameanc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1253
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_nameanc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_nameanc = self._arrays[array_handle]
        else:
            l_nameanc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_nameanc)
            self._arrays[array_handle] = l_nameanc
        return l_nameanc
    
    @l_nameanc.setter
    def l_nameanc(self, l_nameanc):
        self.l_nameanc[...] = l_nameanc
    
    @property
    def nanc(self):
        """
        Element nanc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1255
        
        """
        return _min3p.f90wrap_chem__get__nanc()
    
    @nanc.setter
    def nanc(self, nanc):
        _min3p.f90wrap_chem__set__nanc(nanc)
    
    @property
    def ncsb(self):
        """
        Element ncsb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1256
        
        """
        return _min3p.f90wrap_chem__get__ncsb()
    
    @ncsb.setter
    def ncsb(self, ncsb):
        _min3p.f90wrap_chem__set__ncsb(ncsb)
    
    @property
    def noncompetitive_sorption(self):
        """
        Element noncompetitive_sorption ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1258
        
        """
        return _min3p.f90wrap_chem__get__noncompetitive_sorption()
    
    @noncompetitive_sorption.setter
    def noncompetitive_sorption(self, noncompetitive_sorption):
        _min3p.f90wrap_chem__set__noncompetitive_sorption(noncompetitive_sorption)
    
    @property
    def linear_sorption(self):
        """
        Element linear_sorption ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1259
        
        """
        return _min3p.f90wrap_chem__get__linear_sorption()
    
    @linear_sorption.setter
    def linear_sorption(self, linear_sorption):
        _min3p.f90wrap_chem__set__linear_sorption(linear_sorption)
    
    @property
    def areac(self):
        """
        Element areac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1495
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__areac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            areac = self._arrays[array_handle]
        else:
            areac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__areac)
            self._arrays[array_handle] = areac
        return areac
    
    @areac.setter
    def areac(self, areac):
        self.areac[...] = areac
    
    @property
    def areainit(self):
        """
        Element areainit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1496
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__areainit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            areainit = self._arrays[array_handle]
        else:
            areainit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__areainit)
            self._arrays[array_handle] = areainit
        return areainit
    
    @areainit.setter
    def areainit(self, areainit):
        self.areainit[...] = areainit
    
    @property
    def cmcold(self):
        """
        Element cmcold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1497
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cmcold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmcold = self._arrays[array_handle]
        else:
            cmcold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cmcold)
            self._arrays[array_handle] = cmcold
        return cmcold
    
    @cmcold.setter
    def cmcold(self, cmcold):
        self.cmcold[...] = cmcold
    
    @property
    def cmcnew(self):
        """
        Element cmcnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1498
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cmcnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmcnew = self._arrays[array_handle]
        else:
            cmcnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cmcnew)
            self._arrays[array_handle] = cmcnew
        return cmcnew
    
    @cmcnew.setter
    def cmcnew(self, cmcnew):
        self.cmcnew[...] = cmcnew
    
    @property
    def cmcmin(self):
        """
        Element cmcmin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1499
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cmcmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmcmin = self._arrays[array_handle]
        else:
            cmcmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cmcmin)
            self._arrays[array_handle] = cmcmin
        return cmcmin
    
    @cmcmin.setter
    def cmcmin(self, cmcmin):
        self.cmcmin[...] = cmcmin
    
    @property
    def dgcm(self):
        """
        Element dgcm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1500
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dgcm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dgcm = self._arrays[array_handle]
        else:
            dgcm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dgcm)
            self._arrays[array_handle] = dgcm
        return dgcm
    
    @dgcm.setter
    def dgcm(self, dgcm):
        self.dgcm[...] = dgcm
    
    @property
    def dhcm(self):
        """
        Element dhcm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1501
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcm = self._arrays[array_handle]
        else:
            dhcm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcm)
            self._arrays[array_handle] = dhcm
        return dhcm
    
    @dhcm.setter
    def dhcm(self, dhcm):
        self.dhcm[...] = dhcm
    
    @property
    def dhcmx(self):
        """
        Element dhcmx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1502
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dhcmx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dhcmx = self._arrays[array_handle]
        else:
            dhcmx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dhcmx)
            self._arrays[array_handle] = dhcmx
        return dhcmx
    
    @dhcmx.setter
    def dhcmx(self, dhcmx):
        self.dhcmx[...] = dhcmx
    
    @property
    def expphi(self):
        """
        Element expphi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1503
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__expphi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            expphi = self._arrays[array_handle]
        else:
            expphi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__expphi)
            self._arrays[array_handle] = expphi
        return expphi
    
    @expphi.setter
    def expphi(self, expphi):
        self.expphi[...] = expphi
    
    @property
    def phic(self):
        """
        Element phic ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1504
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phic = self._arrays[array_handle]
        else:
            phic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phic)
            self._arrays[array_handle] = phic
        return phic
    
    @phic.setter
    def phic(self, phic):
        self.phic[...] = phic
    
    @property
    def phicold(self):
        """
        Element phicold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1505
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phicold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phicold = self._arrays[array_handle]
        else:
            phicold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phicold)
            self._arrays[array_handle] = phicold
        return phicold
    
    @phicold.setter
    def phicold(self, phicold):
        self.phicold[...] = phicold
    
    @property
    def fmdi(self):
        """
        Element fmdi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1506
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmdi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmdi = self._arrays[array_handle]
        else:
            fmdi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmdi)
            self._arrays[array_handle] = fmdi
        return fmdi
    
    @fmdi.setter
    def fmdi(self, fmdi):
        self.fmdi[...] = fmdi
    
    @property
    def fmdm(self):
        """
        Element fmdm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1507
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmdm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmdm = self._arrays[array_handle]
        else:
            fmdm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmdm)
            self._arrays[array_handle] = fmdm
        return fmdm
    
    @fmdm.setter
    def fmdm(self, fmdm):
        self.fmdm[...] = fmdm
    
    @property
    def fmic(self):
        """
        Element fmic ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1508
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmic = self._arrays[array_handle]
        else:
            fmic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmic)
            self._arrays[array_handle] = fmic
        return fmic
    
    @fmic.setter
    def fmic(self, fmic):
        self.fmic[...] = fmic
    
    @property
    def fmhc(self):
        """
        Element fmhc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1509
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmhc = self._arrays[array_handle]
        else:
            fmhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmhc)
            self._arrays[array_handle] = fmhc
        return fmhc
    
    @fmhc.setter
    def fmhc(self, fmhc):
        self.fmhc[...] = fmhc
    
    @property
    def fmdpi(self):
        """
        Element fmdpi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1510
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmdpi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmdpi = self._arrays[array_handle]
        else:
            fmdpi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmdpi)
            self._arrays[array_handle] = fmdpi
        return fmdpi
    
    @fmdpi.setter
    def fmdpi(self, fmdpi):
        self.fmdpi[...] = fmdpi
    
    @property
    def fmdpm(self):
        """
        Element fmdpm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1511
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__fmdpm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            fmdpm = self._arrays[array_handle]
        else:
            fmdpm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__fmdpm)
            self._arrays[array_handle] = fmdpm
        return fmdpm
    
    @fmdpm.setter
    def fmdpm(self, fmdpm):
        self.fmdpm[...] = fmdpm
    
    @property
    def rads(self):
        """
        Element rads ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1512
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rads(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rads = self._arrays[array_handle]
        else:
            rads = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rads)
            self._arrays[array_handle] = rads
        return rads
    
    @rads.setter
    def rads(self, rads):
        self.rads[...] = rads
    
    @property
    def radi(self):
        """
        Element radi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1513
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__radi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            radi = self._arrays[array_handle]
        else:
            radi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__radi)
            self._arrays[array_handle] = radi
        return radi
    
    @radi.setter
    def radi(self, radi):
        self.radi[...] = radi
    
    @property
    def phimin(self):
        """
        Element phimin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1514
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phimin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phimin = self._arrays[array_handle]
        else:
            phimin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phimin)
            self._arrays[array_handle] = phimin
        return phimin
    
    @phimin.setter
    def phimin(self, phimin):
        self.phimin[...] = phimin
    
    @property
    def phimin_out(self):
        """
        Element phimin_out ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1515
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phimin_out(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phimin_out = self._arrays[array_handle]
        else:
            phimin_out = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phimin_out)
            self._arrays[array_handle] = phimin_out
        return phimin_out
    
    @phimin_out.setter
    def phimin_out(self, phimin_out):
        self.phimin_out[...] = phimin_out
    
    @property
    def phiinit(self):
        """
        Element phiinit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1516
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phiinit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phiinit = self._arrays[array_handle]
        else:
            phiinit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phiinit)
            self._arrays[array_handle] = phiinit
        return phiinit
    
    @phiinit.setter
    def phiinit(self, phiinit):
        self.phiinit[...] = phiinit
    
    @property
    def phi_out(self):
        """
        Element phi_out ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1517
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__phi_out(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phi_out = self._arrays[array_handle]
        else:
            phi_out = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__phi_out)
            self._arrays[array_handle] = phi_out
        return phi_out
    
    @phi_out.setter
    def phi_out(self, phi_out):
        self.phi_out[...] = phi_out
    
    @property
    def radmin(self):
        """
        Element radmin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1518
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__radmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            radmin = self._arrays[array_handle]
        else:
            radmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__radmin)
            self._arrays[array_handle] = radmin
        return radmin
    
    @radmin.setter
    def radmin(self, radmin):
        self.radmin[...] = radmin
    
    @property
    def supsatm(self):
        """
        Element supsatm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1519
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__supsatm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            supsatm = self._arrays[array_handle]
        else:
            supsatm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__supsatm)
            self._arrays[array_handle] = supsatm
        return supsatm
    
    @supsatm.setter
    def supsatm(self, supsatm):
        self.supsatm[...] = supsatm
    
    @property
    def scalfac(self):
        """
        Element scalfac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1520
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__scalfac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            scalfac = self._arrays[array_handle]
        else:
            scalfac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__scalfac)
            self._arrays[array_handle] = scalfac
        return scalfac
    
    @scalfac.setter
    def scalfac(self, scalfac):
        self.scalfac[...] = scalfac
    
    @property
    def gfwm(self):
        """
        Element gfwm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1521
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gfwm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfwm = self._arrays[array_handle]
        else:
            gfwm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gfwm)
            self._arrays[array_handle] = gfwm
        return gfwm
    
    @gfwm.setter
    def gfwm(self, gfwm):
        self.gfwm[...] = gfwm
    
    @property
    def diffm(self):
        """
        Element diffm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1522
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__diffm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            diffm = self._arrays[array_handle]
        else:
            diffm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__diffm)
            self._arrays[array_handle] = diffm
        return diffm
    
    @diffm.setter
    def diffm(self, diffm):
        self.diffm[...] = diffm
    
    @property
    def densm(self):
        """
        Element densm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1523
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__densm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            densm = self._arrays[array_handle]
        else:
            densm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__densm)
            self._arrays[array_handle] = densm
        return densm
    
    @densm.setter
    def densm(self, densm):
        self.densm[...] = densm
    
    @property
    def eqm(self):
        """
        Element eqm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1524
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqm = self._arrays[array_handle]
        else:
            eqm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqm)
            self._arrays[array_handle] = eqm
        return eqm
    
    @eqm.setter
    def eqm(self, eqm):
        self.eqm[...] = eqm
    
    @property
    def eqmx(self):
        """
        Element eqmx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1525
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqmx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqmx = self._arrays[array_handle]
        else:
            eqmx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqmx)
            self._arrays[array_handle] = eqmx
        return eqmx
    
    @eqmx.setter
    def eqmx(self, eqmx):
        self.eqmx[...] = eqmx
    
    @property
    def eqms(self):
        """
        Element eqms ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1526
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqms(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqms = self._arrays[array_handle]
        else:
            eqms = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqms)
            self._arrays[array_handle] = eqms
        return eqms
    
    @eqms.setter
    def eqms(self, eqms):
        self.eqms[...] = eqms
    
    @property
    def eqmxs(self):
        """
        Element eqmxs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1527
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__eqmxs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            eqmxs = self._arrays[array_handle]
        else:
            eqmxs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__eqmxs)
            self._arrays[array_handle] = eqmxs
        return eqmxs
    
    @eqmxs.setter
    def eqmxs(self, eqmxs):
        self.eqmxs[...] = eqmxs
    
    @property
    def rated(self):
        """
        Element rated ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1528
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rated(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rated = self._arrays[array_handle]
        else:
            rated = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rated)
            self._arrays[array_handle] = rated
        return rated
    
    @rated.setter
    def rated(self, rated):
        self.rated[...] = rated
    
    @property
    def rateds(self):
        """
        Element rateds ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1529
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__rateds(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateds = self._arrays[array_handle]
        else:
            rateds = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__rateds)
            self._arrays[array_handle] = rateds
        return rateds
    
    @rateds.setter
    def rateds(self, rateds):
        self.rateds[...] = rateds
    
    @property
    def ratemp(self):
        """
        Element ratemp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1530
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ratemp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratemp = self._arrays[array_handle]
        else:
            ratemp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ratemp)
            self._arrays[array_handle] = ratemp
        return ratemp
    
    @ratemp.setter
    def ratemp(self, ratemp):
        self.ratemp[...] = ratemp
    
    @property
    def orddc(self):
        """
        Element orddc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1531
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__orddc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            orddc = self._arrays[array_handle]
        else:
            orddc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__orddc)
            self._arrays[array_handle] = orddc
        return orddc
    
    @orddc.setter
    def orddc(self, orddc):
        self.orddc[...] = orddc
    
    @property
    def orddcx(self):
        """
        Element orddcx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1532
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__orddcx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            orddcx = self._arrays[array_handle]
        else:
            orddcx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__orddcx)
            self._arrays[array_handle] = orddcx
        return orddcx
    
    @orddcx.setter
    def orddcx(self, orddcx):
        self.orddcx[...] = orddcx
    
    @property
    def orddt(self):
        """
        Element orddt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1533
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__orddt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            orddt = self._arrays[array_handle]
        else:
            orddt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__orddt)
            self._arrays[array_handle] = orddt
        return orddt
    
    @orddt.setter
    def orddt(self, orddt):
        self.orddt[...] = orddt
    
    @property
    def orddm(self):
        """
        Element orddm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1534
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__orddm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            orddm = self._arrays[array_handle]
        else:
            orddm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__orddm)
            self._arrays[array_handle] = orddm
        return orddm
    
    @orddm.setter
    def orddm(self, orddm):
        self.orddm[...] = orddm
    
    @property
    def ordm(self):
        """
        Element ordm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1535
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordm = self._arrays[array_handle]
        else:
            ordm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordm)
            self._arrays[array_handle] = ordm
        return ordm
    
    @ordm.setter
    def ordm(self, ordm):
        self.ordm[...] = ordm
    
    @property
    def ordmdi(self):
        """
        Element ordmdi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1536
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmdi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmdi = self._arrays[array_handle]
        else:
            ordmdi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmdi)
            self._arrays[array_handle] = ordmdi
        return ordmdi
    
    @ordmdi.setter
    def ordmdi(self, ordmdi):
        self.ordmdi[...] = ordmdi
    
    @property
    def ordmdm(self):
        """
        Element ordmdm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1537
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmdm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmdm = self._arrays[array_handle]
        else:
            ordmdm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmdm)
            self._arrays[array_handle] = ordmdm
        return ordmdm
    
    @ordmdm.setter
    def ordmdm(self, ordmdm):
        self.ordmdm[...] = ordmdm
    
    @property
    def ordmic(self):
        """
        Element ordmic ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1538
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmic = self._arrays[array_handle]
        else:
            ordmic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmic)
            self._arrays[array_handle] = ordmic
        return ordmic
    
    @ordmic.setter
    def ordmic(self, ordmic):
        self.ordmic[...] = ordmic
    
    @property
    def ordmhc(self):
        """
        Element ordmhc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1539
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmhc = self._arrays[array_handle]
        else:
            ordmhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmhc)
            self._arrays[array_handle] = ordmhc
        return ordmhc
    
    @ordmhc.setter
    def ordmhc(self, ordmhc):
        self.ordmhc[...] = ordmhc
    
    @property
    def ordmdpi(self):
        """
        Element ordmdpi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1540
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmdpi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmdpi = self._arrays[array_handle]
        else:
            ordmdpi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmdpi)
            self._arrays[array_handle] = ordmdpi
        return ordmdpi
    
    @ordmdpi.setter
    def ordmdpi(self, ordmdpi):
        self.ordmdpi[...] = ordmdpi
    
    @property
    def ordmdpm(self):
        """
        Element ordmdpm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1541
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordmdpm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordmdpm = self._arrays[array_handle]
        else:
            ordmdpm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordmdpm)
            self._arrays[array_handle] = ordmdpm
        return ordmdpm
    
    @ordmdpm.setter
    def ordmdpm(self, ordmdpm):
        self.ordmdpm[...] = ordmdpm
    
    @property
    def ordn(self):
        """
        Element ordn ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1542
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ordn(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordn = self._arrays[array_handle]
        else:
            ordn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ordn)
            self._arrays[array_handle] = ordn
        return ordn
    
    @ordn.setter
    def ordn(self, ordn):
        self.ordn[...] = ordn
    
    @property
    def totratem(self):
        """
        Element totratem ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1543
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totratem(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totratem = self._arrays[array_handle]
        else:
            totratem = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totratem)
            self._arrays[array_handle] = totratem
        return totratem
    
    @totratem.setter
    def totratem(self, totratem):
        self.totratem[...] = totratem
    
    @property
    def xnud(self):
        """
        Element xnud ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1544
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnud(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnud = self._arrays[array_handle]
        else:
            xnud = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnud)
            self._arrays[array_handle] = xnud
        return xnud
    
    @xnud.setter
    def xnud(self, xnud):
        self.xnud[...] = xnud
    
    @property
    def xnum(self):
        """
        Element xnum ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1545
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnum(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnum = self._arrays[array_handle]
        else:
            xnum = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnum)
            self._arrays[array_handle] = xnum
        return xnum
    
    @xnum.setter
    def xnum(self, xnum):
        self.xnum[...] = xnum
    
    @property
    def xnumx(self):
        """
        Element xnumx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1546
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__xnumx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xnumx = self._arrays[array_handle]
        else:
            xnumx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__xnumx)
            self._arrays[array_handle] = xnumx
        return xnumx
    
    @xnumx.setter
    def xnumx(self, xnumx):
        self.xnumx[...] = xnumx
    
    @property
    def satm(self):
        """
        Element satm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1547
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__satm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satm = self._arrays[array_handle]
        else:
            satm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__satm)
            self._arrays[array_handle] = satm
        return satm
    
    @satm.setter
    def satm(self, satm):
        self.satm[...] = satm
    
    @property
    def satm_log(self):
        """
        Element satm_log ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1548
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__satm_log(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satm_log = self._arrays[array_handle]
        else:
            satm_log = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__satm_log)
            self._arrays[array_handle] = satm_log
        return satm_log
    
    @satm_log.setter
    def satm_log(self, satm_log):
        self.satm_log[...] = satm_log
    
    @property
    def satmx(self):
        """
        Element satmx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1549
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__satmx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satmx = self._arrays[array_handle]
        else:
            satmx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__satmx)
            self._arrays[array_handle] = satmx
        return satmx
    
    @satmx.setter
    def satmx(self, satmx):
        self.satmx[...] = satmx
    
    @property
    def conc_mol_avg(self):
        """
        Element conc_mol_avg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1551
        
        """
        return _min3p.f90wrap_chem__get__conc_mol_avg()
    
    @conc_mol_avg.setter
    def conc_mol_avg(self, conc_mol_avg):
        _min3p.f90wrap_chem__set__conc_mol_avg(conc_mol_avg)
    
    @property
    def iam(self):
        """
        Element iam ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1553
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iam(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iam = self._arrays[array_handle]
        else:
            iam = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iam)
            self._arrays[array_handle] = iam
        return iam
    
    @iam.setter
    def iam(self, iam):
        self.iam[...] = iam
    
    @property
    def iamx(self):
        """
        Element iamx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1554
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamx = self._arrays[array_handle]
        else:
            iamx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamx)
            self._arrays[array_handle] = iamx
        return iamx
    
    @iamx.setter
    def iamx(self, iamx):
        self.iamx[...] = iamx
    
    @property
    def iamd(self):
        """
        Element iamd ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1555
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamd(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamd = self._arrays[array_handle]
        else:
            iamd = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamd)
            self._arrays[array_handle] = iamd
        return iamd
    
    @iamd.setter
    def iamd(self, iamd):
        self.iamd[...] = iamd
    
    @property
    def iamdc(self):
        """
        Element iamdc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1556
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdc = self._arrays[array_handle]
        else:
            iamdc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdc)
            self._arrays[array_handle] = iamdc
        return iamdc
    
    @iamdc.setter
    def iamdc(self, iamdc):
        self.iamdc[...] = iamdc
    
    @property
    def iamdcx(self):
        """
        Element iamdcx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1557
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdcx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdcx = self._arrays[array_handle]
        else:
            iamdcx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdcx)
            self._arrays[array_handle] = iamdcx
        return iamdcx
    
    @iamdcx.setter
    def iamdcx(self, iamdcx):
        self.iamdcx[...] = iamdcx
    
    @property
    def iamdi(self):
        """
        Element iamdi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1558
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdi = self._arrays[array_handle]
        else:
            iamdi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdi)
            self._arrays[array_handle] = iamdi
        return iamdi
    
    @iamdi.setter
    def iamdi(self, iamdi):
        self.iamdi[...] = iamdi
    
    @property
    def iamdm(self):
        """
        Element iamdm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1559
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdm = self._arrays[array_handle]
        else:
            iamdm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdm)
            self._arrays[array_handle] = iamdm
        return iamdm
    
    @iamdm.setter
    def iamdm(self, iamdm):
        self.iamdm[...] = iamdm
    
    @property
    def iamic(self):
        """
        Element iamic ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1560
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamic = self._arrays[array_handle]
        else:
            iamic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamic)
            self._arrays[array_handle] = iamic
        return iamic
    
    @iamic.setter
    def iamic(self, iamic):
        self.iamic[...] = iamic
    
    @property
    def iamhc(self):
        """
        Element iamhc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1561
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamhc = self._arrays[array_handle]
        else:
            iamhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamhc)
            self._arrays[array_handle] = iamhc
        return iamhc
    
    @iamhc.setter
    def iamhc(self, iamhc):
        self.iamhc[...] = iamhc
    
    @property
    def iamdpi(self):
        """
        Element iamdpi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1562
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdpi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdpi = self._arrays[array_handle]
        else:
            iamdpi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdpi)
            self._arrays[array_handle] = iamdpi
        return iamdpi
    
    @iamdpi.setter
    def iamdpi(self, iamdpi):
        self.iamdpi[...] = iamdpi
    
    @property
    def iamdpm(self):
        """
        Element iamdpm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1563
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdpm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdpm = self._arrays[array_handle]
        else:
            iamdpm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdpm)
            self._arrays[array_handle] = iamdpm
        return iamdpm
    
    @iamdpm.setter
    def iamdpm(self, iamdpm):
        self.iamdpm[...] = iamdpm
    
    @property
    def iamdt(self):
        """
        Element iamdt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1564
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdt = self._arrays[array_handle]
        else:
            iamdt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdt)
            self._arrays[array_handle] = iamdt
        return iamdt
    
    @iamdt.setter
    def iamdt(self, iamdt):
        self.iamdt[...] = iamdt
    
    @property
    def iamdmin(self):
        """
        Element iamdmin ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1565
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamdmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamdmin = self._arrays[array_handle]
        else:
            iamdmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamdmin)
            self._arrays[array_handle] = iamdmin
        return iamdmin
    
    @iamdmin.setter
    def iamdmin(self, iamdmin):
        self.iamdmin[...] = iamdmin
    
    @property
    def iamp(self):
        """
        Element iamp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1566
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__iamp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamp = self._arrays[array_handle]
        else:
            iamp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__iamp)
            self._arrays[array_handle] = iamp
        return iamp
    
    @iamp.setter
    def iamp(self, iamp):
        self.iamp[...] = iamp
    
    @property
    def jam(self):
        """
        Element jam ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1567
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jam(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jam = self._arrays[array_handle]
        else:
            jam = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jam)
            self._arrays[array_handle] = jam
        return jam
    
    @jam.setter
    def jam(self, jam):
        self.jam[...] = jam
    
    @property
    def jamx(self):
        """
        Element jamx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1568
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamx = self._arrays[array_handle]
        else:
            jamx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamx)
            self._arrays[array_handle] = jamx
        return jamx
    
    @jamx.setter
    def jamx(self, jamx):
        self.jamx[...] = jamx
    
    @property
    def jamdc(self):
        """
        Element jamdc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1569
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdc = self._arrays[array_handle]
        else:
            jamdc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdc)
            self._arrays[array_handle] = jamdc
        return jamdc
    
    @jamdc.setter
    def jamdc(self, jamdc):
        self.jamdc[...] = jamdc
    
    @property
    def jamdcx(self):
        """
        Element jamdcx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1570
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdcx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdcx = self._arrays[array_handle]
        else:
            jamdcx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdcx)
            self._arrays[array_handle] = jamdcx
        return jamdcx
    
    @jamdcx.setter
    def jamdcx(self, jamdcx):
        self.jamdcx[...] = jamdcx
    
    @property
    def jamdi(self):
        """
        Element jamdi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1571
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdi = self._arrays[array_handle]
        else:
            jamdi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdi)
            self._arrays[array_handle] = jamdi
        return jamdi
    
    @jamdi.setter
    def jamdi(self, jamdi):
        self.jamdi[...] = jamdi
    
    @property
    def jamdm(self):
        """
        Element jamdm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1572
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdm = self._arrays[array_handle]
        else:
            jamdm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdm)
            self._arrays[array_handle] = jamdm
        return jamdm
    
    @jamdm.setter
    def jamdm(self, jamdm):
        self.jamdm[...] = jamdm
    
    @property
    def jamic(self):
        """
        Element jamic ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1573
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamic(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamic = self._arrays[array_handle]
        else:
            jamic = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamic)
            self._arrays[array_handle] = jamic
        return jamic
    
    @jamic.setter
    def jamic(self, jamic):
        self.jamic[...] = jamic
    
    @property
    def jamhc(self):
        """
        Element jamhc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1574
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamhc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamhc = self._arrays[array_handle]
        else:
            jamhc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamhc)
            self._arrays[array_handle] = jamhc
        return jamhc
    
    @jamhc.setter
    def jamhc(self, jamhc):
        self.jamhc[...] = jamhc
    
    @property
    def jamdpi(self):
        """
        Element jamdpi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1575
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdpi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdpi = self._arrays[array_handle]
        else:
            jamdpi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdpi)
            self._arrays[array_handle] = jamdpi
        return jamdpi
    
    @jamdpi.setter
    def jamdpi(self, jamdpi):
        self.jamdpi[...] = jamdpi
    
    @property
    def jamdpm(self):
        """
        Element jamdpm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1576
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdpm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdpm = self._arrays[array_handle]
        else:
            jamdpm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdpm)
            self._arrays[array_handle] = jamdpm
        return jamdpm
    
    @jamdpm.setter
    def jamdpm(self, jamdpm):
        self.jamdpm[...] = jamdpm
    
    @property
    def jamdt(self):
        """
        Element jamdt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1577
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdt = self._arrays[array_handle]
        else:
            jamdt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdt)
            self._arrays[array_handle] = jamdt
        return jamdt
    
    @jamdt.setter
    def jamdt(self, jamdt):
        self.jamdt[...] = jamdt
    
    @property
    def jamdmin(self):
        """
        Element jamdmin ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1578
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamdmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamdmin = self._arrays[array_handle]
        else:
            jamdmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamdmin)
            self._arrays[array_handle] = jamdmin
        return jamdmin
    
    @jamdmin.setter
    def jamdmin(self, jamdmin):
        self.jamdmin[...] = jamdmin
    
    @property
    def jamp(self):
        """
        Element jamp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1579
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__jamp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jamp = self._arrays[array_handle]
        else:
            jamp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__jamp)
            self._arrays[array_handle] = jamp
        return jamp
    
    @jamp.setter
    def jamp(self, jamp):
        self.jamp[...] = jamp
    
    @property
    def l_namem(self):
        """
        Element l_namem ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1580
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namem(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namem = self._arrays[array_handle]
        else:
            l_namem = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namem)
            self._arrays[array_handle] = l_namem
        return l_namem
    
    @l_namem.setter
    def l_namem(self, l_namem):
        self.l_namem[...] = l_namem
    
    @property
    def l_namemp(self):
        """
        Element l_namemp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1581
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namemp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namemp = self._arrays[array_handle]
        else:
            l_namemp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namemp)
            self._arrays[array_handle] = l_namemp
        return l_namemp
    
    @l_namemp.setter
    def l_namemp(self, l_namemp):
        self.l_namemp[...] = l_namemp
    
    @property
    def l_namemx(self):
        """
        Element l_namemx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1582
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__l_namemx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            l_namemx = self._arrays[array_handle]
        else:
            l_namemx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__l_namemx)
            self._arrays[array_handle] = l_namemx
        return l_namemx
    
    @l_namemx.setter
    def l_namemx(self, l_namemx):
        self.l_namemx[...] = l_namemx
    
    @property
    def far_from_equil(self):
        """
        Element far_from_equil ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1584
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__far_from_equil(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            far_from_equil = self._arrays[array_handle]
        else:
            far_from_equil = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__far_from_equil)
            self._arrays[array_handle] = far_from_equil
        return far_from_equil
    
    @far_from_equil.setter
    def far_from_equil(self, far_from_equil):
        self.far_from_equil[...] = far_from_equil
    
    @property
    def tmp(self):
        """
        Element tmp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1618
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__tmp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tmp = self._arrays[array_handle]
        else:
            tmp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__tmp)
            self._arrays[array_handle] = tmp
        return tmp
    
    @tmp.setter
    def tmp(self, tmp):
        self.tmp[...] = tmp
    
    @property
    def ztmp(self):
        """
        Element ztmp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1619
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ztmp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ztmp = self._arrays[array_handle]
        else:
            ztmp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ztmp)
            self._arrays[array_handle] = ztmp
        return ztmp
    
    @ztmp.setter
    def ztmp(self, ztmp):
        self.ztmp[...] = ztmp
    
    @property
    def dt_tmp(self):
        """
        Element dt_tmp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1621
        
        """
        return _min3p.f90wrap_chem__get__dt_tmp()
    
    @dt_tmp.setter
    def dt_tmp(self, dt_tmp):
        _min3p.f90wrap_chem__set__dt_tmp(dt_tmp)
    
    @property
    def tmp_read(self):
        """
        Element tmp_read ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1622
        
        """
        return _min3p.f90wrap_chem__get__tmp_read()
    
    @tmp_read.setter
    def tmp_read(self, tmp_read):
        _min3p.f90wrap_chem__set__tmp_read(tmp_read)
    
    @property
    def ntmp(self):
        """
        Element ntmp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/chem.f line 1624
        
        """
        return _min3p.f90wrap_chem__get__ntmp()
    
    @ntmp.setter
    def ntmp(self, ntmp):
        _min3p.f90wrap_chem__set__ntmp(ntmp)
    
    @property
    def update_temp(self):
        """
        Element update_temp ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1626
        
        """
        return _min3p.f90wrap_chem__get__update_temp()
    
    @update_temp.setter
    def update_temp(self, update_temp):
        _min3p.f90wrap_chem__set__update_temp(update_temp)
    
    @property
    def cinc(self):
        """
        Element cinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1693
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinc = self._arrays[array_handle]
        else:
            cinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cinc)
            self._arrays[array_handle] = cinc
        return cinc
    
    @cinc.setter
    def cinc(self, cinc):
        self.cinc[...] = cinc
    
    @property
    def cxinc(self):
        """
        Element cxinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1694
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__cxinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cxinc = self._arrays[array_handle]
        else:
            cxinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__cxinc)
            self._arrays[array_handle] = cxinc
        return cxinc
    
    @cxinc.setter
    def cxinc(self, cxinc):
        self.cxinc[...] = cxinc
    
    @property
    def dcsb(self):
        """
        Element dcsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1695
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dcsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dcsb = self._arrays[array_handle]
        else:
            dcsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dcsb)
            self._arrays[array_handle] = dcsb
        return dcsb
    
    @dcsb.setter
    def dcsb(self, dcsb):
        self.dcsb[...] = dcsb
    
    @property
    def dncsb(self):
        """
        Element dncsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1696
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dncsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dncsb = self._arrays[array_handle]
        else:
            dncsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dncsb)
            self._arrays[array_handle] = dncsb
        return dncsb
    
    @dncsb.setter
    def dncsb(self, dncsb):
        self.dncsb[...] = dncsb
    
    @property
    def ginc(self):
        """
        Element ginc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1697
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ginc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ginc = self._arrays[array_handle]
        else:
            ginc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ginc)
            self._arrays[array_handle] = ginc
        return ginc
    
    @ginc.setter
    def ginc(self, ginc):
        self.ginc[...] = ginc
    
    @property
    def dtotc(self):
        """
        Element dtotc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1698
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotc = self._arrays[array_handle]
        else:
            dtotc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotc)
            self._arrays[array_handle] = dtotc
        return dtotc
    
    @dtotc.setter
    def dtotc(self, dtotc):
        self.dtotc[...] = dtotc
    
    @property
    def dtotg(self):
        """
        Element dtotg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1699
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotg = self._arrays[array_handle]
        else:
            dtotg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotg)
            self._arrays[array_handle] = dtotg
        return dtotg
    
    @dtotg.setter
    def dtotg(self, dtotg):
        self.dtotg[...] = dtotg
    
    @property
    def dtotsb(self):
        """
        Element dtotsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1700
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotsb = self._arrays[array_handle]
        else:
            dtotsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotsb)
            self._arrays[array_handle] = dtotsb
        return dtotsb
    
    @dtotsb.setter
    def dtotsb(self, dtotsb):
        self.dtotsb[...] = dtotsb
    
    @property
    def ratedp(self):
        """
        Element ratedp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1701
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__ratedp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratedp = self._arrays[array_handle]
        else:
            ratedp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__ratedp)
            self._arrays[array_handle] = ratedp
        return ratedp
    
    @ratedp.setter
    def ratedp(self, ratedp):
        self.ratedp[...] = ratedp
    
    @property
    def dratedp(self):
        """
        Element dratedp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1702
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dratedp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dratedp = self._arrays[array_handle]
        else:
            dratedp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dratedp)
            self._arrays[array_handle] = dratedp
        return dratedp
    
    @dratedp.setter
    def dratedp(self, dratedp):
        self.dratedp[...] = dratedp
    
    @property
    def totdp(self):
        """
        Element totdp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1703
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totdp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totdp = self._arrays[array_handle]
        else:
            totdp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totdp)
            self._arrays[array_handle] = totdp
        return totdp
    
    @totdp.setter
    def totdp(self, totdp):
        self.totdp[...] = totdp
    
    @property
    def dtotdp(self):
        """
        Element dtotdp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1704
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtotdp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotdp = self._arrays[array_handle]
        else:
            dtotdp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtotdp)
            self._arrays[array_handle] = dtotdp
        return dtotdp
    
    @dtotdp.setter
    def dtotdp(self, dtotdp):
        self.dtotdp[...] = dtotdp
    
    @property
    def totsb(self):
        """
        Element totsb ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1705
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totsb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totsb = self._arrays[array_handle]
        else:
            totsb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totsb)
            self._arrays[array_handle] = totsb
        return totsb
    
    @totsb.setter
    def totsb(self, totsb):
        self.totsb[...] = totsb
    
    @property
    def totcinc(self):
        """
        Element totcinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1706
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__totcinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcinc = self._arrays[array_handle]
        else:
            totcinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__totcinc)
            self._arrays[array_handle] = totcinc
        return totcinc
    
    @totcinc.setter
    def totcinc(self, totcinc):
        self.totcinc[...] = totcinc
    
    @property
    def dtota(self):
        """
        Element dtota ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1707
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__dtota(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtota = self._arrays[array_handle]
        else:
            dtota = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__dtota)
            self._arrays[array_handle] = dtota
        return dtota
    
    @dtota.setter
    def dtota(self, dtota):
        self.dtota[...] = dtota
    
    @property
    def alc(self):
        """
        Element alc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1726
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__alc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            alc = self._arrays[array_handle]
        else:
            alc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__alc)
            self._arrays[array_handle] = alc
        return alc
    
    @alc.setter
    def alc(self, alc):
        self.alc[...] = alc
    
    @property
    def blc(self):
        """
        Element blc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1727
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__blc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            blc = self._arrays[array_handle]
        else:
            blc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__blc)
            self._arrays[array_handle] = blc
        return blc
    
    @blc.setter
    def blc(self, blc):
        self.blc[...] = blc
    
    @property
    def conct(self):
        """
        Element conct ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1728
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__conct(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            conct = self._arrays[array_handle]
        else:
            conct = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__conct)
            self._arrays[array_handle] = conct
        return conct
    
    @conct.setter
    def conct(self, conct):
        self.conct[...] = conct
    
    @property
    def gammat(self):
        """
        Element gammat ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/chem.f line 1729
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_chem__array__gammat(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gammat = self._arrays[array_handle]
        else:
            gammat = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_chem__array__gammat)
            self._arrays[array_handle] = gammat
        return gammat
    
    @gammat.setter
    def gammat(self, gammat):
        self.gammat[...] = gammat
    
    @property
    def depth_dependence(self):
        """
        Element depth_dependence ftype=logical pytype=bool
        
        
        Defined at ../src/chem.f line 1735
        
        """
        return _min3p.f90wrap_chem__get__depth_dependence()
    
    @depth_dependence.setter
    def depth_dependence(self, depth_dependence):
        _min3p.f90wrap_chem__set__depth_dependence(depth_dependence)
    
    def __str__(self):
        ret = ['<chem>{\n']
        ret.append('    acth2omin : ')
        ret.append(repr(self.acth2omin))
        ret.append(',\n    dinc_lc : ')
        ret.append(repr(self.dinc_lc))
        ret.append(',\n    ph_fixed : ')
        ret.append(repr(self.ph_fixed))
        ret.append(',\n    ph_inc : ')
        ret.append(repr(self.ph_inc))
        ret.append(',\n    ph_start : ')
        ret.append(repr(self.ph_start))
        ret.append(',\n    ph_stop : ')
        ret.append(repr(self.ph_stop))
        ret.append(',\n    sionmax : ')
        ret.append(repr(self.sionmax))
        ret.append(',\n    srelfac_lc : ')
        ret.append(repr(self.srelfac_lc))
        ret.append(',\n    tempc : ')
        ret.append(repr(self.tempc))
        ret.append(',\n    tempk : ')
        ret.append(repr(self.tempk))
        ret.append(',\n    tfinal_lc : ')
        ret.append(repr(self.tfinal_lc))
        ret.append(',\n    tinyrate : ')
        ret.append(repr(self.tinyrate))
        ret.append(',\n    time_factor_lc : ')
        ret.append(repr(self.time_factor_lc))
        ret.append(',\n    tol_lc : ')
        ret.append(repr(self.tol_lc))
        ret.append(',\n    ncorder : ')
        ret.append(repr(self.ncorder))
        ret.append(',\n    iph_steps : ')
        ret.append(repr(self.iph_steps))
        ret.append(',\n    maxit_lc : ')
        ret.append(repr(self.maxit_lc))
        ret.append(',\n    idetail_lc : ')
        ret.append(repr(self.idetail_lc))
        ret.append(',\n    ittot_lc : ')
        ret.append(repr(self.ittot_lc))
        ret.append(',\n    iter_lc : ')
        ret.append(repr(self.iter_lc))
        ret.append(',\n    naq : ')
        ret.append(repr(self.naq))
        ret.append(',\n    nc : ')
        ret.append(repr(self.nc))
        ret.append(',\n    nx : ')
        ret.append(repr(self.nx))
        ret.append(',\n    nm : ')
        ret.append(repr(self.nm))
        ret.append(',\n    nmx : ')
        ret.append(repr(self.nmx))
        ret.append(',\n    nopu : ')
        ret.append(repr(self.nopu))
        ret.append(',\n    ng : ')
        ret.append(repr(self.ng))
        ret.append(',\n    nr : ')
        ret.append(repr(self.nr))
        ret.append(',\n    nph_steps : ')
        ret.append(repr(self.nph_steps))
        ret.append(',\n    ivolindice : ')
        ret.append(repr(self.ivolindice))
        ret.append(',\n    minequil : ')
        ret.append(repr(self.minequil))
        ret.append(',\n    compute_alkalinity : ')
        ret.append(repr(self.compute_alkalinity))
        ret.append(',\n    explicit_surface : ')
        ret.append(repr(self.explicit_surface))
        ret.append(',\n    finite_minerals : ')
        ret.append(repr(self.finite_minerals))
        ret.append(',\n    implicit_surface : ')
        ret.append(repr(self.implicit_surface))
        ret.append(',\n    new_database : ')
        ret.append(repr(self.new_database))
        ret.append(',\n    ph_sweep : ')
        ret.append(repr(self.ph_sweep))
        ret.append(',\n    reactive_minerals : ')
        ret.append(repr(self.reactive_minerals))
        ret.append(',\n    redox_equil_lc : ')
        ret.append(repr(self.redox_equil_lc))
        ret.append(',\n    search_database : ')
        ret.append(repr(self.search_database))
        ret.append(',\n    specified_ph : ')
        ret.append(repr(self.specified_ph))
        ret.append(',\n    temp_corr : ')
        ret.append(repr(self.temp_corr))
        ret.append(',\n    temp_field : ')
        ret.append(repr(self.temp_field))
        ret.append(',\n    tstart_to_equil : ')
        ret.append(repr(self.tstart_to_equil))
        ret.append(',\n    tstart_to_tfinal : ')
        ret.append(repr(self.tstart_to_tfinal))
        ret.append(',\n    adav : ')
        ret.append(repr(self.adav))
        ret.append(',\n    avog_const : ')
        ret.append(repr(self.avog_const))
        ret.append(',\n    bdav : ')
        ret.append(repr(self.bdav))
        ret.append(',\n    diel_const : ')
        ret.append(repr(self.diel_const))
        ret.append(',\n    dhad : ')
        ret.append(repr(self.dhad))
        ret.append(',\n    dhbd : ')
        ret.append(repr(self.dhbd))
        ret.append(',\n    ehfac : ')
        ret.append(repr(self.ehfac))
        ret.append(',\n    farad_const : ')
        ret.append(repr(self.farad_const))
        ret.append(',\n    g_acc : ')
        ret.append(repr(self.g_acc))
        ret.append(',\n    pa_atm : ')
        ret.append(repr(self.pa_atm))
        ret.append(',\n    permit_const : ')
        ret.append(repr(self.permit_const))
        ret.append(',\n    pres_atm : ')
        ret.append(repr(self.pres_atm))
        ret.append(',\n    tempcs : ')
        ret.append(repr(self.tempcs))
        ret.append(',\n    tempks : ')
        ret.append(repr(self.tempks))
        ret.append(',\n    tconv : ')
        ret.append(repr(self.tconv))
        ret.append(',\n    rgas : ')
        ret.append(repr(self.rgas))
        ret.append(',\n    rgascal : ')
        ret.append(repr(self.rgascal))
        ret.append(',\n    rgasjoule : ')
        ret.append(repr(self.rgasjoule))
        ret.append(',\n    rho_w : ')
        ret.append(repr(self.rho_w))
        ret.append(',\n    delt_lc : ')
        ret.append(repr(self.delt_lc))
        ret.append(',\n    delt_max_lc : ')
        ret.append(repr(self.delt_max_lc))
        ret.append(',\n    ntstp_lc : ')
        ret.append(repr(self.ntstp_lc))
        ret.append(',\n    ilbb : ')
        ret.append(repr(self.ilbb))
        ret.append(',\n    ilbc : ')
        ret.append(repr(self.ilbc))
        ret.append(',\n    ilbd : ')
        ret.append(repr(self.ilbd))
        ret.append(',\n    ilbg : ')
        ret.append(repr(self.ilbg))
        ret.append(',\n    ilbgr : ')
        ret.append(repr(self.ilbgr))
        ret.append(',\n    ilbm : ')
        ret.append(repr(self.ilbm))
        ret.append(',\n    ilbi : ')
        ret.append(repr(self.ilbi))
        ret.append(',\n    ilbs : ')
        ret.append(repr(self.ilbs))
        ret.append(',\n    ilbt : ')
        ret.append(repr(self.ilbt))
        ret.append(',\n    ilbv : ')
        ret.append(repr(self.ilbv))
        ret.append(',\n    ilbx : ')
        ret.append(repr(self.ilbx))
        ret.append(',\n    lb_output : ')
        ret.append(repr(self.lb_output))
        ret.append(',\n    pe_output : ')
        ret.append(repr(self.pe_output))
        ret.append(',\n    ph_output : ')
        ret.append(repr(self.ph_output))
        ret.append(',\n    actv : ')
        ret.append(repr(self.actv))
        ret.append(',\n    alkfacc : ')
        ret.append(repr(self.alkfacc))
        ret.append(',\n    alkfacx : ')
        ret.append(repr(self.alkfacx))
        ret.append(',\n    totcinit : ')
        ret.append(repr(self.totcinit))
        ret.append(',\n    totcn : ')
        ret.append(repr(self.totcn))
        ret.append(',\n    totcmin : ')
        ret.append(repr(self.totcmin))
        ret.append(',\n    totco : ')
        ret.append(repr(self.totco))
        ret.append(',\n    ccnew : ')
        ret.append(repr(self.ccnew))
        ret.append(',\n    ccold : ')
        ret.append(repr(self.ccold))
        ret.append(',\n    gamma_l : ')
        ret.append(repr(self.gamma_l))
        ret.append(',\n    chargec : ')
        ret.append(repr(self.chargec))
        ret.append(',\n    gfwc : ')
        ret.append(repr(self.gfwc))
        ret.append(',\n    distcoff_lc : ')
        ret.append(repr(self.distcoff_lc))
        ret.append(',\n    nfr : ')
        ret.append(repr(self.nfr))
        ret.append(',\n    lang : ')
        ret.append(repr(self.lang))
        ret.append(',\n    pdm : ')
        ret.append(repr(self.pdm))
        ret.append(',\n    dhac : ')
        ret.append(repr(self.dhac))
        ret.append(',\n    dhbc : ')
        ret.append(repr(self.dhbc))
        ret.append(',\n    cxc : ')
        ret.append(repr(self.cxc))
        ret.append(',\n    cxmax : ')
        ret.append(repr(self.cxmax))
        ret.append(',\n    chargex : ')
        ret.append(repr(self.chargex))
        ret.append(',\n    eqx : ')
        ret.append(repr(self.eqx))
        ret.append(',\n    eqxs : ')
        ret.append(repr(self.eqxs))
        ret.append(',\n    gfwx : ')
        ret.append(repr(self.gfwx))
        ret.append(',\n    dhcx : ')
        ret.append(repr(self.dhcx))
        ret.append(',\n    dhax : ')
        ret.append(repr(self.dhax))
        ret.append(',\n    dhbx : ')
        ret.append(repr(self.dhbx))
        ret.append(',\n    xnux : ')
        ret.append(repr(self.xnux))
        ret.append(',\n    sion1 : ')
        ret.append(repr(self.sion1))
        ret.append(',\n    phguess : ')
        ret.append(repr(self.phguess))
        ret.append(',\n    iax : ')
        ret.append(repr(self.iax))
        ret.append(',\n    jax : ')
        ret.append(repr(self.jax))
        ret.append(',\n    l_namec : ')
        ret.append(repr(self.l_namec))
        ret.append(',\n    l_namex : ')
        ret.append(repr(self.l_namex))
        ret.append(',\n    cequil_kin : ')
        ret.append(repr(self.cequil_kin))
        ret.append(',\n    clang_kin : ')
        ret.append(repr(self.clang_kin))
        ret.append(',\n    smax_kin : ')
        ret.append(repr(self.smax_kin))
        ret.append(',\n    cfreund_kin : ')
        ret.append(repr(self.cfreund_kin))
        ret.append(',\n    exponfreund_kin : ')
        ret.append(repr(self.exponfreund_kin))
        ret.append(',\n    eqaq : ')
        ret.append(repr(self.eqaq))
        ret.append(',\n    eqaqs : ')
        ret.append(repr(self.eqaqs))
        ret.append(',\n    dgaq : ')
        ret.append(repr(self.dgaq))
        ret.append(',\n    dhaq : ')
        ret.append(repr(self.dhaq))
        ret.append(',\n    dtotaq : ')
        ret.append(repr(self.dtotaq))
        ret.append(',\n    faqhc : ')
        ret.append(repr(self.faqhc))
        ret.append(',\n    faqht : ')
        ret.append(repr(self.faqht))
        ret.append(',\n    faqhm : ')
        ret.append(repr(self.faqhm))
        ret.append(',\n    faqi : ')
        ret.append(repr(self.faqi))
        ret.append(',\n    faqic : ')
        ret.append(repr(self.faqic))
        ret.append(',\n    faqit : ')
        ret.append(repr(self.faqit))
        ret.append(',\n    faqim : ')
        ret.append(repr(self.faqim))
        ret.append(',\n    ordaqic : ')
        ret.append(repr(self.ordaqic))
        ret.append(',\n    ordaqit : ')
        ret.append(repr(self.ordaqit))
        ret.append(',\n    ordaqim : ')
        ret.append(repr(self.ordaqim))
        ret.append(',\n    ordaqhc : ')
        ret.append(repr(self.ordaqhc))
        ret.append(',\n    ordaqht : ')
        ret.append(repr(self.ordaqht))
        ret.append(',\n    ordaqhm : ')
        ret.append(repr(self.ordaqhm))
        ret.append(',\n    ordaqt : ')
        ret.append(repr(self.ordaqt))
        ret.append(',\n    ordaqc : ')
        ret.append(repr(self.ordaqc))
        ret.append(',\n    ordaqx : ')
        ret.append(repr(self.ordaqx))
        ret.append(',\n    ordaqm : ')
        ret.append(repr(self.ordaqm))
        ret.append(',\n    rateaq : ')
        ret.append(repr(self.rateaq))
        ret.append(',\n    ratecaq : ')
        ret.append(repr(self.ratecaq))
        ret.append(',\n    ratecaqs : ')
        ret.append(repr(self.ratecaqs))
        ret.append(',\n    sataq : ')
        ret.append(repr(self.sataq))
        ret.append(',\n    scalfac_aq : ')
        ret.append(repr(self.scalfac_aq))
        ret.append(',\n    totaq : ')
        ret.append(repr(self.totaq))
        ret.append(',\n    xnuaq : ')
        ret.append(repr(self.xnuaq))
        ret.append(',\n    iaaq : ')
        ret.append(repr(self.iaaq))
        ret.append(',\n    iaaqi : ')
        ret.append(repr(self.iaaqi))
        ret.append(',\n    iaaqic : ')
        ret.append(repr(self.iaaqic))
        ret.append(',\n    iaaqit : ')
        ret.append(repr(self.iaaqit))
        ret.append(',\n    iaaqim : ')
        ret.append(repr(self.iaaqim))
        ret.append(',\n    iaaqhc : ')
        ret.append(repr(self.iaaqhc))
        ret.append(',\n    iaaqht : ')
        ret.append(repr(self.iaaqht))
        ret.append(',\n    iaaqhm : ')
        ret.append(repr(self.iaaqhm))
        ret.append(',\n    iaaqt : ')
        ret.append(repr(self.iaaqt))
        ret.append(',\n    iaequil : ')
        ret.append(repr(self.iaequil))
        ret.append(',\n    iaaqc : ')
        ret.append(repr(self.iaaqc))
        ret.append(',\n    iaaqx : ')
        ret.append(repr(self.iaaqx))
        ret.append(',\n    iaaqm : ')
        ret.append(repr(self.iaaqm))
        ret.append(',\n    jaaq : ')
        ret.append(repr(self.jaaq))
        ret.append(',\n    jaaqt : ')
        ret.append(repr(self.jaaqt))
        ret.append(',\n    jaequil : ')
        ret.append(repr(self.jaequil))
        ret.append(',\n    jaaqc : ')
        ret.append(repr(self.jaaqc))
        ret.append(',\n    jaaqx : ')
        ret.append(repr(self.jaaqx))
        ret.append(',\n    jaaqm : ')
        ret.append(repr(self.jaaqm))
        ret.append(',\n    jaaqhc : ')
        ret.append(repr(self.jaaqhc))
        ret.append(',\n    jaaqht : ')
        ret.append(repr(self.jaaqht))
        ret.append(',\n    jaaqhm : ')
        ret.append(repr(self.jaaqhm))
        ret.append(',\n    jaaqi : ')
        ret.append(repr(self.jaaqi))
        ret.append(',\n    jaaqic : ')
        ret.append(repr(self.jaaqic))
        ret.append(',\n    jaaqit : ')
        ret.append(repr(self.jaaqit))
        ret.append(',\n    jaaqim : ')
        ret.append(repr(self.jaaqim))
        ret.append(',\n    l_nameaq : ')
        ret.append(repr(self.l_nameaq))
        ret.append(',\n    bcatfac : ')
        ret.append(repr(self.bcatfac))
        ret.append(',\n    dhcr : ')
        ret.append(repr(self.dhcr))
        ret.append(',\n    dtotor : ')
        ret.append(repr(self.dtotor))
        ret.append(',\n    eqr : ')
        ret.append(repr(self.eqr))
        ret.append(',\n    eqrs : ')
        ret.append(repr(self.eqrs))
        ret.append(',\n    chomc : ')
        ret.append(repr(self.chomc))
        ret.append(',\n    chomt : ')
        ret.append(repr(self.chomt))
        ret.append(',\n    chomx : ')
        ret.append(repr(self.chomx))
        ret.append(',\n    ordorc : ')
        ret.append(repr(self.ordorc))
        ret.append(',\n    ordort : ')
        ret.append(repr(self.ordort))
        ret.append(',\n    ordorx : ')
        ret.append(repr(self.ordorx))
        ret.append(',\n    rateor : ')
        ret.append(repr(self.rateor))
        ret.append(',\n    rateox : ')
        ret.append(repr(self.rateox))
        ret.append(',\n    totor : ')
        ret.append(repr(self.totor))
        ret.append(',\n    xnur : ')
        ret.append(repr(self.xnur))
        ret.append(',\n    iaor : ')
        ret.append(repr(self.iaor))
        ret.append(',\n    iaorc : ')
        ret.append(repr(self.iaorc))
        ret.append(',\n    iaort : ')
        ret.append(repr(self.iaort))
        ret.append(',\n    iaorx : ')
        ret.append(repr(self.iaorx))
        ret.append(',\n    iarc : ')
        ret.append(repr(self.iarc))
        ret.append(',\n    iars : ')
        ret.append(repr(self.iars))
        ret.append(',\n    jaorc : ')
        ret.append(repr(self.jaorc))
        ret.append(',\n    jaort : ')
        ret.append(repr(self.jaort))
        ret.append(',\n    jaorx : ')
        ret.append(repr(self.jaorx))
        ret.append(',\n    jarc : ')
        ret.append(repr(self.jarc))
        ret.append(',\n    l_namer : ')
        ret.append(repr(self.l_namer))
        ret.append(',\n    l_namerp : ')
        ret.append(repr(self.l_namerp))
        ret.append(',\n    l_namers : ')
        ret.append(repr(self.l_namers))
        ret.append(',\n    ncrc : ')
        ret.append(repr(self.ncrc))
        ret.append(',\n    nor : ')
        ret.append(repr(self.nor))
        ret.append(',\n    norc : ')
        ret.append(repr(self.norc))
        ret.append(',\n    nort : ')
        ret.append(repr(self.nort))
        ret.append(',\n    norx : ')
        ret.append(repr(self.norx))
        ret.append(',\n    redox_equil : ')
        ret.append(repr(self.redox_equil))
        ret.append(',\n    cgc : ')
        ret.append(repr(self.cgc))
        ret.append(',\n    rateg : ')
        ret.append(repr(self.rateg))
        ret.append(',\n    totgn : ')
        ret.append(repr(self.totgn))
        ret.append(',\n    totgo : ')
        ret.append(repr(self.totgo))
        ret.append(',\n    totrateg : ')
        ret.append(repr(self.totrateg))
        ret.append(',\n    gfwg : ')
        ret.append(repr(self.gfwg))
        ret.append(',\n    eqg : ')
        ret.append(repr(self.eqg))
        ret.append(',\n    eqgs : ')
        ret.append(repr(self.eqgs))
        ret.append(',\n    dhcg : ')
        ret.append(repr(self.dhcg))
        ret.append(',\n    xnug : ')
        ret.append(repr(self.xnug))
        ret.append(',\n    degas_rate : ')
        ret.append(repr(self.degas_rate))
        ret.append(',\n    iaga : ')
        ret.append(repr(self.iaga))
        ret.append(',\n    jaga : ')
        ret.append(repr(self.jaga))
        ret.append(',\n    l_nameg : ')
        ret.append(repr(self.l_nameg))
        ret.append(',\n    gas_removal : ')
        ret.append(repr(self.gas_removal))
        ret.append(',\n    csb : ')
        ret.append(repr(self.csb))
        ret.append(',\n    chargesb : ')
        ret.append(repr(self.chargesb))
        ret.append(',\n    totcsn : ')
        ret.append(repr(self.totcsn))
        ret.append(',\n    totcso : ')
        ret.append(repr(self.totcso))
        ret.append(',\n    gfwsb : ')
        ret.append(repr(self.gfwsb))
        ret.append(',\n    eqsb : ')
        ret.append(repr(self.eqsb))
        ret.append(',\n    eqsbs : ')
        ret.append(repr(self.eqsbs))
        ret.append(',\n    dhcsb : ')
        ret.append(repr(self.dhcsb))
        ret.append(',\n    xnusb : ')
        ret.append(repr(self.xnusb))
        ret.append(',\n    site_area : ')
        ret.append(repr(self.site_area))
        ret.append(',\n    site_dens : ')
        ret.append(repr(self.site_dens))
        ret.append(',\n    site_mass : ')
        ret.append(repr(self.site_mass))
        ret.append(',\n    dcalcpsi : ')
        ret.append(repr(self.dcalcpsi))
        ret.append(',\n    cap1 : ')
        ret.append(repr(self.cap1))
        ret.append(',\n    cap2 : ')
        ret.append(repr(self.cap2))
        ret.append(',\n    strionsb : ')
        ret.append(repr(self.strionsb))
        ret.append(',\n    surfacensb : ')
        ret.append(repr(self.surfacensb))
        ret.append(',\n    calcpsi : ')
        ret.append(repr(self.calcpsi))
        ret.append(',\n    totpsi : ')
        ret.append(repr(self.totpsi))
        ret.append(',\n    dtotpsi : ')
        ret.append(repr(self.dtotpsi))
        ret.append(',\n    dcnew : ')
        ret.append(repr(self.dcnew))
        ret.append(',\n    cec : ')
        ret.append(repr(self.cec))
        ret.append(',\n    rhobulk : ')
        ret.append(repr(self.rhobulk))
        ret.append(',\n    iaic : ')
        ret.append(repr(self.iaic))
        ret.append(',\n    iais : ')
        ret.append(repr(self.iais))
        ret.append(',\n    iasb : ')
        ret.append(repr(self.iasb))
        ret.append(',\n    jasb : ')
        ret.append(repr(self.jasb))
        ret.append(',\n    l_namesb : ')
        ret.append(repr(self.l_namesb))
        ret.append(',\n    nsb : ')
        ret.append(repr(self.nsb))
        ret.append(',\n    nsites : ')
        ret.append(repr(self.nsites))
        ret.append(',\n    nsites2 : ')
        ret.append(repr(self.nsites2))
        ret.append(',\n    nlinear : ')
        ret.append(repr(self.nlinear))
        ret.append(',\n    nelec : ')
        ret.append(repr(self.nelec))
        ret.append(',\n    chargencsb : ')
        ret.append(repr(self.chargencsb))
        ret.append(',\n    totan : ')
        ret.append(repr(self.totan))
        ret.append(',\n    totao : ')
        ret.append(repr(self.totao))
        ret.append(',\n    gfwncsb : ')
        ret.append(repr(self.gfwncsb))
        ret.append(',\n    eqncsb : ')
        ret.append(repr(self.eqncsb))
        ret.append(',\n    eqncsbs : ')
        ret.append(repr(self.eqncsbs))
        ret.append(',\n    dhncsb : ')
        ret.append(repr(self.dhncsb))
        ret.append(',\n    xnuncsb : ')
        ret.append(repr(self.xnuncsb))
        ret.append(',\n    iancsb : ')
        ret.append(repr(self.iancsb))
        ret.append(',\n    jancsb : ')
        ret.append(repr(self.jancsb))
        ret.append(',\n    l_nameanc : ')
        ret.append(repr(self.l_nameanc))
        ret.append(',\n    nanc : ')
        ret.append(repr(self.nanc))
        ret.append(',\n    ncsb : ')
        ret.append(repr(self.ncsb))
        ret.append(',\n    noncompetitive_sorption : ')
        ret.append(repr(self.noncompetitive_sorption))
        ret.append(',\n    linear_sorption : ')
        ret.append(repr(self.linear_sorption))
        ret.append(',\n    areac : ')
        ret.append(repr(self.areac))
        ret.append(',\n    areainit : ')
        ret.append(repr(self.areainit))
        ret.append(',\n    cmcold : ')
        ret.append(repr(self.cmcold))
        ret.append(',\n    cmcnew : ')
        ret.append(repr(self.cmcnew))
        ret.append(',\n    cmcmin : ')
        ret.append(repr(self.cmcmin))
        ret.append(',\n    dgcm : ')
        ret.append(repr(self.dgcm))
        ret.append(',\n    dhcm : ')
        ret.append(repr(self.dhcm))
        ret.append(',\n    dhcmx : ')
        ret.append(repr(self.dhcmx))
        ret.append(',\n    expphi : ')
        ret.append(repr(self.expphi))
        ret.append(',\n    phic : ')
        ret.append(repr(self.phic))
        ret.append(',\n    phicold : ')
        ret.append(repr(self.phicold))
        ret.append(',\n    fmdi : ')
        ret.append(repr(self.fmdi))
        ret.append(',\n    fmdm : ')
        ret.append(repr(self.fmdm))
        ret.append(',\n    fmic : ')
        ret.append(repr(self.fmic))
        ret.append(',\n    fmhc : ')
        ret.append(repr(self.fmhc))
        ret.append(',\n    fmdpi : ')
        ret.append(repr(self.fmdpi))
        ret.append(',\n    fmdpm : ')
        ret.append(repr(self.fmdpm))
        ret.append(',\n    rads : ')
        ret.append(repr(self.rads))
        ret.append(',\n    radi : ')
        ret.append(repr(self.radi))
        ret.append(',\n    phimin : ')
        ret.append(repr(self.phimin))
        ret.append(',\n    phimin_out : ')
        ret.append(repr(self.phimin_out))
        ret.append(',\n    phiinit : ')
        ret.append(repr(self.phiinit))
        ret.append(',\n    phi_out : ')
        ret.append(repr(self.phi_out))
        ret.append(',\n    radmin : ')
        ret.append(repr(self.radmin))
        ret.append(',\n    supsatm : ')
        ret.append(repr(self.supsatm))
        ret.append(',\n    scalfac : ')
        ret.append(repr(self.scalfac))
        ret.append(',\n    gfwm : ')
        ret.append(repr(self.gfwm))
        ret.append(',\n    diffm : ')
        ret.append(repr(self.diffm))
        ret.append(',\n    densm : ')
        ret.append(repr(self.densm))
        ret.append(',\n    eqm : ')
        ret.append(repr(self.eqm))
        ret.append(',\n    eqmx : ')
        ret.append(repr(self.eqmx))
        ret.append(',\n    eqms : ')
        ret.append(repr(self.eqms))
        ret.append(',\n    eqmxs : ')
        ret.append(repr(self.eqmxs))
        ret.append(',\n    rated : ')
        ret.append(repr(self.rated))
        ret.append(',\n    rateds : ')
        ret.append(repr(self.rateds))
        ret.append(',\n    ratemp : ')
        ret.append(repr(self.ratemp))
        ret.append(',\n    orddc : ')
        ret.append(repr(self.orddc))
        ret.append(',\n    orddcx : ')
        ret.append(repr(self.orddcx))
        ret.append(',\n    orddt : ')
        ret.append(repr(self.orddt))
        ret.append(',\n    orddm : ')
        ret.append(repr(self.orddm))
        ret.append(',\n    ordm : ')
        ret.append(repr(self.ordm))
        ret.append(',\n    ordmdi : ')
        ret.append(repr(self.ordmdi))
        ret.append(',\n    ordmdm : ')
        ret.append(repr(self.ordmdm))
        ret.append(',\n    ordmic : ')
        ret.append(repr(self.ordmic))
        ret.append(',\n    ordmhc : ')
        ret.append(repr(self.ordmhc))
        ret.append(',\n    ordmdpi : ')
        ret.append(repr(self.ordmdpi))
        ret.append(',\n    ordmdpm : ')
        ret.append(repr(self.ordmdpm))
        ret.append(',\n    ordn : ')
        ret.append(repr(self.ordn))
        ret.append(',\n    totratem : ')
        ret.append(repr(self.totratem))
        ret.append(',\n    xnud : ')
        ret.append(repr(self.xnud))
        ret.append(',\n    xnum : ')
        ret.append(repr(self.xnum))
        ret.append(',\n    xnumx : ')
        ret.append(repr(self.xnumx))
        ret.append(',\n    satm : ')
        ret.append(repr(self.satm))
        ret.append(',\n    satm_log : ')
        ret.append(repr(self.satm_log))
        ret.append(',\n    satmx : ')
        ret.append(repr(self.satmx))
        ret.append(',\n    conc_mol_avg : ')
        ret.append(repr(self.conc_mol_avg))
        ret.append(',\n    iam : ')
        ret.append(repr(self.iam))
        ret.append(',\n    iamx : ')
        ret.append(repr(self.iamx))
        ret.append(',\n    iamd : ')
        ret.append(repr(self.iamd))
        ret.append(',\n    iamdc : ')
        ret.append(repr(self.iamdc))
        ret.append(',\n    iamdcx : ')
        ret.append(repr(self.iamdcx))
        ret.append(',\n    iamdi : ')
        ret.append(repr(self.iamdi))
        ret.append(',\n    iamdm : ')
        ret.append(repr(self.iamdm))
        ret.append(',\n    iamic : ')
        ret.append(repr(self.iamic))
        ret.append(',\n    iamhc : ')
        ret.append(repr(self.iamhc))
        ret.append(',\n    iamdpi : ')
        ret.append(repr(self.iamdpi))
        ret.append(',\n    iamdpm : ')
        ret.append(repr(self.iamdpm))
        ret.append(',\n    iamdt : ')
        ret.append(repr(self.iamdt))
        ret.append(',\n    iamdmin : ')
        ret.append(repr(self.iamdmin))
        ret.append(',\n    iamp : ')
        ret.append(repr(self.iamp))
        ret.append(',\n    jam : ')
        ret.append(repr(self.jam))
        ret.append(',\n    jamx : ')
        ret.append(repr(self.jamx))
        ret.append(',\n    jamdc : ')
        ret.append(repr(self.jamdc))
        ret.append(',\n    jamdcx : ')
        ret.append(repr(self.jamdcx))
        ret.append(',\n    jamdi : ')
        ret.append(repr(self.jamdi))
        ret.append(',\n    jamdm : ')
        ret.append(repr(self.jamdm))
        ret.append(',\n    jamic : ')
        ret.append(repr(self.jamic))
        ret.append(',\n    jamhc : ')
        ret.append(repr(self.jamhc))
        ret.append(',\n    jamdpi : ')
        ret.append(repr(self.jamdpi))
        ret.append(',\n    jamdpm : ')
        ret.append(repr(self.jamdpm))
        ret.append(',\n    jamdt : ')
        ret.append(repr(self.jamdt))
        ret.append(',\n    jamdmin : ')
        ret.append(repr(self.jamdmin))
        ret.append(',\n    jamp : ')
        ret.append(repr(self.jamp))
        ret.append(',\n    l_namem : ')
        ret.append(repr(self.l_namem))
        ret.append(',\n    l_namemp : ')
        ret.append(repr(self.l_namemp))
        ret.append(',\n    l_namemx : ')
        ret.append(repr(self.l_namemx))
        ret.append(',\n    far_from_equil : ')
        ret.append(repr(self.far_from_equil))
        ret.append(',\n    tmp : ')
        ret.append(repr(self.tmp))
        ret.append(',\n    ztmp : ')
        ret.append(repr(self.ztmp))
        ret.append(',\n    dt_tmp : ')
        ret.append(repr(self.dt_tmp))
        ret.append(',\n    tmp_read : ')
        ret.append(repr(self.tmp_read))
        ret.append(',\n    ntmp : ')
        ret.append(repr(self.ntmp))
        ret.append(',\n    update_temp : ')
        ret.append(repr(self.update_temp))
        ret.append(',\n    cinc : ')
        ret.append(repr(self.cinc))
        ret.append(',\n    cxinc : ')
        ret.append(repr(self.cxinc))
        ret.append(',\n    dcsb : ')
        ret.append(repr(self.dcsb))
        ret.append(',\n    dncsb : ')
        ret.append(repr(self.dncsb))
        ret.append(',\n    ginc : ')
        ret.append(repr(self.ginc))
        ret.append(',\n    dtotc : ')
        ret.append(repr(self.dtotc))
        ret.append(',\n    dtotg : ')
        ret.append(repr(self.dtotg))
        ret.append(',\n    dtotsb : ')
        ret.append(repr(self.dtotsb))
        ret.append(',\n    ratedp : ')
        ret.append(repr(self.ratedp))
        ret.append(',\n    dratedp : ')
        ret.append(repr(self.dratedp))
        ret.append(',\n    totdp : ')
        ret.append(repr(self.totdp))
        ret.append(',\n    dtotdp : ')
        ret.append(repr(self.dtotdp))
        ret.append(',\n    totsb : ')
        ret.append(repr(self.totsb))
        ret.append(',\n    totcinc : ')
        ret.append(repr(self.totcinc))
        ret.append(',\n    dtota : ')
        ret.append(repr(self.dtota))
        ret.append(',\n    alc : ')
        ret.append(repr(self.alc))
        ret.append(',\n    blc : ')
        ret.append(repr(self.blc))
        ret.append(',\n    conct : ')
        ret.append(repr(self.conct))
        ret.append(',\n    gammat : ')
        ret.append(repr(self.gammat))
        ret.append(',\n    depth_dependence : ')
        ret.append(repr(self.depth_dependence))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

chem = Chem()

class Dgml(f90wrap.runtime.FortranModule):
    """
    Module dgml
    
    
    Defined at ../src/dgml.f lines 1-43
    
    """
    @property
    def dgm(self):
        """
        Element dgm ftype=logical pytype=bool
        
        
        Defined at ../src/dgml.f line 41
        
        """
        return _min3p.f90wrap_dgml__get__dgm()
    
    @dgm.setter
    def dgm(self, dgm):
        _min3p.f90wrap_dgml__set__dgm(dgm)
    
    @property
    def maxwell(self):
        """
        Element maxwell ftype=logical pytype=bool
        
        
        Defined at ../src/dgml.f line 42
        
        """
        return _min3p.f90wrap_dgml__get__maxwell()
    
    @maxwell.setter
    def maxwell(self, maxwell):
        _min3p.f90wrap_dgml__set__maxwell(maxwell)
    
    @property
    def equimolar(self):
        """
        Element equimolar ftype=logical pytype=bool
        
        
        Defined at ../src/dgml.f line 43
        
        """
        return _min3p.f90wrap_dgml__get__equimolar()
    
    @equimolar.setter
    def equimolar(self, equimolar):
        _min3p.f90wrap_dgml__set__equimolar(equimolar)
    
    def __str__(self):
        ret = ['<dgml>{\n']
        ret.append('    dgm : ')
        ret.append(repr(self.dgm))
        ret.append(',\n    maxwell : ')
        ret.append(repr(self.maxwell))
        ret.append(',\n    equimolar : ')
        ret.append(repr(self.equimolar))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

dgml = Dgml()

class Dual(f90wrap.runtime.FortranModule):
    """
    Module dual
    
    
    Defined at ../src/dual.f lines 1-56
    
    """
    @property
    def idual_type(self):
        """
        Element idual_type ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/dual.f line 34
        
        """
        return _min3p.f90wrap_dual__get__idual_type()
    
    @idual_type.setter
    def idual_type(self, idual_type):
        _min3p.f90wrap_dual__set__idual_type(idual_type)
    
    @property
    def dual_perm(self):
        """
        Element dual_perm ftype=logical pytype=bool
        
        
        Defined at ../src/dual.f line 37
        
        """
        return _min3p.f90wrap_dual__get__dual_perm()
    
    @dual_perm.setter
    def dual_perm(self, dual_perm):
        _min3p.f90wrap_dual__set__dual_perm(dual_perm)
    
    @property
    def dual_perm1(self):
        """
        Element dual_perm1 ftype=logical pytype=bool
        
        
        Defined at ../src/dual.f line 38
        
        """
        return _min3p.f90wrap_dual__get__dual_perm1()
    
    @dual_perm1.setter
    def dual_perm1(self, dual_perm1):
        _min3p.f90wrap_dual__set__dual_perm1(dual_perm1)
    
    @property
    def dual_perm2(self):
        """
        Element dual_perm2 ftype=logical pytype=bool
        
        
        Defined at ../src/dual.f line 39
        
        """
        return _min3p.f90wrap_dual__get__dual_perm2()
    
    @dual_perm2.setter
    def dual_perm2(self, dual_perm2):
        _min3p.f90wrap_dual__set__dual_perm2(dual_perm2)
    
    @property
    def cpuint(self):
        """
        Element cpuint ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 41
        
        """
        return _min3p.f90wrap_dual__get__cpuint()
    
    @cpuint.setter
    def cpuint(self, cpuint):
        _min3p.f90wrap_dual__set__cpuint(cpuint)
    
    @property
    def csec(self):
        """
        Element csec ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 42
        
        """
        return _min3p.f90wrap_dual__get__csec()
    
    @csec.setter
    def csec(self, csec):
        _min3p.f90wrap_dual__set__csec(csec)
    
    @property
    def rkinter (self):
        """
        Element rkinter  ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 44
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__rkinter (f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rkinter  = self._arrays[array_handle]
        else:
            rkinter = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__rkinter )
            self._arrays[array_handle] = rkinter 
        return rkinter
    
    @rkinter .setter
    def rkinter (self, rkinter ):
        self.rkinter [...] = rkinter
    
    @property
    def dualhcrit(self):
        """
        Element dualhcrit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 46
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__dualhcrit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dualhcrit = self._arrays[array_handle]
        else:
            dualhcrit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__dualhcrit)
            self._arrays[array_handle] = dualhcrit
        return dualhcrit
    
    @dualhcrit.setter
    def dualhcrit(self, dualhcrit):
        self.dualhcrit[...] = dualhcrit
    
    @property
    def satwcrit(self):
        """
        Element satwcrit ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 48
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__satwcrit(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwcrit = self._arrays[array_handle]
        else:
            satwcrit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__satwcrit)
            self._arrays[array_handle] = satwcrit
        return satwcrit
    
    @satwcrit.setter
    def satwcrit(self, satwcrit):
        self.satwcrit[...] = satwcrit
    
    @property
    def dualmag(self):
        """
        Element dualmag ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 49
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__dualmag(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dualmag = self._arrays[array_handle]
        else:
            dualmag = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__dualmag)
            self._arrays[array_handle] = dualmag
        return dualmag
    
    @dualmag.setter
    def dualmag(self, dualmag):
        self.dualmag[...] = dualmag
    
    @property
    def wf (self):
        """
        Element wf  ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/dual.f line 51
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__wf (f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            wf  = self._arrays[array_handle]
        else:
            wf  = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__wf )
            self._arrays[array_handle] = wf 
        return wf
    
    @wf .setter
    def wf (self, wf ):
        self.wf [...] = wf
    
    @property
    def mat(self):
        """
        Element mat ftype=logical pytype=bool
        
        
        Defined at ../src/dual.f line 53
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_dual__array__mat(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            mat = self._arrays[array_handle]
        else:
            mat = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_dual__array__mat)
            self._arrays[array_handle] = mat
        return mat
    
    @mat.setter
    def mat(self, mat):
        self.mat[...] = mat
    
    def __str__(self):
        ret = ['<dual>{\n']
        ret.append('    idual_type : ')
        ret.append(repr(self.idual_type))
        ret.append(',\n    dual_perm : ')
        ret.append(repr(self.dual_perm))
        ret.append(',\n    dual_perm1 : ')
        ret.append(repr(self.dual_perm1))
        ret.append(',\n    dual_perm2 : ')
        ret.append(repr(self.dual_perm2))
        ret.append(',\n    cpuint : ')
        ret.append(repr(self.cpuint))
        ret.append(',\n    csec : ')
        ret.append(repr(self.csec))
        ret.append(',\n    rkinter  : ')
        ret.append(repr(self.rkinter ))
        ret.append(',\n    dualhcrit : ')
        ret.append(repr(self.dualhcrit))
        ret.append(',\n    satwcrit : ')
        ret.append(repr(self.satwcrit))
        ret.append(',\n    dualmag : ')
        ret.append(repr(self.dualmag))
        ret.append(',\n    wf  : ')
        ret.append(repr(self.wf ))
        ret.append(',\n    mat : ')
        ret.append(repr(self.mat))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

dual = Dual()

class Gen(f90wrap.runtime.FortranModule):
    """
    Module gen
    
    
    Defined at ../src/gen.f lines 1-1620
    
    """
    @property
    def cpuint(self):
        """
        Element cpuint ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 58
        
        """
        return _min3p.f90wrap_gen__get__cpuint()
    
    @cpuint.setter
    def cpuint(self, cpuint):
        _min3p.f90wrap_gen__set__cpuint(cpuint)
    
    @property
    def csec(self):
        """
        Element csec ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 59
        
        """
        return _min3p.f90wrap_gen__get__csec()
    
    @csec.setter
    def csec(self, csec):
        _min3p.f90wrap_gen__set__csec(csec)
    
    @property
    def varsat_flow(self):
        """
        Element varsat_flow ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 61
        
        """
        return _min3p.f90wrap_gen__get__varsat_flow()
    
    @varsat_flow.setter
    def varsat_flow(self, varsat_flow):
        _min3p.f90wrap_gen__set__varsat_flow(varsat_flow)
    
    @property
    def steady_flow(self):
        """
        Element steady_flow ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 62
        
        """
        return _min3p.f90wrap_gen__get__steady_flow()
    
    @steady_flow.setter
    def steady_flow(self, steady_flow):
        _min3p.f90wrap_gen__set__steady_flow(steady_flow)
    
    @property
    def transient_flow(self):
        """
        Element transient_flow ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 63
        
        """
        return _min3p.f90wrap_gen__get__transient_flow()
    
    @transient_flow.setter
    def transient_flow(self, transient_flow):
        _min3p.f90wrap_gen__set__transient_flow(transient_flow)
    
    @property
    def not_converged(self):
        """
        Element not_converged ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 64
        
        """
        return _min3p.f90wrap_gen__get__not_converged()
    
    @not_converged.setter
    def not_converged(self, not_converged):
        _min3p.f90wrap_gen__set__not_converged(not_converged)
    
    @property
    def full_path(self):
        """
        Element full_path ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 65
        
        """
        return _min3p.f90wrap_gen__get__full_path()
    
    @full_path.setter
    def full_path(self, full_path):
        _min3p.f90wrap_gen__set__full_path(full_path)
    
    @property
    def fully_saturated(self):
        """
        Element fully_saturated ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 66
        
        """
        return _min3p.f90wrap_gen__get__fully_saturated()
    
    @fully_saturated.setter
    def fully_saturated(self, fully_saturated):
        _min3p.f90wrap_gen__set__fully_saturated(fully_saturated)
    
    @property
    def variably_saturated(self):
        """
        Element variably_saturated ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 67
        
        """
        return _min3p.f90wrap_gen__get__variably_saturated()
    
    @variably_saturated.setter
    def variably_saturated(self, variably_saturated):
        _min3p.f90wrap_gen__set__variably_saturated(variably_saturated)
    
    @property
    def geo_chemistry(self):
        """
        Element geo_chemistry ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 68
        
        """
        return _min3p.f90wrap_gen__get__geo_chemistry()
    
    @geo_chemistry.setter
    def geo_chemistry(self, geo_chemistry):
        _min3p.f90wrap_gen__set__geo_chemistry(geo_chemistry)
    
    @property
    def reactive_transport(self):
        """
        Element reactive_transport ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 69
        
        """
        return _min3p.f90wrap_gen__get__reactive_transport()
    
    @reactive_transport.setter
    def reactive_transport(self, reactive_transport):
        _min3p.f90wrap_gen__set__reactive_transport(reactive_transport)
    
    @property
    def show_module(self):
        """
        Element show_module ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 70
        
        """
        return _min3p.f90wrap_gen__get__show_module()
    
    @show_module.setter
    def show_module(self, show_module):
        _min3p.f90wrap_gen__set__show_module(show_module)
    
    @property
    def log_file(self):
        """
        Element log_file ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 71
        
        """
        return _min3p.f90wrap_gen__get__log_file()
    
    @log_file.setter
    def log_file(self, log_file):
        _min3p.f90wrap_gen__set__log_file(log_file)
    
    @property
    def depth_output(self):
        """
        Element depth_output ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 72
        
        """
        return _min3p.f90wrap_gen__get__depth_output()
    
    @depth_output.setter
    def depth_output(self, depth_output):
        _min3p.f90wrap_gen__set__depth_output(depth_output)
    
    @property
    def update_porosity(self):
        """
        Element update_porosity ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 73
        
        """
        return _min3p.f90wrap_gen__get__update_porosity()
    
    @update_porosity.setter
    def update_porosity(self, update_porosity):
        _min3p.f90wrap_gen__set__update_porosity(update_porosity)
    
    @property
    def update_permeability(self):
        """
        Element update_permeability ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 74
        
        """
        return _min3p.f90wrap_gen__get__update_permeability()
    
    @update_permeability.setter
    def update_permeability(self, update_permeability):
        _min3p.f90wrap_gen__set__update_permeability(update_permeability)
    
    @property
    def pure_evap(self):
        """
        Element pure_evap ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 75
        
        """
        return _min3p.f90wrap_gen__get__pure_evap()
    
    @pure_evap.setter
    def pure_evap(self, pure_evap):
        _min3p.f90wrap_gen__set__pure_evap(pure_evap)
    
    @property
    def sec_per_days(self):
        """
        Element sec_per_days ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 93
        
        """
        return _min3p.f90wrap_gen__get__sec_per_days()
    
    @sec_per_days.setter
    def sec_per_days(self, sec_per_days):
        _min3p.f90wrap_gen__set__sec_per_days(sec_per_days)
    
    @property
    def gacc(self):
        """
        Element gacc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 94
        
        """
        return _min3p.f90wrap_gen__get__gacc()
    
    @gacc.setter
    def gacc(self, gacc):
        _min3p.f90wrap_gen__set__gacc(gacc)
    
    @property
    def xg(self):
        """
        Element xg ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 153
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__xg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xg = self._arrays[array_handle]
        else:
            xg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__xg)
            self._arrays[array_handle] = xg
        return xg
    
    @xg.setter
    def xg(self, xg):
        self.xg[...] = xg
    
    @property
    def yg(self):
        """
        Element yg ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 154
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__yg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            yg = self._arrays[array_handle]
        else:
            yg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__yg)
            self._arrays[array_handle] = yg
        return yg
    
    @yg.setter
    def yg(self, yg):
        self.yg[...] = yg
    
    @property
    def zg(self):
        """
        Element zg ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 155
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__zg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            zg = self._arrays[array_handle]
        else:
            zg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__zg)
            self._arrays[array_handle] = zg
        return zg
    
    @zg.setter
    def zg(self, zg):
        self.zg[...] = zg
    
    @property
    def dimcv(self):
        """
        Element dimcv ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 157
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dimcv(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dimcv = self._arrays[array_handle]
        else:
            dimcv = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dimcv)
            self._arrays[array_handle] = dimcv
        return dimcv
    
    @dimcv.setter
    def dimcv(self, dimcv):
        self.dimcv[...] = dimcv
    
    @property
    def cvol(self):
        """
        Element cvol ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 158
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cvol(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cvol = self._arrays[array_handle]
        else:
            cvol = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cvol)
            self._arrays[array_handle] = cvol
        return cvol
    
    @cvol.setter
    def cvol(self, cvol):
        self.cvol[...] = cvol
    
    @property
    def delx(self):
        """
        Element delx ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 160
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__delx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            delx = self._arrays[array_handle]
        else:
            delx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__delx)
            self._arrays[array_handle] = delx
        return delx
    
    @delx.setter
    def delx(self, delx):
        self.delx[...] = delx
    
    @property
    def dely(self):
        """
        Element dely ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 161
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dely(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dely = self._arrays[array_handle]
        else:
            dely = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dely)
            self._arrays[array_handle] = dely
        return dely
    
    @dely.setter
    def dely(self, dely):
        self.dely[...] = dely
    
    @property
    def delz(self):
        """
        Element delz ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 162
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__delz(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            delz = self._arrays[array_handle]
        else:
            delz = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__delz)
            self._arrays[array_handle] = delz
        return delz
    
    @delz.setter
    def delz(self, delz):
        self.delz[...] = delz
    
    @property
    def xmax(self):
        """
        Element xmax ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 163
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__xmax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xmax = self._arrays[array_handle]
        else:
            xmax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__xmax)
            self._arrays[array_handle] = xmax
        return xmax
    
    @xmax.setter
    def xmax(self, xmax):
        self.xmax[...] = xmax
    
    @property
    def xmin(self):
        """
        Element xmin ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 164
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__xmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            xmin = self._arrays[array_handle]
        else:
            xmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__xmin)
            self._arrays[array_handle] = xmin
        return xmin
    
    @xmin.setter
    def xmin(self, xmin):
        self.xmin[...] = xmin
    
    @property
    def ymax(self):
        """
        Element ymax ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 165
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ymax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ymax = self._arrays[array_handle]
        else:
            ymax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ymax)
            self._arrays[array_handle] = ymax
        return ymax
    
    @ymax.setter
    def ymax(self, ymax):
        self.ymax[...] = ymax
    
    @property
    def ymin(self):
        """
        Element ymin ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 166
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ymin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ymin = self._arrays[array_handle]
        else:
            ymin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ymin)
            self._arrays[array_handle] = ymin
        return ymin
    
    @ymin.setter
    def ymin(self, ymin):
        self.ymin[...] = ymin
    
    @property
    def zmax(self):
        """
        Element zmax ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 167
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__zmax(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            zmax = self._arrays[array_handle]
        else:
            zmax = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__zmax)
            self._arrays[array_handle] = zmax
        return zmax
    
    @zmax.setter
    def zmax(self, zmax):
        self.zmax[...] = zmax
    
    @property
    def zmin(self):
        """
        Element zmin ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 168
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__zmin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            zmin = self._arrays[array_handle]
        else:
            zmin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__zmin)
            self._arrays[array_handle] = zmin
        return zmin
    
    @zmin.setter
    def zmin(self, zmin):
        self.zmin[...] = zmin
    
    @property
    def elevmax(self):
        """
        Element elevmax ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 170
        
        """
        return _min3p.f90wrap_gen__get__elevmax()
    
    @elevmax.setter
    def elevmax(self, elevmax):
        _min3p.f90wrap_gen__set__elevmax(elevmax)
    
    @property
    def toparea(self):
        """
        Element toparea ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 171
        
        """
        return _min3p.f90wrap_gen__get__toparea()
    
    @toparea.setter
    def toparea(self, toparea):
        _min3p.f90wrap_gen__set__toparea(toparea)
    
    @property
    def nvix(self):
        """
        Element nvix ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 173
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__nvix(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            nvix = self._arrays[array_handle]
        else:
            nvix = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__nvix)
            self._arrays[array_handle] = nvix
        return nvix
    
    @nvix.setter
    def nvix(self, nvix):
        self.nvix[...] = nvix
    
    @property
    def nviy(self):
        """
        Element nviy ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 174
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__nviy(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            nviy = self._arrays[array_handle]
        else:
            nviy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__nviy)
            self._arrays[array_handle] = nviy
        return nviy
    
    @nviy.setter
    def nviy(self, nviy):
        self.nviy[...] = nviy
    
    @property
    def nviz(self):
        """
        Element nviz ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 175
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__nviz(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            nviz = self._arrays[array_handle]
        else:
            nviz = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__nviz)
            self._arrays[array_handle] = nviz
        return nviz
    
    @nviz.setter
    def nviz(self, nviz):
        self.nviz[...] = nviz
    
    @property
    def nxx(self):
        """
        Element nxx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 177
        
        """
        return _min3p.f90wrap_gen__get__nxx()
    
    @nxx.setter
    def nxx(self, nxx):
        _min3p.f90wrap_gen__set__nxx(nxx)
    
    @property
    def nyy(self):
        """
        Element nyy ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 178
        
        """
        return _min3p.f90wrap_gen__get__nyy()
    
    @nyy.setter
    def nyy(self, nyy):
        _min3p.f90wrap_gen__set__nyy(nyy)
    
    @property
    def nzz(self):
        """
        Element nzz ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 179
        
        """
        return _min3p.f90wrap_gen__get__nzz()
    
    @nzz.setter
    def nzz(self, nzz):
        _min3p.f90wrap_gen__set__nzz(nzz)
    
    @property
    def nvx(self):
        """
        Element nvx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 180
        
        """
        return _min3p.f90wrap_gen__get__nvx()
    
    @nvx.setter
    def nvx(self, nvx):
        _min3p.f90wrap_gen__set__nvx(nvx)
    
    @property
    def nvy(self):
        """
        Element nvy ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 181
        
        """
        return _min3p.f90wrap_gen__get__nvy()
    
    @nvy.setter
    def nvy(self, nvy):
        _min3p.f90wrap_gen__set__nvy(nvy)
    
    @property
    def nvz(self):
        """
        Element nvz ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 182
        
        """
        return _min3p.f90wrap_gen__get__nvz()
    
    @nvz.setter
    def nvz(self, nvz):
        _min3p.f90wrap_gen__set__nvz(nvz)
    
    @property
    def nn(self):
        """
        Element nn ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 183
        
        """
        return _min3p.f90wrap_gen__get__nn()
    
    @nn.setter
    def nn(self, nn):
        _min3p.f90wrap_gen__set__nn(nn)
    
    @property
    def half_cells(self):
        """
        Element half_cells ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 185
        
        """
        return _min3p.f90wrap_gen__get__half_cells()
    
    @half_cells.setter
    def half_cells(self, half_cells):
        _min3p.f90wrap_gen__set__half_cells(half_cells)
    
    @property
    def delta_c(self):
        """
        Element delta_c ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 230
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__delta_c(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            delta_c = self._arrays[array_handle]
        else:
            delta_c = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__delta_c)
            self._arrays[array_handle] = delta_c
        return delta_c
    
    @delta_c.setter
    def delta_c(self, delta_c):
        self.delta_c[...] = delta_c
    
    @property
    def delta_c_max(self):
        """
        Element delta_c_max ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 231
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__delta_c_max(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            delta_c_max = self._arrays[array_handle]
        else:
            delta_c_max = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__delta_c_max)
            self._arrays[array_handle] = delta_c_max
        return delta_c_max
    
    @delta_c_max.setter
    def delta_c_max(self, delta_c_max):
        self.delta_c_max[...] = delta_c_max
    
    @property
    def time(self):
        """
        Element time ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 233
        
        """
        return _min3p.f90wrap_gen__get__time()
    
    @time.setter
    def time(self, time):
        _min3p.f90wrap_gen__set__time(time)
    
    @property
    def time_io(self):
        """
        Element time_io ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 235
        
        """
        return _min3p.f90wrap_gen__get__time_io()
    
    @time_io.setter
    def time_io(self, time_io):
        _min3p.f90wrap_gen__set__time_io(time_io)
    
    @property
    def time_io_bis(self):
        """
        Element time_io_bis ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/gen.f line 236
        
        """
        return _min3p.f90wrap_gen__get__time_io_bis()
    
    @time_io_bis.setter
    def time_io_bis(self, time_io_bis):
        _min3p.f90wrap_gen__set__time_io_bis(time_io_bis)
    
    @property
    def time_io_prec(self):
        """
        Element time_io_prec ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 238
        
        """
        return _min3p.f90wrap_gen__get__time_io_prec()
    
    @time_io_prec.setter
    def time_io_prec(self, time_io_prec):
        _min3p.f90wrap_gen__set__time_io_prec(time_io_prec)
    
    @property
    def time_factor(self):
        """
        Element time_factor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 241
        
        """
        return _min3p.f90wrap_gen__get__time_factor()
    
    @time_factor.setter
    def time_factor(self, time_factor):
        _min3p.f90wrap_gen__set__time_factor(time_factor)
    
    @property
    def tfinal(self):
        """
        Element tfinal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 243
        
        """
        return _min3p.f90wrap_gen__get__tfinal()
    
    @tfinal.setter
    def tfinal(self, tfinal):
        _min3p.f90wrap_gen__set__tfinal(tfinal)
    
    @property
    def tfinal_bis(self):
        """
        Element tfinal_bis ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 244
        
        """
        return _min3p.f90wrap_gen__get__tfinal_bis()
    
    @tfinal_bis.setter
    def tfinal_bis(self, tfinal_bis):
        _min3p.f90wrap_gen__set__tfinal_bis(tfinal_bis)
    
    @property
    def delt(self):
        """
        Element delt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 246
        
        """
        return _min3p.f90wrap_gen__get__delt()
    
    @delt.setter
    def delt(self, delt):
        _min3p.f90wrap_gen__set__delt(delt)
    
    @property
    def delt_io(self):
        """
        Element delt_io ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 247
        
        """
        return _min3p.f90wrap_gen__get__delt_io()
    
    @delt_io.setter
    def delt_io(self, delt_io):
        _min3p.f90wrap_gen__set__delt_io(delt_io)
    
    @property
    def delt_vs(self):
        """
        Element delt_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 248
        
        """
        return _min3p.f90wrap_gen__get__delt_vs()
    
    @delt_vs.setter
    def delt_vs(self, delt_vs):
        _min3p.f90wrap_gen__set__delt_vs(delt_vs)
    
    @property
    def delt_rt(self):
        """
        Element delt_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 249
        
        """
        return _min3p.f90wrap_gen__get__delt_rt()
    
    @delt_rt.setter
    def delt_rt(self, delt_rt):
        _min3p.f90wrap_gen__set__delt_rt(delt_rt)
    
    @property
    def deltmin(self):
        """
        Element deltmin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 250
        
        """
        return _min3p.f90wrap_gen__get__deltmin()
    
    @deltmin.setter
    def deltmin(self, deltmin):
        _min3p.f90wrap_gen__set__deltmin(deltmin)
    
    @property
    def deltmax(self):
        """
        Element deltmax ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 251
        
        """
        return _min3p.f90wrap_gen__get__deltmax()
    
    @deltmax.setter
    def deltmax(self, deltmax):
        _min3p.f90wrap_gen__set__deltmax(deltmax)
    
    @property
    def urtant_log(self):
        """
        Element urtant_log ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 252
        
        """
        return _min3p.f90wrap_gen__get__urtant_log()
    
    @urtant_log.setter
    def urtant_log(self, urtant_log):
        _min3p.f90wrap_gen__set__urtant_log(urtant_log)
    
    @property
    def l_time_unit(self):
        """
        Element l_time_unit ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 254
        
        """
        return _min3p.f90wrap_gen__get__l_time_unit()
    
    @l_time_unit.setter
    def l_time_unit(self, l_time_unit):
        _min3p.f90wrap_gen__set__l_time_unit(l_time_unit)
    
    @property
    def mtime(self):
        """
        Element mtime ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 255
        
        """
        return _min3p.f90wrap_gen__get__mtime()
    
    @mtime.setter
    def mtime(self, mtime):
        _min3p.f90wrap_gen__set__mtime(mtime)
    
    @property
    def mtime_f(self):
        """
        Element mtime_f ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 256
        
        """
        return _min3p.f90wrap_gen__get__mtime_f()
    
    @mtime_f.setter
    def mtime_f(self, mtime_f):
        _min3p.f90wrap_gen__set__mtime_f(mtime_f)
    
    @property
    def reduce_timestep(self):
        """
        Element reduce_timestep ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 258
        
        """
        return _min3p.f90wrap_gen__get__reduce_timestep()
    
    @reduce_timestep.setter
    def reduce_timestep(self, reduce_timestep):
        _min3p.f90wrap_gen__set__reduce_timestep(reduce_timestep)
    
    @property
    def gs_tout(self):
        """
        Element gs_tout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 457
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gs_tout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gs_tout = self._arrays[array_handle]
        else:
            gs_tout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gs_tout)
            self._arrays[array_handle] = gs_tout
        return gs_tout
    
    @gs_tout.setter
    def gs_tout(self, gs_tout):
        self.gs_tout[...] = gs_tout
    
    @property
    def iamb(self):
        """
        Element iamb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 459
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iamb(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iamb = self._arrays[array_handle]
        else:
            iamb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iamb)
            self._arrays[array_handle] = iamb
        return iamb
    
    @iamb.setter
    def iamb(self, iamb):
        self.iamb[...] = iamb
    
    @property
    def ngb_vol(self):
        """
        Element ngb_vol ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 460
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ngb_vol(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ngb_vol = self._arrays[array_handle]
        else:
            ngb_vol = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ngb_vol)
            self._arrays[array_handle] = ngb_vol
        return ngb_vol
    
    @ngb_vol.setter
    def ngb_vol(self, ngb_vol):
        self.ngb_vol[...] = ngb_vol
    
    @property
    def ngb(self):
        """
        Element ngb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 462
        
        """
        return _min3p.f90wrap_gen__get__ngb()
    
    @ngb.setter
    def ngb(self, ngb):
        _min3p.f90wrap_gen__set__ngb(ngb)
    
    @property
    def ngs(self):
        """
        Element ngs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 462
        
        """
        return _min3p.f90wrap_gen__get__ngs()
    
    @ngs.setter
    def ngs(self, ngs):
        _min3p.f90wrap_gen__set__ngs(ngs)
    
    @property
    def igstime(self):
        """
        Element igstime ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 463
        
        """
        return _min3p.f90wrap_gen__get__igstime()
    
    @igstime.setter
    def igstime(self, igstime):
        _min3p.f90wrap_gen__set__igstime(igstime)
    
    @property
    def ngb_step(self):
        """
        Element ngb_step ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 464
        
        """
        return _min3p.f90wrap_gen__get__ngb_step()
    
    @ngb_step.setter
    def ngb_step(self, ngb_step):
        _min3p.f90wrap_gen__set__ngb_step(ngb_step)
    
    @property
    def nmb(self):
        """
        Element nmb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 465
        
        """
        return _min3p.f90wrap_gen__get__nmb()
    
    @nmb.setter
    def nmb(self, nmb):
        _min3p.f90wrap_gen__set__nmb(nmb)
    
    @property
    def l_prfx(self):
        """
        Element l_prfx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 466
        
        """
        return _min3p.f90wrap_gen__get__l_prfx()
    
    @l_prfx.setter
    def l_prfx(self, l_prfx):
        _min3p.f90wrap_gen__set__l_prfx(l_prfx)
    
    @property
    def l_dbs_dir(self):
        """
        Element l_dbs_dir ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 467
        
        """
        return _min3p.f90wrap_gen__get__l_dbs_dir()
    
    @l_dbs_dir.setter
    def l_dbs_dir(self, l_dbs_dir):
        _min3p.f90wrap_gen__set__l_dbs_dir(l_dbs_dir)
    
    @property
    def idat(self):
        """
        Element idat ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 468
        
        """
        return _min3p.f90wrap_gen__get__idat()
    
    @idat.setter
    def idat(self, idat):
        _min3p.f90wrap_gen__set__idat(idat)
    
    @property
    def igen(self):
        """
        Element igen ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 469
        
        """
        return _min3p.f90wrap_gen__get__igen()
    
    @igen.setter
    def igen(self, igen):
        _min3p.f90wrap_gen__set__igen(igen)
    
    @property
    def ifls(self):
        """
        Element ifls ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 470
        
        """
        return _min3p.f90wrap_gen__get__ifls()
    
    @ifls.setter
    def ifls(self, ifls):
        _min3p.f90wrap_gen__set__ifls(ifls)
    
    @property
    def idbg(self):
        """
        Element idbg ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 471
        
        """
        return _min3p.f90wrap_gen__get__idbg()
    
    @idbg.setter
    def idbg(self, idbg):
        _min3p.f90wrap_gen__set__idbg(idbg)
    
    @property
    def ilog(self):
        """
        Element ilog ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 472
        
        """
        return _min3p.f90wrap_gen__get__ilog()
    
    @ilog.setter
    def ilog(self, ilog):
        _min3p.f90wrap_gen__set__ilog(ilog)
    
    @property
    def idelt(self):
        """
        Element idelt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 473
        
        """
        return _min3p.f90wrap_gen__get__idelt()
    
    @idelt.setter
    def idelt(self, idelt):
        _min3p.f90wrap_gen__set__idelt(idelt)
    
    @property
    def icnv(self):
        """
        Element icnv ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 474
        
        """
        return _min3p.f90wrap_gen__get__icnv()
    
    @icnv.setter
    def icnv(self, icnv):
        _min3p.f90wrap_gen__set__icnv(icnv)
    
    @property
    def ihyc(self):
        """
        Element ihyc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 475
        
        """
        return _min3p.f90wrap_gen__get__ihyc()
    
    @ihyc.setter
    def ihyc(self, ihyc):
        _min3p.f90wrap_gen__set__ihyc(ihyc)
    
    @property
    def itmp(self):
        """
        Element itmp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 476
        
        """
        return _min3p.f90wrap_gen__get__itmp()
    
    @itmp.setter
    def itmp(self, itmp):
        _min3p.f90wrap_gen__set__itmp(itmp)
    
    @property
    def ivel(self):
        """
        Element ivel ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 477
        
        """
        return _min3p.f90wrap_gen__get__ivel()
    
    @ivel.setter
    def ivel(self, ivel):
        _min3p.f90wrap_gen__set__ivel(ivel)
    
    @property
    def icdbs(self):
        """
        Element icdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 478
        
        """
        return _min3p.f90wrap_gen__get__icdbs()
    
    @icdbs.setter
    def icdbs(self, icdbs):
        _min3p.f90wrap_gen__set__icdbs(icdbs)
    
    @property
    def ixdbs(self):
        """
        Element ixdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 479
        
        """
        return _min3p.f90wrap_gen__get__ixdbs()
    
    @ixdbs.setter
    def ixdbs(self, ixdbs):
        _min3p.f90wrap_gen__set__ixdbs(ixdbs)
    
    @property
    def imdbs(self):
        """
        Element imdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 480
        
        """
        return _min3p.f90wrap_gen__get__imdbs()
    
    @imdbs.setter
    def imdbs(self, imdbs):
        _min3p.f90wrap_gen__set__imdbs(imdbs)
    
    @property
    def isdbs(self):
        """
        Element isdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 481
        
        """
        return _min3p.f90wrap_gen__get__isdbs()
    
    @isdbs.setter
    def isdbs(self, isdbs):
        _min3p.f90wrap_gen__set__isdbs(isdbs)
    
    @property
    def irdbs(self):
        """
        Element irdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 482
        
        """
        return _min3p.f90wrap_gen__get__irdbs()
    
    @irdbs.setter
    def irdbs(self, irdbs):
        _min3p.f90wrap_gen__set__irdbs(irdbs)
    
    @property
    def igdbs(self):
        """
        Element igdbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 483
        
        """
        return _min3p.f90wrap_gen__get__igdbs()
    
    @igdbs.setter
    def igdbs(self, igdbs):
        _min3p.f90wrap_gen__set__igdbs(igdbs)
    
    @property
    def imvs(self):
        """
        Element imvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 484
        
        """
        return _min3p.f90wrap_gen__get__imvs()
    
    @imvs.setter
    def imvs(self, imvs):
        _min3p.f90wrap_gen__set__imvs(imvs)
    
    @property
    def imvs_first(self):
        """
        Element imvs_first ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 485
        
        """
        return _min3p.f90wrap_gen__get__imvs_first()
    
    @imvs_first.setter
    def imvs_first(self, imvs_first):
        _min3p.f90wrap_gen__set__imvs_first(imvs_first)
    
    @property
    def imvs_last(self):
        """
        Element imvs_last ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 486
        
        """
        return _min3p.f90wrap_gen__get__imvs_last()
    
    @imvs_last.setter
    def imvs_last(self, imvs_last):
        _min3p.f90wrap_gen__set__imvs_last(imvs_last)
    
    @property
    def imrt(self):
        """
        Element imrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 487
        
        """
        return _min3p.f90wrap_gen__get__imrt()
    
    @imrt.setter
    def imrt(self, imrt):
        _min3p.f90wrap_gen__set__imrt(imrt)
    
    @property
    def imrt_first(self):
        """
        Element imrt_first ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 488
        
        """
        return _min3p.f90wrap_gen__get__imrt_first()
    
    @imrt_first.setter
    def imrt_first(self, imrt_first):
        _min3p.f90wrap_gen__set__imrt_first(imrt_first)
    
    @property
    def imrt_last(self):
        """
        Element imrt_last ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 489
        
        """
        return _min3p.f90wrap_gen__get__imrt_last()
    
    @imrt_last.setter
    def imrt_last(self, imrt_last):
        _min3p.f90wrap_gen__set__imrt_last(imrt_last)
    
    @property
    def igsp(self):
        """
        Element igsp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 490
        
        """
        return _min3p.f90wrap_gen__get__igsp()
    
    @igsp.setter
    def igsp(self, igsp):
        _min3p.f90wrap_gen__set__igsp(igsp)
    
    @property
    def igsb(self):
        """
        Element igsb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 491
        
        """
        return _min3p.f90wrap_gen__get__igsb()
    
    @igsb.setter
    def igsb(self, igsb):
        _min3p.f90wrap_gen__set__igsb(igsb)
    
    @property
    def igsc(self):
        """
        Element igsc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 492
        
        """
        return _min3p.f90wrap_gen__get__igsc()
    
    @igsc.setter
    def igsc(self, igsc):
        _min3p.f90wrap_gen__set__igsc(igsc)
    
    @property
    def igsd(self):
        """
        Element igsd ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 493
        
        """
        return _min3p.f90wrap_gen__get__igsd()
    
    @igsd.setter
    def igsd(self, igsd):
        _min3p.f90wrap_gen__set__igsd(igsd)
    
    @property
    def igsg(self):
        """
        Element igsg ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 494
        
        """
        return _min3p.f90wrap_gen__get__igsg()
    
    @igsg.setter
    def igsg(self, igsg):
        _min3p.f90wrap_gen__set__igsg(igsg)
    
    @property
    def igsgr(self):
        """
        Element igsgr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 495
        
        """
        return _min3p.f90wrap_gen__get__igsgr()
    
    @igsgr.setter
    def igsgr(self, igsgr):
        _min3p.f90wrap_gen__set__igsgr(igsgr)
    
    @property
    def igsm(self):
        """
        Element igsm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 496
        
        """
        return _min3p.f90wrap_gen__get__igsm()
    
    @igsm.setter
    def igsm(self, igsm):
        _min3p.f90wrap_gen__set__igsm(igsm)
    
    @property
    def igsi(self):
        """
        Element igsi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 497
        
        """
        return _min3p.f90wrap_gen__get__igsi()
    
    @igsi.setter
    def igsi(self, igsi):
        _min3p.f90wrap_gen__set__igsi(igsi)
    
    @property
    def igss(self):
        """
        Element igss ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 498
        
        """
        return _min3p.f90wrap_gen__get__igss()
    
    @igss.setter
    def igss(self, igss):
        _min3p.f90wrap_gen__set__igss(igss)
    
    @property
    def igst(self):
        """
        Element igst ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 499
        
        """
        return _min3p.f90wrap_gen__get__igst()
    
    @igst.setter
    def igst(self, igst):
        _min3p.f90wrap_gen__set__igst(igst)
    
    @property
    def igsv(self):
        """
        Element igsv ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 500
        
        """
        return _min3p.f90wrap_gen__get__igsv()
    
    @igsv.setter
    def igsv(self, igsv):
        _min3p.f90wrap_gen__set__igsv(igsv)
    
    @property
    def igsx(self):
        """
        Element igsx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 501
        
        """
        return _min3p.f90wrap_gen__get__igsx()
    
    @igsx.setter
    def igsx(self, igsx):
        _min3p.f90wrap_gen__set__igsx(igsx)
    
    @property
    def igb_start(self):
        """
        Element igb_start ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 502
        
        """
        return _min3p.f90wrap_gen__get__igb_start()
    
    @igb_start.setter
    def igb_start(self, igb_start):
        _min3p.f90wrap_gen__set__igb_start(igb_start)
    
    @property
    def igbb(self):
        """
        Element igbb ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 503
        
        """
        return _min3p.f90wrap_gen__get__igbb()
    
    @igbb.setter
    def igbb(self, igbb):
        _min3p.f90wrap_gen__set__igbb(igbb)
    
    @property
    def igbc(self):
        """
        Element igbc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 504
        
        """
        return _min3p.f90wrap_gen__get__igbc()
    
    @igbc.setter
    def igbc(self, igbc):
        _min3p.f90wrap_gen__set__igbc(igbc)
    
    @property
    def igbd(self):
        """
        Element igbd ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 505
        
        """
        return _min3p.f90wrap_gen__get__igbd()
    
    @igbd.setter
    def igbd(self, igbd):
        _min3p.f90wrap_gen__set__igbd(igbd)
    
    @property
    def igbg(self):
        """
        Element igbg ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 506
        
        """
        return _min3p.f90wrap_gen__get__igbg()
    
    @igbg.setter
    def igbg(self, igbg):
        _min3p.f90wrap_gen__set__igbg(igbg)
    
    @property
    def igbgr(self):
        """
        Element igbgr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 507
        
        """
        return _min3p.f90wrap_gen__get__igbgr()
    
    @igbgr.setter
    def igbgr(self, igbgr):
        _min3p.f90wrap_gen__set__igbgr(igbgr)
    
    @property
    def igbm(self):
        """
        Element igbm ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 508
        
        """
        return _min3p.f90wrap_gen__get__igbm()
    
    @igbm.setter
    def igbm(self, igbm):
        _min3p.f90wrap_gen__set__igbm(igbm)
    
    @property
    def igbp(self):
        """
        Element igbp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 509
        
        """
        return _min3p.f90wrap_gen__get__igbp()
    
    @igbp.setter
    def igbp(self, igbp):
        _min3p.f90wrap_gen__set__igbp(igbp)
    
    @property
    def igbi(self):
        """
        Element igbi ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 510
        
        """
        return _min3p.f90wrap_gen__get__igbi()
    
    @igbi.setter
    def igbi(self, igbi):
        _min3p.f90wrap_gen__set__igbi(igbi)
    
    @property
    def igbs(self):
        """
        Element igbs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 511
        
        """
        return _min3p.f90wrap_gen__get__igbs()
    
    @igbs.setter
    def igbs(self, igbs):
        _min3p.f90wrap_gen__set__igbs(igbs)
    
    @property
    def igbt(self):
        """
        Element igbt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 512
        
        """
        return _min3p.f90wrap_gen__get__igbt()
    
    @igbt.setter
    def igbt(self, igbt):
        _min3p.f90wrap_gen__set__igbt(igbt)
    
    @property
    def igbv(self):
        """
        Element igbv ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 513
        
        """
        return _min3p.f90wrap_gen__get__igbv()
    
    @igbv.setter
    def igbv(self, igbv):
        _min3p.f90wrap_gen__set__igbv(igbv)
    
    @property
    def igbx(self):
        """
        Element igbx ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 514
        
        """
        return _min3p.f90wrap_gen__get__igbx()
    
    @igbx.setter
    def igbx(self, igbx):
        _min3p.f90wrap_gen__set__igbx(igbx)
    
    @property
    def ipsp(self):
        """
        Element ipsp ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 515
        
        """
        return _min3p.f90wrap_gen__get__ipsp()
    
    @ipsp.setter
    def ipsp(self, ipsp):
        _min3p.f90wrap_gen__set__ipsp(ipsp)
    
    @property
    def itec(self):
        """
        Element itec ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 516
        
        """
        return _min3p.f90wrap_gen__get__itec()
    
    @itec.setter
    def itec(self, itec):
        _min3p.f90wrap_gen__set__itec(itec)
    
    @property
    def item(self):
        """
        Element item ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 517
        
        """
        return _min3p.f90wrap_gen__get__item()
    
    @item.setter
    def item(self, item):
        _min3p.f90wrap_gen__set__item(item)
    
    @property
    def jtec(self):
        """
        Element jtec ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 518
        
        """
        return _min3p.f90wrap_gen__get__jtec()
    
    @jtec.setter
    def jtec(self, jtec):
        _min3p.f90wrap_gen__set__jtec(jtec)
    
    @property
    def ktec(self):
        """
        Element ktec ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 519
        
        """
        return _min3p.f90wrap_gen__get__ktec()
    
    @ktec.setter
    def ktec(self, ktec):
        _min3p.f90wrap_gen__set__ktec(ktec)
    
    @property
    def l_zone_name(self):
        """
        Element l_zone_name ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 520
        
        """
        return _min3p.f90wrap_gen__get__l_zone_name()
    
    @l_zone_name.setter
    def l_zone_name(self, l_zone_name):
        _min3p.f90wrap_gen__set__l_zone_name(l_zone_name)
    
    @property
    def igsa(self):
        """
        Element igsa ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 521
        
        """
        return _min3p.f90wrap_gen__get__igsa()
    
    @igsa.setter
    def igsa(self, igsa):
        _min3p.f90wrap_gen__set__igsa(igsa)
    
    @property
    def igsa_first(self):
        """
        Element igsa_first ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 522
        
        """
        return _min3p.f90wrap_gen__get__igsa_first()
    
    @igsa_first.setter
    def igsa_first(self, igsa_first):
        _min3p.f90wrap_gen__set__igsa_first(igsa_first)
    
    @property
    def igsa_last(self):
        """
        Element igsa_last ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 523
        
        """
        return _min3p.f90wrap_gen__get__igsa_last()
    
    @igsa_last.setter
    def igsa_last(self, igsa_last):
        _min3p.f90wrap_gen__set__igsa_last(igsa_last)
    
    @property
    def igs2(self):
        """
        Element igs2 ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 524
        
        """
        return _min3p.f90wrap_gen__get__igs2()
    
    @igs2.setter
    def igs2(self, igs2):
        _min3p.f90wrap_gen__set__igs2(igs2)
    
    @property
    def igsr(self):
        """
        Element igsr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 525
        
        """
        return _min3p.f90wrap_gen__get__igsr()
    
    @igsr.setter
    def igsr(self, igsr):
        _min3p.f90wrap_gen__set__igsr(igsr)
    
    @property
    def igsy(self):
        """
        Element igsy ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 526
        
        """
        return _min3p.f90wrap_gen__get__igsy()
    
    @igsy.setter
    def igsy(self, igsy):
        _min3p.f90wrap_gen__set__igsy(igsy)
    
    @property
    def igsf(self):
        """
        Element igsf ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 527
        
        """
        return _min3p.f90wrap_gen__get__igsf()
    
    @igsf.setter
    def igsf(self, igsf):
        _min3p.f90wrap_gen__set__igsf(igsf)
    
    @property
    def igsf_first(self):
        """
        Element igsf_first ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 528
        
        """
        return _min3p.f90wrap_gen__get__igsf_first()
    
    @igsf_first.setter
    def igsf_first(self, igsf_first):
        _min3p.f90wrap_gen__set__igsf_first(igsf_first)
    
    @property
    def igsf_last(self):
        """
        Element igsf_last ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 529
        
        """
        return _min3p.f90wrap_gen__get__igsf_last()
    
    @igsf_last.setter
    def igsf_last(self, igsf_last):
        _min3p.f90wrap_gen__set__igsf_last(igsf_last)
    
    @property
    def igsk(self):
        """
        Element igsk ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 530
        
        """
        return _min3p.f90wrap_gen__get__igsk()
    
    @igsk.setter
    def igsk(self, igsk):
        _min3p.f90wrap_gen__set__igsk(igsk)
    
    @property
    def igsw(self):
        """
        Element igsw ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 531
        
        """
        return _min3p.f90wrap_gen__get__igsw()
    
    @igsw.setter
    def igsw(self, igsw):
        _min3p.f90wrap_gen__set__igsw(igsw)
    
    @property
    def initial_condition(self):
        """
        Element initial_condition ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 539
        
        """
        return _min3p.f90wrap_gen__get__initial_condition()
    
    @initial_condition.setter
    def initial_condition(self, initial_condition):
        _min3p.f90wrap_gen__set__initial_condition(initial_condition)
    
    @property
    def extended_output(self):
        """
        Element extended_output ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 540
        
        """
        return _min3p.f90wrap_gen__get__extended_output()
    
    @extended_output.setter
    def extended_output(self, extended_output):
        _min3p.f90wrap_gen__set__extended_output(extended_output)
    
    @property
    def gs_output(self):
        """
        Element gs_output ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 541
        
        """
        return _min3p.f90wrap_gen__get__gs_output()
    
    @gs_output.setter
    def gs_output(self, gs_output):
        _min3p.f90wrap_gen__set__gs_output(gs_output)
    
    @property
    def gb_output(self):
        """
        Element gb_output ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 542
        
        """
        return _min3p.f90wrap_gen__get__gb_output()
    
    @gb_output.setter
    def gb_output(self, gb_output):
        _min3p.f90wrap_gen__set__gb_output(gb_output)
    
    @property
    def tec_header(self):
        """
        Element tec_header ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 543
        
        """
        return _min3p.f90wrap_gen__get__tec_header()
    
    @tec_header.setter
    def tec_header(self, tec_header):
        _min3p.f90wrap_gen__set__tec_header(tec_header)
    
    @property
    def dinc_rt(self):
        """
        Element dinc_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 616
        
        """
        return _min3p.f90wrap_gen__get__dinc_rt()
    
    @dinc_rt.setter
    def dinc_rt(self, dinc_rt):
        _min3p.f90wrap_gen__set__dinc_rt(dinc_rt)
    
    @property
    def tol_rt(self):
        """
        Element tol_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 617
        
        """
        return _min3p.f90wrap_gen__get__tol_rt()
    
    @tol_rt.setter
    def tol_rt(self, tol_rt):
        _min3p.f90wrap_gen__set__tol_rt(tol_rt)
    
    @property
    def srelfac_rt(self):
        """
        Element srelfac_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 618
        
        """
        return _min3p.f90wrap_gen__get__srelfac_rt()
    
    @srelfac_rt.setter
    def srelfac_rt(self, srelfac_rt):
        _min3p.f90wrap_gen__set__srelfac_rt(srelfac_rt)
    
    @property
    def n(self):
        """
        Element n ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 620
        
        """
        return _min3p.f90wrap_gen__get__n()
    
    @n.setter
    def n(self, n):
        _min3p.f90wrap_gen__set__n(n)
    
    @property
    def iter_rt(self):
        """
        Element iter_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 621
        
        """
        return _min3p.f90wrap_gen__get__iter_rt()
    
    @iter_rt.setter
    def iter_rt(self, iter_rt):
        _min3p.f90wrap_gen__set__iter_rt(iter_rt)
    
    @property
    def iter_rt_ant(self):
        """
        Element iter_rt_ant ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 622
        
        """
        return _min3p.f90wrap_gen__get__iter_rt_ant()
    
    @iter_rt_ant.setter
    def iter_rt_ant(self, iter_rt_ant):
        _min3p.f90wrap_gen__set__iter_rt_ant(iter_rt_ant)
    
    @property
    def maxit_rt(self):
        """
        Element maxit_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 623
        
        """
        return _min3p.f90wrap_gen__get__maxit_rt()
    
    @maxit_rt.setter
    def maxit_rt(self, maxit_rt):
        _min3p.f90wrap_gen__set__maxit_rt(maxit_rt)
    
    @property
    def itsolvtot_rt(self):
        """
        Element itsolvtot_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 624
        
        """
        return _min3p.f90wrap_gen__get__itsolvtot_rt()
    
    @itsolvtot_rt.setter
    def itsolvtot_rt(self, itsolvtot_rt):
        _min3p.f90wrap_gen__set__itsolvtot_rt(itsolvtot_rt)
    
    @property
    def ittot_rt(self):
        """
        Element ittot_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 625
        
        """
        return _min3p.f90wrap_gen__get__ittot_rt()
    
    @ittot_rt.setter
    def ittot_rt(self, ittot_rt):
        _min3p.f90wrap_gen__set__ittot_rt(ittot_rt)
    
    @property
    def analyt_deriv_rt(self):
        """
        Element analyt_deriv_rt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 627
        
        """
        return _min3p.f90wrap_gen__get__analyt_deriv_rt()
    
    @analyt_deriv_rt.setter
    def analyt_deriv_rt(self, analyt_deriv_rt):
        _min3p.f90wrap_gen__set__analyt_deriv_rt(analyt_deriv_rt)
    
    @property
    def mass_balance_rt(self):
        """
        Element mass_balance_rt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 628
        
        """
        return _min3p.f90wrap_gen__get__mass_balance_rt()
    
    @mass_balance_rt.setter
    def mass_balance_rt(self, mass_balance_rt):
        _min3p.f90wrap_gen__set__mass_balance_rt(mass_balance_rt)
    
    @property
    def sparse_blocks(self):
        """
        Element sparse_blocks ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 629
        
        """
        return _min3p.f90wrap_gen__get__sparse_blocks()
    
    @sparse_blocks.setter
    def sparse_blocks(self, sparse_blocks):
        _min3p.f90wrap_gen__set__sparse_blocks(sparse_blocks)
    
    @property
    def redox_equil_rt(self):
        """
        Element redox_equil_rt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 630
        
        """
        return _min3p.f90wrap_gen__get__redox_equil_rt()
    
    @redox_equil_rt.setter
    def redox_equil_rt(self, redox_equil_rt):
        _min3p.f90wrap_gen__set__redox_equil_rt(redox_equil_rt)
    
    @property
    def under_relax_rt(self):
        """
        Element under_relax_rt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 632
        
        """
        return _min3p.f90wrap_gen__get__under_relax_rt()
    
    @under_relax_rt.setter
    def under_relax_rt(self, under_relax_rt):
        _min3p.f90wrap_gen__set__under_relax_rt(under_relax_rt)
    
    @property
    def gas_advection(self):
        """
        Element gas_advection ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 636
        
        """
        return _min3p.f90wrap_gen__get__gas_advection()
    
    @gas_advection.setter
    def gas_advection(self, gas_advection):
        _min3p.f90wrap_gen__set__gas_advection(gas_advection)
    
    @property
    def cum_molfrac(self):
        """
        Element cum_molfrac ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 637
        
        """
        return _min3p.f90wrap_gen__get__cum_molfrac()
    
    @cum_molfrac.setter
    def cum_molfrac(self, cum_molfrac):
        _min3p.f90wrap_gen__set__cum_molfrac(cum_molfrac)
    
    @property
    def gas_gravity(self):
        """
        Element gas_gravity ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 639
        
        """
        return _min3p.f90wrap_gen__get__gas_gravity()
    
    @gas_gravity.setter
    def gas_gravity(self, gas_gravity):
        _min3p.f90wrap_gen__set__gas_gravity(gas_gravity)
    
    @property
    def update_tortuosity(self):
        """
        Element update_tortuosity ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 647
        
        """
        return _min3p.f90wrap_gen__get__update_tortuosity()
    
    @update_tortuosity.setter
    def update_tortuosity(self, update_tortuosity):
        _min3p.f90wrap_gen__set__update_tortuosity(update_tortuosity)
    
    @property
    def c(self):
        """
        Element c ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 736
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__c(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            c = self._arrays[array_handle]
        else:
            c = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__c)
            self._arrays[array_handle] = c
        return c
    
    @c.setter
    def c(self, c):
        self.c[...] = c
    
    @property
    def cnew(self):
        """
        Element cnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 737
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cnew = self._arrays[array_handle]
        else:
            cnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cnew)
            self._arrays[array_handle] = cnew
        return cnew
    
    @cnew.setter
    def cnew(self, cnew):
        self.cnew[...] = cnew
    
    @property
    def cec_g(self):
        """
        Element cec_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 738
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cec_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cec_g = self._arrays[array_handle]
        else:
            cec_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cec_g)
            self._arrays[array_handle] = cec_g
        return cec_g
    
    @cec_g.setter
    def cec_g(self, cec_g):
        self.cec_g[...] = cec_g
    
    @property
    def gamma(self):
        """
        Element gamma ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 739
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gamma(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gamma = self._arrays[array_handle]
        else:
            gamma = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gamma)
            self._arrays[array_handle] = gamma
        return gamma
    
    @gamma.setter
    def gamma(self, gamma):
        self.gamma[...] = gamma
    
    @property
    def totaold(self):
        """
        Element totaold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 740
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totaold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totaold = self._arrays[array_handle]
        else:
            totaold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totaold)
            self._arrays[array_handle] = totaold
        return totaold
    
    @totaold.setter
    def totaold(self, totaold):
        self.totaold[...] = totaold
    
    @property
    def totanew(self):
        """
        Element totanew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 741
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totanew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totanew = self._arrays[array_handle]
        else:
            totanew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totanew)
            self._arrays[array_handle] = totanew
        return totanew
    
    @totanew.setter
    def totanew(self, totanew):
        self.totanew[...] = totanew
    
    @property
    def totcold(self):
        """
        Element totcold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 742
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcold = self._arrays[array_handle]
        else:
            totcold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcold)
            self._arrays[array_handle] = totcold
        return totcold
    
    @totcold.setter
    def totcold(self, totcold):
        self.totcold[...] = totcold
    
    @property
    def totcnew(self):
        """
        Element totcnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 743
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcnew = self._arrays[array_handle]
        else:
            totcnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcnew)
            self._arrays[array_handle] = totcnew
        return totcnew
    
    @totcnew.setter
    def totcnew(self, totcnew):
        self.totcnew[...] = totcnew
    
    @property
    def totgold(self):
        """
        Element totgold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 744
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgold = self._arrays[array_handle]
        else:
            totgold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgold)
            self._arrays[array_handle] = totgold
        return totgold
    
    @totgold.setter
    def totgold(self, totgold):
        self.totgold[...] = totgold
    
    @property
    def totgnew(self):
        """
        Element totgnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 745
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgnew = self._arrays[array_handle]
        else:
            totgnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgnew)
            self._arrays[array_handle] = totgnew
        return totgnew
    
    @totgnew.setter
    def totgnew(self, totgnew):
        self.totgnew[...] = totgnew
    
    @property
    def totsold(self):
        """
        Element totsold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 746
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totsold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totsold = self._arrays[array_handle]
        else:
            totsold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totsold)
            self._arrays[array_handle] = totsold
        return totsold
    
    @totsold.setter
    def totsold(self, totsold):
        self.totsold[...] = totsold
    
    @property
    def totsnew(self):
        """
        Element totsnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 747
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totsnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totsnew = self._arrays[array_handle]
        else:
            totsnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totsnew)
            self._arrays[array_handle] = totsnew
        return totsnew
    
    @totsnew.setter
    def totsnew(self, totsnew):
        self.totsnew[...] = totsnew
    
    @property
    def cmold(self):
        """
        Element cmold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 748
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmold = self._arrays[array_handle]
        else:
            cmold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmold)
            self._arrays[array_handle] = cmold
        return cmold
    
    @cmold.setter
    def cmold(self, cmold):
        self.cmold[...] = cmold
    
    @property
    def cmnew(self):
        """
        Element cmnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 749
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmnew = self._arrays[array_handle]
        else:
            cmnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmnew)
            self._arrays[array_handle] = cmnew
        return cmnew
    
    @cmnew.setter
    def cmnew(self, cmnew):
        self.cmnew[...] = cmnew
    
    @property
    def distcoff_rt(self):
        """
        Element distcoff_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 750
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__distcoff_rt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            distcoff_rt = self._arrays[array_handle]
        else:
            distcoff_rt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__distcoff_rt)
            self._arrays[array_handle] = distcoff_rt
        return distcoff_rt
    
    @distcoff_rt.setter
    def distcoff_rt(self, distcoff_rt):
        self.distcoff_rt[...] = distcoff_rt
    
    @property
    def ksb2(self):
        """
        Element ksb2 ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 751
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ksb2(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ksb2 = self._arrays[array_handle]
        else:
            ksb2 = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ksb2)
            self._arrays[array_handle] = ksb2
        return ksb2
    
    @ksb2.setter
    def ksb2(self, ksb2):
        self.ksb2[...] = ksb2
    
    @property
    def pdm_rt(self):
        """
        Element pdm_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 753
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__pdm_rt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            pdm_rt = self._arrays[array_handle]
        else:
            pdm_rt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__pdm_rt)
            self._arrays[array_handle] = pdm_rt
        return pdm_rt
    
    @pdm_rt.setter
    def pdm_rt(self, pdm_rt):
        self.pdm_rt[...] = pdm_rt
    
    @property
    def gold(self):
        """
        Element gold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 754
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gold = self._arrays[array_handle]
        else:
            gold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gold)
            self._arrays[array_handle] = gold
        return gold
    
    @gold.setter
    def gold(self, gold):
        self.gold[...] = gold
    
    @property
    def gnew(self):
        """
        Element gnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 755
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gnew = self._arrays[array_handle]
        else:
            gnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gnew)
            self._arrays[array_handle] = gnew
        return gnew
    
    @gnew.setter
    def gnew(self, gnew):
        self.gnew[...] = gnew
    
    @property
    def cx(self):
        """
        Element cx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 756
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cx = self._arrays[array_handle]
        else:
            cx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cx)
            self._arrays[array_handle] = cx
        return cx
    
    @cx.setter
    def cx(self, cx):
        self.cx[...] = cx
    
    @property
    def sionnew(self):
        """
        Element sionnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 757
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sionnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sionnew = self._arrays[array_handle]
        else:
            sionnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sionnew)
            self._arrays[array_handle] = sionnew
        return sionnew
    
    @sionnew.setter
    def sionnew(self, sionnew):
        self.sionnew[...] = sionnew
    
    @property
    def sionold(self):
        """
        Element sionold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 758
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sionold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sionold = self._arrays[array_handle]
        else:
            sionold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sionold)
            self._arrays[array_handle] = sionold
        return sionold
    
    @sionold.setter
    def sionold(self, sionold):
        self.sionold[...] = sionold
    
    @property
    def phi(self):
        """
        Element phi ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 759
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__phi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phi = self._arrays[array_handle]
        else:
            phi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__phi)
            self._arrays[array_handle] = phi
        return phi
    
    @phi.setter
    def phi(self, phi):
        self.phi[...] = phi
    
    @property
    def phiold(self):
        """
        Element phiold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 760
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__phiold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phiold = self._arrays[array_handle]
        else:
            phiold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__phiold)
            self._arrays[array_handle] = phiold
        return phiold
    
    @phiold.setter
    def phiold(self, phiold):
        self.phiold[...] = phiold
    
    @property
    def phi_init(self):
        """
        Element phi_init ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 761
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__phi_init(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            phi_init = self._arrays[array_handle]
        else:
            phi_init = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__phi_init)
            self._arrays[array_handle] = phi_init
        return phi_init
    
    @phi_init.setter
    def phi_init(self, phi_init):
        self.phi_init[...] = phi_init
    
    @property
    def area(self):
        """
        Element area ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 762
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__area(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            area = self._arrays[array_handle]
        else:
            area = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__area)
            self._arrays[array_handle] = area
        return area
    
    @area.setter
    def area(self, area):
        self.area[...] = area
    
    @property
    def cinfrt_va(self):
        """
        Element cinfrt_va ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 763
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfrt_va(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfrt_va = self._arrays[array_handle]
        else:
            cinfrt_va = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfrt_va)
            self._arrays[array_handle] = cinfrt_va
        return cinfrt_va
    
    @cinfrt_va.setter
    def cinfrt_va(self, cinfrt_va):
        self.cinfrt_va[...] = cinfrt_va
    
    @property
    def cinfrt_da(self):
        """
        Element cinfrt_da ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 764
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfrt_da(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfrt_da = self._arrays[array_handle]
        else:
            cinfrt_da = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfrt_da)
            self._arrays[array_handle] = cinfrt_da
        return cinfrt_da
    
    @cinfrt_da.setter
    def cinfrt_da(self, cinfrt_da):
        self.cinfrt_da[...] = cinfrt_da
    
    @property
    def cinfrt_dg(self):
        """
        Element cinfrt_dg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 766
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfrt_dg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfrt_dg = self._arrays[array_handle]
        else:
            cinfrt_dg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfrt_dg)
            self._arrays[array_handle] = cinfrt_dg
        return cinfrt_dg
    
    @cinfrt_dg.setter
    def cinfrt_dg(self, cinfrt_dg):
        self.cinfrt_dg[...] = cinfrt_dg
    
    @property
    def deltaij(self):
        """
        Element deltaij ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 768
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__deltaij(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            deltaij = self._arrays[array_handle]
        else:
            deltaij = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__deltaij)
            self._arrays[array_handle] = deltaij
        return deltaij
    
    @deltaij.setter
    def deltaij(self, deltaij):
        self.deltaij[...] = deltaij
    
    @property
    def tauij(self):
        """
        Element tauij ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 769
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__tauij(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tauij = self._arrays[array_handle]
        else:
            tauij = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__tauij)
            self._arrays[array_handle] = tauij
        return tauij
    
    @tauij.setter
    def tauij(self, tauij):
        self.tauij[...] = tauij
    
    @property
    def gporij(self):
        """
        Element gporij ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 770
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gporij(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gporij = self._arrays[array_handle]
        else:
            gporij = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gporij)
            self._arrays[array_handle] = gporij
        return gporij
    
    @gporij.setter
    def gporij(self, gporij):
        self.gporij[...] = gporij
    
    @property
    def gsatij(self):
        """
        Element gsatij ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 771
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gsatij(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gsatij = self._arrays[array_handle]
        else:
            gsatij = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gsatij)
            self._arrays[array_handle] = gsatij
        return gsatij
    
    @gsatij.setter
    def gsatij(self, gsatij):
        self.gsatij[...] = gsatij
    
    @property
    def tkel(self):
        """
        Element tkel ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 772
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__tkel(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tkel = self._arrays[array_handle]
        else:
            tkel = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__tkel)
            self._arrays[array_handle] = tkel
        return tkel
    
    @tkel.setter
    def tkel(self, tkel):
        self.tkel[...] = tkel
    
    @property
    def gmfrac(self):
        """
        Element gmfrac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 775
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gmfrac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gmfrac = self._arrays[array_handle]
        else:
            gmfrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gmfrac)
            self._arrays[array_handle] = gmfrac
        return gmfrac
    
    @gmfrac.setter
    def gmfrac(self, gmfrac):
        self.gmfrac[...] = gmfrac
    
    @property
    def totgmfrac(self):
        """
        Element totgmfrac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 776
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgmfrac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgmfrac = self._arrays[array_handle]
        else:
            totgmfrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgmfrac)
            self._arrays[array_handle] = totgmfrac
        return totgmfrac
    
    @totgmfrac.setter
    def totgmfrac(self, totgmfrac):
        self.totgmfrac[...] = totgmfrac
    
    @property
    def mpropc(self):
        """
        Element mpropc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 778
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__mpropc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            mpropc = self._arrays[array_handle]
        else:
            mpropc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__mpropc)
            self._arrays[array_handle] = mpropc
        return mpropc
    
    @mpropc.setter
    def mpropc(self, mpropc):
        self.mpropc[...] = mpropc
    
    @property
    def bcondrt_a(self):
        """
        Element bcondrt_a ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 866
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bcondrt_a(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bcondrt_a = self._arrays[array_handle]
        else:
            bcondrt_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bcondrt_a)
            self._arrays[array_handle] = bcondrt_a
        return bcondrt_a
    
    @bcondrt_a.setter
    def bcondrt_a(self, bcondrt_a):
        self.bcondrt_a[...] = bcondrt_a
    
    @property
    def bcondrt_g(self):
        """
        Element bcondrt_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 867
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bcondrt_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bcondrt_g = self._arrays[array_handle]
        else:
            bcondrt_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bcondrt_g)
            self._arrays[array_handle] = bcondrt_g
        return bcondrt_g
    
    @bcondrt_g.setter
    def bcondrt_g(self, bcondrt_g):
        self.bcondrt_g[...] = bcondrt_g
    
    @property
    def bdycrt_d(self):
        """
        Element bdycrt_d ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 868
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bdycrt_d(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bdycrt_d = self._arrays[array_handle]
        else:
            bdycrt_d = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bdycrt_d)
            self._arrays[array_handle] = bdycrt_d
        return bdycrt_d
    
    @bdycrt_d.setter
    def bdycrt_d(self, bdycrt_d):
        self.bdycrt_d[...] = bdycrt_d
    
    @property
    def zgbrt(self):
        """
        Element zgbrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 869
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__zgbrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            zgbrt = self._arrays[array_handle]
        else:
            zgbrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__zgbrt)
            self._arrays[array_handle] = zgbrt
        return zgbrt
    
    @zgbrt.setter
    def zgbrt(self, zgbrt):
        self.zgbrt[...] = zgbrt
    
    @property
    def dijbrt(self):
        """
        Element dijbrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 870
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dijbrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dijbrt = self._arrays[array_handle]
        else:
            dijbrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dijbrt)
            self._arrays[array_handle] = dijbrt
        return dijbrt
    
    @dijbrt.setter
    def dijbrt(self, dijbrt):
        self.dijbrt[...] = dijbrt
    
    @property
    def gbrt(self):
        """
        Element gbrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 871
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gbrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gbrt = self._arrays[array_handle]
        else:
            gbrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gbrt)
            self._arrays[array_handle] = gbrt
        return gbrt
    
    @gbrt.setter
    def gbrt(self, gbrt):
        self.gbrt[...] = gbrt
    
    @property
    def tsrc(self):
        """
        Element tsrc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 872
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__tsrc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tsrc = self._arrays[array_handle]
        else:
            tsrc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__tsrc)
            self._arrays[array_handle] = tsrc
        return tsrc
    
    @tsrc.setter
    def tsrc(self, tsrc):
        self.tsrc[...] = tsrc
    
    @property
    def permbrt(self):
        """
        Element permbrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 873
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__permbrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            permbrt = self._arrays[array_handle]
        else:
            permbrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__permbrt)
            self._arrays[array_handle] = permbrt
        return permbrt
    
    @permbrt.setter
    def permbrt(self, permbrt):
        self.permbrt[...] = permbrt
    
    @property
    def cinfvs_gbrt(self):
        """
        Element cinfvs_gbrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 874
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfvs_gbrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfvs_gbrt = self._arrays[array_handle]
        else:
            cinfvs_gbrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfvs_gbrt)
            self._arrays[array_handle] = cinfvs_gbrt
        return cinfvs_gbrt
    
    @cinfvs_gbrt.setter
    def cinfvs_gbrt(self, cinfvs_gbrt):
        self.cinfvs_gbrt[...] = cinfvs_gbrt
    
    @property
    def iabrt(self):
        """
        Element iabrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 876
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iabrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iabrt = self._arrays[array_handle]
        else:
            iabrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iabrt)
            self._arrays[array_handle] = iabrt
        return iabrt
    
    @iabrt.setter
    def iabrt(self, iabrt):
        self.iabrt[...] = iabrt
    
    @property
    def jabrt(self):
        """
        Element jabrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 877
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jabrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jabrt = self._arrays[array_handle]
        else:
            jabrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jabrt)
            self._arrays[array_handle] = jabrt
        return jabrt
    
    @jabrt.setter
    def jabrt(self, jabrt):
        self.jabrt[...] = jabrt
    
    @property
    def itsrc(self):
        """
        Element itsrc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 879
        
        """
        return _min3p.f90wrap_gen__get__itsrc()
    
    @itsrc.setter
    def itsrc(self, itsrc):
        _min3p.f90wrap_gen__set__itsrc(itsrc)
    
    @property
    def nbrt(self):
        """
        Element nbrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 880
        
        """
        return _min3p.f90wrap_gen__get__nbrt()
    
    @nbrt.setter
    def nbrt(self, nbrt):
        _min3p.f90wrap_gen__set__nbrt(nbrt)
    
    @property
    def nbzrt(self):
        """
        Element nbzrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 881
        
        """
        return _min3p.f90wrap_gen__get__nbzrt()
    
    @nbzrt.setter
    def nbzrt(self, nbzrt):
        _min3p.f90wrap_gen__set__nbzrt(nbzrt)
    
    @property
    def ntsrc(self):
        """
        Element ntsrc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 882
        
        """
        return _min3p.f90wrap_gen__get__ntsrc()
    
    @ntsrc.setter
    def ntsrc(self, ntsrc):
        _min3p.f90wrap_gen__set__ntsrc(ntsrc)
    
    @property
    def spec_conc(self):
        """
        Element spec_conc ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 884
        
        """
        return _min3p.f90wrap_gen__get__spec_conc()
    
    @spec_conc.setter
    def spec_conc(self, spec_conc):
        _min3p.f90wrap_gen__set__spec_conc(spec_conc)
    
    @property
    def transient_source(self):
        """
        Element transient_source ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 885
        
        """
        return _min3p.f90wrap_gen__get__transient_source()
    
    @transient_source.setter
    def transient_source(self, transient_source):
        _min3p.f90wrap_gen__set__transient_source(transient_source)
    
    @property
    def update_bcrt(self):
        """
        Element update_bcrt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 886
        
        """
        return _min3p.f90wrap_gen__get__update_bcrt()
    
    @update_bcrt.setter
    def update_bcrt(self, update_bcrt):
        _min3p.f90wrap_gen__set__update_bcrt(update_bcrt)
    
    @property
    def astor(self):
        """
        Element astor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 926
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__astor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            astor = self._arrays[array_handle]
        else:
            astor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__astor)
            self._arrays[array_handle] = astor
        return astor
    
    @astor.setter
    def astor(self, astor):
        self.astor[...] = astor
    
    @property
    def cflux(self):
        """
        Element cflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 927
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cflux = self._arrays[array_handle]
        else:
            cflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cflux)
            self._arrays[array_handle] = cflux
        return cflux
    
    @cflux.setter
    def cflux(self, cflux):
        self.cflux[...] = cflux
    
    @property
    def cstor(self):
        """
        Element cstor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 928
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cstor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cstor = self._arrays[array_handle]
        else:
            cstor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cstor)
            self._arrays[array_handle] = cstor
        return cstor
    
    @cstor.setter
    def cstor(self, cstor):
        self.cstor[...] = cstor
    
    @property
    def gflux(self):
        """
        Element gflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 929
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gflux = self._arrays[array_handle]
        else:
            gflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gflux)
            self._arrays[array_handle] = gflux
        return gflux
    
    @gflux.setter
    def gflux(self, gflux):
        self.gflux[...] = gflux
    
    @property
    def gstor(self):
        """
        Element gstor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 930
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gstor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gstor = self._arrays[array_handle]
        else:
            gstor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gstor)
            self._arrays[array_handle] = gstor
        return gstor
    
    @gstor.setter
    def gstor(self, gstor):
        self.gstor[...] = gstor
    
    @property
    def dtotcflux(self):
        """
        Element dtotcflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 931
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dtotcflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotcflux = self._arrays[array_handle]
        else:
            dtotcflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dtotcflux)
            self._arrays[array_handle] = dtotcflux
        return dtotcflux
    
    @dtotcflux.setter
    def dtotcflux(self, dtotcflux):
        self.dtotcflux[...] = dtotcflux
    
    @property
    def dtotgflux(self):
        """
        Element dtotgflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 932
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dtotgflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dtotgflux = self._arrays[array_handle]
        else:
            dtotgflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dtotgflux)
            self._arrays[array_handle] = dtotgflux
        return dtotgflux
    
    @dtotgflux.setter
    def dtotgflux(self, dtotgflux):
        self.dtotgflux[...] = dtotgflux
    
    @property
    def ratemdp(self):
        """
        Element ratemdp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 933
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ratemdp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ratemdp = self._arrays[array_handle]
        else:
            ratemdp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ratemdp)
            self._arrays[array_handle] = ratemdp
        return ratemdp
    
    @ratemdp.setter
    def ratemdp(self, ratemdp):
        self.ratemdp[...] = ratemdp
    
    @property
    def totcflux(self):
        """
        Element totcflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 934
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcflux = self._arrays[array_handle]
        else:
            totcflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcflux)
            self._arrays[array_handle] = totcflux
        return totcflux
    
    @totcflux.setter
    def totcflux(self, totcflux):
        self.totcflux[...] = totcflux
    
    @property
    def totgflux(self):
        """
        Element totgflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 935
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgflux = self._arrays[array_handle]
        else:
            totgflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgflux)
            self._arrays[array_handle] = totgflux
        return totgflux
    
    @totgflux.setter
    def totgflux(self, totgflux):
        self.totgflux[...] = totgflux
    
    @property
    def totgaflux(self):
        """
        Element totgaflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 936
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgaflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgaflux = self._arrays[array_handle]
        else:
            totgaflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgaflux)
            self._arrays[array_handle] = totgaflux
        return totgaflux
    
    @totgaflux.setter
    def totgaflux(self, totgaflux):
        self.totgaflux[...] = totgaflux
    
    @property
    def totmdp(self):
        """
        Element totmdp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 937
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totmdp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totmdp = self._arrays[array_handle]
        else:
            totmdp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totmdp)
            self._arrays[array_handle] = totmdp
        return totmdp
    
    @totmdp.setter
    def totmdp(self, totmdp):
        self.totmdp[...] = totmdp
    
    @property
    def i2up(self):
        """
        Element i2up ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 939
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__i2up(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            i2up = self._arrays[array_handle]
        else:
            i2up = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__i2up)
            self._arrays[array_handle] = i2up
        return i2up
    
    @i2up.setter
    def i2up(self, i2up):
        self.i2up[...] = i2up
    
    @property
    def art(self):
        """
        Element art ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1008
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__art(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            art = self._arrays[array_handle]
        else:
            art = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__art)
            self._arrays[array_handle] = art
        return art
    
    @art.setter
    def art(self, art):
        self.art[...] = art
    
    @property
    def brt(self):
        """
        Element brt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1009
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__brt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            brt = self._arrays[array_handle]
        else:
            brt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__brt)
            self._arrays[array_handle] = brt
        return brt
    
    @brt.setter
    def brt(self, brt):
        self.brt[...] = brt
    
    @property
    def urt(self):
        """
        Element urt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1010
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__urt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            urt = self._arrays[array_handle]
        else:
            urt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__urt)
            self._arrays[array_handle] = urt
        return urt
    
    @urt.setter
    def urt(self, urt):
        self.urt[...] = urt
    
    @property
    def resrt(self):
        """
        Element resrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1011
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__resrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            resrt = self._arrays[array_handle]
        else:
            resrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__resrt)
            self._arrays[array_handle] = resrt
        return resrt
    
    @resrt.setter
    def resrt(self, resrt):
        self.resrt[...] = resrt
    
    @property
    def afrt(self):
        """
        Element afrt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1012
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__afrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            afrt = self._arrays[array_handle]
        else:
            afrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__afrt)
            self._arrays[array_handle] = afrt
        return afrt
    
    @afrt.setter
    def afrt(self, afrt):
        self.afrt[...] = afrt
    
    @property
    def restol_rt(self):
        """
        Element restol_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1014
        
        """
        return _min3p.f90wrap_gen__get__restol_rt()
    
    @restol_rt.setter
    def restol_rt(self, restol_rt):
        _min3p.f90wrap_gen__set__restol_rt(restol_rt)
    
    @property
    def deltol_rt(self):
        """
        Element deltol_rt ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1015
        
        """
        return _min3p.f90wrap_gen__get__deltol_rt()
    
    @deltol_rt.setter
    def deltol_rt(self, deltol_rt):
        _min3p.f90wrap_gen__set__deltol_rt(deltol_rt)
    
    @property
    def urtlim_log(self):
        """
        Element urtlim_log ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1016
        
        """
        return _min3p.f90wrap_gen__get__urtlim_log()
    
    @urtlim_log.setter
    def urtlim_log(self, urtlim_log):
        _min3p.f90wrap_gen__set__urtlim_log(urtlim_log)
    
    @property
    def iart(self):
        """
        Element iart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1018
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iart(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iart = self._arrays[array_handle]
        else:
            iart = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iart)
            self._arrays[array_handle] = iart
        return iart
    
    @iart.setter
    def iart(self, iart):
        self.iart[...] = iart
    
    @property
    def jart(self):
        """
        Element jart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1019
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jart(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jart = self._arrays[array_handle]
        else:
            jart = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jart)
            self._arrays[array_handle] = jart
        return jart
    
    @jart.setter
    def jart(self, jart):
        self.jart[...] = jart
    
    @property
    def lart(self):
        """
        Element lart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1020
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__lart(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            lart = self._arrays[array_handle]
        else:
            lart = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__lart)
            self._arrays[array_handle] = lart
        return lart
    
    @lart.setter
    def lart(self, lart):
        self.lart[...] = lart
    
    @property
    def kbl(self):
        """
        Element kbl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1021
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__kbl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            kbl = self._arrays[array_handle]
        else:
            kbl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__kbl)
            self._arrays[array_handle] = kbl
        return kbl
    
    @kbl.setter
    def kbl(self, kbl):
        self.kbl[...] = kbl
    
    @property
    def kart(self):
        """
        Element kart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1022
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__kart(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            kart = self._arrays[array_handle]
        else:
            kart = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__kart)
            self._arrays[array_handle] = kart
        return kart
    
    @kart.setter
    def kart(self, kart):
        self.kart[...] = kart
    
    @property
    def iafrt(self):
        """
        Element iafrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1023
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iafrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iafrt = self._arrays[array_handle]
        else:
            iafrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iafrt)
            self._arrays[array_handle] = iafrt
        return iafrt
    
    @iafrt.setter
    def iafrt(self, iafrt):
        self.iafrt[...] = iafrt
    
    @property
    def jafrt(self):
        """
        Element jafrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1024
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jafrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jafrt = self._arrays[array_handle]
        else:
            jafrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jafrt)
            self._arrays[array_handle] = jafrt
        return jafrt
    
    @jafrt.setter
    def jafrt(self, jafrt):
        self.jafrt[...] = jafrt
    
    @property
    def iafdrt(self):
        """
        Element iafdrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1025
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iafdrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iafdrt = self._arrays[array_handle]
        else:
            iafdrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iafdrt)
            self._arrays[array_handle] = iafdrt
        return iafdrt
    
    @iafdrt.setter
    def iafdrt(self, iafdrt):
        self.iafdrt[...] = iafdrt
    
    @property
    def lorderrt(self):
        """
        Element lorderrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1026
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__lorderrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            lorderrt = self._arrays[array_handle]
        else:
            lorderrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__lorderrt)
            self._arrays[array_handle] = lorderrt
        return lorderrt
    
    @lorderrt.setter
    def lorderrt(self, lorderrt):
        self.lorderrt[...] = lorderrt
    
    @property
    def invordrt(self):
        """
        Element invordrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1027
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__invordrt(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            invordrt = self._arrays[array_handle]
        else:
            invordrt = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__invordrt)
            self._arrays[array_handle] = invordrt
        return invordrt
    
    @invordrt.setter
    def invordrt(self, invordrt):
        self.invordrt[...] = invordrt
    
    @property
    def iadbl(self):
        """
        Element iadbl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1028
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iadbl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iadbl = self._arrays[array_handle]
        else:
            iadbl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iadbl)
            self._arrays[array_handle] = iadbl
        return iadbl
    
    @iadbl.setter
    def iadbl(self, iadbl):
        self.iadbl[...] = iadbl
    
    @property
    def jadbl(self):
        """
        Element jadbl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1029
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jadbl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jadbl = self._arrays[array_handle]
        else:
            jadbl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jadbl)
            self._arrays[array_handle] = jadbl
        return jadbl
    
    @jadbl.setter
    def jadbl(self, jadbl):
        self.jadbl[...] = jadbl
    
    @property
    def kadbl(self):
        """
        Element kadbl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1030
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__kadbl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            kadbl = self._arrays[array_handle]
        else:
            kadbl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__kadbl)
            self._arrays[array_handle] = kadbl
        return kadbl
    
    @kadbl.setter
    def kadbl(self, kadbl):
        self.kadbl[...] = kadbl
    
    @property
    def iaobl(self):
        """
        Element iaobl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1031
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iaobl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iaobl = self._arrays[array_handle]
        else:
            iaobl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iaobl)
            self._arrays[array_handle] = iaobl
        return iaobl
    
    @iaobl.setter
    def iaobl(self, iaobl):
        self.iaobl[...] = iaobl
    
    @property
    def jaobl(self):
        """
        Element jaobl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1032
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jaobl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jaobl = self._arrays[array_handle]
        else:
            jaobl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jaobl)
            self._arrays[array_handle] = jaobl
        return jaobl
    
    @jaobl.setter
    def jaobl(self, jaobl):
        self.jaobl[...] = jaobl
    
    @property
    def kaobl(self):
        """
        Element kaobl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1033
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__kaobl(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            kaobl = self._arrays[array_handle]
        else:
            kaobl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__kaobl)
            self._arrays[array_handle] = kaobl
        return kaobl
    
    @kaobl.setter
    def kaobl(self, kaobl):
        self.kaobl[...] = kaobl
    
    @property
    def mnjart(self):
        """
        Element mnjart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1035
        
        """
        return _min3p.f90wrap_gen__get__mnjart()
    
    @mnjart.setter
    def mnjart(self, mnjart):
        _min3p.f90wrap_gen__set__mnjart(mnjart)
    
    @property
    def mnjafrt(self):
        """
        Element mnjafrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1036
        
        """
        return _min3p.f90wrap_gen__get__mnjafrt()
    
    @mnjafrt.setter
    def mnjafrt(self, mnjafrt):
        _min3p.f90wrap_gen__set__mnjafrt(mnjafrt)
    
    @property
    def njart(self):
        """
        Element njart ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1037
        
        """
        return _min3p.f90wrap_gen__get__njart()
    
    @njart.setter
    def njart(self, njart):
        _min3p.f90wrap_gen__set__njart(njart)
    
    @property
    def njafrt(self):
        """
        Element njafrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1038
        
        """
        return _min3p.f90wrap_gen__get__njafrt()
    
    @njafrt.setter
    def njafrt(self, njafrt):
        _min3p.f90wrap_gen__set__njafrt(njafrt)
    
    @property
    def njadbl(self):
        """
        Element njadbl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1039
        
        """
        return _min3p.f90wrap_gen__get__njadbl()
    
    @njadbl.setter
    def njadbl(self, njadbl):
        _min3p.f90wrap_gen__set__njadbl(njadbl)
    
    @property
    def njaobl(self):
        """
        Element njaobl ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1040
        
        """
        return _min3p.f90wrap_gen__get__njaobl()
    
    @njaobl.setter
    def njaobl(self, njaobl):
        _min3p.f90wrap_gen__set__njaobl(njaobl)
    
    @property
    def level_rt(self):
        """
        Element level_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1041
        
        """
        return _min3p.f90wrap_gen__get__level_rt()
    
    @level_rt.setter
    def level_rt(self, level_rt):
        _min3p.f90wrap_gen__set__level_rt(level_rt)
    
    @property
    def msolvit_rt(self):
        """
        Element msolvit_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1042
        
        """
        return _min3p.f90wrap_gen__get__msolvit_rt()
    
    @msolvit_rt.setter
    def msolvit_rt(self, msolvit_rt):
        _min3p.f90wrap_gen__set__msolvit_rt(msolvit_rt)
    
    @property
    def nexvol_old_rt(self):
        """
        Element nexvol_old_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1043
        
        """
        return _min3p.f90wrap_gen__get__nexvol_old_rt()
    
    @nexvol_old_rt.setter
    def nexvol_old_rt(self, nexvol_old_rt):
        _min3p.f90wrap_gen__set__nexvol_old_rt(nexvol_old_rt)
    
    @property
    def idetail_rt(self):
        """
        Element idetail_rt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1044
        
        """
        return _min3p.f90wrap_gen__get__idetail_rt()
    
    @idetail_rt.setter
    def idetail_rt(self, idetail_rt):
        _min3p.f90wrap_gen__set__idetail_rt(idetail_rt)
    
    @property
    def rcm_ordering_rt(self):
        """
        Element rcm_ordering_rt ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1046
        
        """
        return _min3p.f90wrap_gen__get__rcm_ordering_rt()
    
    @rcm_ordering_rt.setter
    def rcm_ordering_rt(self, rcm_ordering_rt):
        _min3p.f90wrap_gen__set__rcm_ordering_rt(rcm_ordering_rt)
    
    @property
    def cfluxin(self):
        """
        Element cfluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1172
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cfluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cfluxin = self._arrays[array_handle]
        else:
            cfluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cfluxin)
            self._arrays[array_handle] = cfluxin
        return cfluxin
    
    @cfluxin.setter
    def cfluxin(self, cfluxin):
        self.cfluxin[...] = cfluxin
    
    @property
    def cfluxout(self):
        """
        Element cfluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1173
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cfluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cfluxout = self._arrays[array_handle]
        else:
            cfluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cfluxout)
            self._arrays[array_handle] = cfluxout
        return cfluxout
    
    @cfluxout.setter
    def cfluxout(self, cfluxout):
        self.cfluxout[...] = cfluxout
    
    @property
    def gfluxtbdy(self):
        """
        Element gfluxtbdy ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1174
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gfluxtbdy(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfluxtbdy = self._arrays[array_handle]
        else:
            gfluxtbdy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gfluxtbdy)
            self._arrays[array_handle] = gfluxtbdy
        return gfluxtbdy
    
    @gfluxtbdy.setter
    def gfluxtbdy(self, gfluxtbdy):
        self.gfluxtbdy[...] = gfluxtbdy
    
    @property
    def gfluxin(self):
        """
        Element gfluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1175
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gfluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfluxin = self._arrays[array_handle]
        else:
            gfluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gfluxin)
            self._arrays[array_handle] = gfluxin
        return gfluxin
    
    @gfluxin.setter
    def gfluxin(self, gfluxin):
        self.gfluxin[...] = gfluxin
    
    @property
    def gfluxout(self):
        """
        Element gfluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1176
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gfluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gfluxout = self._arrays[array_handle]
        else:
            gfluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gfluxout)
            self._arrays[array_handle] = gfluxout
        return gfluxout
    
    @gfluxout.setter
    def gfluxout(self, gfluxout):
        self.gfluxout[...] = gfluxout
    
    @property
    def gafluxin(self):
        """
        Element gafluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1177
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gafluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gafluxin = self._arrays[array_handle]
        else:
            gafluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gafluxin)
            self._arrays[array_handle] = gafluxin
        return gafluxin
    
    @gafluxin.setter
    def gafluxin(self, gafluxin):
        self.gafluxin[...] = gafluxin
    
    @property
    def gafluxout(self):
        """
        Element gafluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1178
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gafluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gafluxout = self._arrays[array_handle]
        else:
            gafluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gafluxout)
            self._arrays[array_handle] = gafluxout
        return gafluxout
    
    @gafluxout.setter
    def gafluxout(self, gafluxout):
        self.gafluxout[...] = gafluxout
    
    @property
    def cstordiff(self):
        """
        Element cstordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1179
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cstordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cstordiff = self._arrays[array_handle]
        else:
            cstordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cstordiff)
            self._arrays[array_handle] = cstordiff
        return cstordiff
    
    @cstordiff.setter
    def cstordiff(self, cstordiff):
        self.cstordiff[...] = cstordiff
    
    @property
    def gdegas(self):
        """
        Element gdegas ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1180
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gdegas(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gdegas = self._arrays[array_handle]
        else:
            gdegas = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gdegas)
            self._arrays[array_handle] = gdegas
        return gdegas
    
    @gdegas.setter
    def gdegas(self, gdegas):
        self.gdegas[...] = gdegas
    
    @property
    def gstordiff(self):
        """
        Element gstordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1181
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gstordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gstordiff = self._arrays[array_handle]
        else:
            gstordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gstordiff)
            self._arrays[array_handle] = gstordiff
        return gstordiff
    
    @gstordiff.setter
    def gstordiff(self, gstordiff):
        self.gstordiff[...] = gstordiff
    
    @property
    def ordiff(self):
        """
        Element ordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1182
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__ordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            ordiff = self._arrays[array_handle]
        else:
            ordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__ordiff)
            self._arrays[array_handle] = ordiff
        return ordiff
    
    @ordiff.setter
    def ordiff(self, ordiff):
        self.ordiff[...] = ordiff
    
    @property
    def dpdiff(self):
        """
        Element dpdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1183
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dpdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dpdiff = self._arrays[array_handle]
        else:
            dpdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dpdiff)
            self._arrays[array_handle] = dpdiff
        return dpdiff
    
    @dpdiff.setter
    def dpdiff(self, dpdiff):
        self.dpdiff[...] = dpdiff
    
    @property
    def gdiff(self):
        """
        Element gdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1184
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gdiff = self._arrays[array_handle]
        else:
            gdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gdiff)
            self._arrays[array_handle] = gdiff
        return gdiff
    
    @gdiff.setter
    def gdiff(self, gdiff):
        self.gdiff[...] = gdiff
    
    @property
    def amass(self):
        """
        Element amass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1185
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__amass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            amass = self._arrays[array_handle]
        else:
            amass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__amass)
            self._arrays[array_handle] = amass
        return amass
    
    @amass.setter
    def amass(self, amass):
        self.amass[...] = amass
    
    @property
    def tmass(self):
        """
        Element tmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1186
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__tmass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tmass = self._arrays[array_handle]
        else:
            tmass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__tmass)
            self._arrays[array_handle] = tmass
        return tmass
    
    @tmass.setter
    def tmass(self, tmass):
        self.tmass[...] = tmass
    
    @property
    def cmass(self):
        """
        Element cmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1187
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmass = self._arrays[array_handle]
        else:
            cmass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmass)
            self._arrays[array_handle] = cmass
        return cmass
    
    @cmass.setter
    def cmass(self, cmass):
        self.cmass[...] = cmass
    
    @property
    def gmass(self):
        """
        Element gmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1188
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gmass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gmass = self._arrays[array_handle]
        else:
            gmass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gmass)
            self._arrays[array_handle] = gmass
        return gmass
    
    @gmass.setter
    def gmass(self, gmass):
        self.gmass[...] = gmass
    
    @property
    def cmmass(self):
        """
        Element cmmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1189
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmmass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmmass = self._arrays[array_handle]
        else:
            cmmass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmmass)
            self._arrays[array_handle] = cmmass
        return cmmass
    
    @cmmass.setter
    def cmmass(self, cmmass):
        self.cmmass[...] = cmmass
    
    @property
    def csbmass(self):
        """
        Element csbmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1190
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__csbmass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            csbmass = self._arrays[array_handle]
        else:
            csbmass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__csbmass)
            self._arrays[array_handle] = csbmass
        return csbmass
    
    @csbmass.setter
    def csbmass(self, csbmass):
        self.csbmass[...] = csbmass
    
    @property
    def csbmass_c(self):
        """
        Element csbmass_c ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1191
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__csbmass_c(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            csbmass_c = self._arrays[array_handle]
        else:
            csbmass_c = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__csbmass_c)
            self._arrays[array_handle] = csbmass_c
        return csbmass_c
    
    @csbmass_c.setter
    def csbmass_c(self, csbmass_c):
        self.csbmass_c[...] = csbmass_c
    
    @property
    def cculabsbal(self):
        """
        Element cculabsbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1192
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cculabsbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cculabsbal = self._arrays[array_handle]
        else:
            cculabsbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cculabsbal)
            self._arrays[array_handle] = cculabsbal
        return cculabsbal
    
    @cculabsbal.setter
    def cculabsbal(self, cculabsbal):
        self.cculabsbal[...] = cculabsbal
    
    @property
    def cculrelbal(self):
        """
        Element cculrelbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1193
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cculrelbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cculrelbal = self._arrays[array_handle]
        else:
            cculrelbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cculrelbal)
            self._arrays[array_handle] = cculrelbal
        return cculrelbal
    
    @cculrelbal.setter
    def cculrelbal(self, cculrelbal):
        self.cculrelbal[...] = cculrelbal
    
    @property
    def gculabsbal(self):
        """
        Element gculabsbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1194
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gculabsbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gculabsbal = self._arrays[array_handle]
        else:
            gculabsbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gculabsbal)
            self._arrays[array_handle] = gculabsbal
        return gculabsbal
    
    @gculabsbal.setter
    def gculabsbal(self, gculabsbal):
        self.gculabsbal[...] = gculabsbal
    
    @property
    def gculrelbal(self):
        """
        Element gculrelbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1195
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__gculrelbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            gculrelbal = self._arrays[array_handle]
        else:
            gculrelbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__gculrelbal)
            self._arrays[array_handle] = gculrelbal
        return gculrelbal
    
    @gculrelbal.setter
    def gculrelbal(self, gculrelbal):
        self.gculrelbal[...] = gculrelbal
    
    @property
    def cmculabsbal(self):
        """
        Element cmculabsbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1196
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmculabsbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmculabsbal = self._arrays[array_handle]
        else:
            cmculabsbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmculabsbal)
            self._arrays[array_handle] = cmculabsbal
        return cmculabsbal
    
    @cmculabsbal.setter
    def cmculabsbal(self, cmculabsbal):
        self.cmculabsbal[...] = cmculabsbal
    
    @property
    def cmculrelbal(self):
        """
        Element cmculrelbal ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1197
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cmculrelbal(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cmculrelbal = self._arrays[array_handle]
        else:
            cmculrelbal = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cmculrelbal)
            self._arrays[array_handle] = cmculrelbal
        return cmculrelbal
    
    @cmculrelbal.setter
    def cmculrelbal(self, cmculrelbal):
        self.cmculrelbal[...] = cmculrelbal
    
    @property
    def smass(self):
        """
        Element smass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1198
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__smass(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            smass = self._arrays[array_handle]
        else:
            smass = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__smass)
            self._arrays[array_handle] = smass
        return smass
    
    @smass.setter
    def smass(self, smass):
        self.smass[...] = smass
    
    @property
    def sbdiff(self):
        """
        Element sbdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1199
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sbdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sbdiff = self._arrays[array_handle]
        else:
            sbdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sbdiff)
            self._arrays[array_handle] = sbdiff
        return sbdiff
    
    @sbdiff.setter
    def sbdiff(self, sbdiff):
        self.sbdiff[...] = sbdiff
    
    @property
    def rateaqtot(self):
        """
        Element rateaqtot ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1200
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__rateaqtot(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rateaqtot = self._arrays[array_handle]
        else:
            rateaqtot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__rateaqtot)
            self._arrays[array_handle] = rateaqtot
        return rateaqtot
    
    @rateaqtot.setter
    def rateaqtot(self, rateaqtot):
        self.rateaqtot[...] = rateaqtot
    
    @property
    def contaqtot(self):
        """
        Element contaqtot ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1201
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__contaqtot(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            contaqtot = self._arrays[array_handle]
        else:
            contaqtot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__contaqtot)
            self._arrays[array_handle] = contaqtot
        return contaqtot
    
    @contaqtot.setter
    def contaqtot(self, contaqtot):
        self.contaqtot[...] = contaqtot
    
    @property
    def contmintot(self):
        """
        Element contmintot ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1202
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__contmintot(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            contmintot = self._arrays[array_handle]
        else:
            contmintot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__contmintot)
            self._arrays[array_handle] = contmintot
        return contmintot
    
    @contmintot.setter
    def contmintot(self, contmintot):
        self.contmintot[...] = contmintot
    
    @property
    def totcfluxin(self):
        """
        Element totcfluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1203
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcfluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcfluxin = self._arrays[array_handle]
        else:
            totcfluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcfluxin)
            self._arrays[array_handle] = totcfluxin
        return totcfluxin
    
    @totcfluxin.setter
    def totcfluxin(self, totcfluxin):
        self.totcfluxin[...] = totcfluxin
    
    @property
    def totcfluxout(self):
        """
        Element totcfluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1204
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcfluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcfluxout = self._arrays[array_handle]
        else:
            totcfluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcfluxout)
            self._arrays[array_handle] = totcfluxout
        return totcfluxout
    
    @totcfluxout.setter
    def totcfluxout(self, totcfluxout):
        self.totcfluxout[...] = totcfluxout
    
    @property
    def totcstordiff(self):
        """
        Element totcstordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1205
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totcstordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totcstordiff = self._arrays[array_handle]
        else:
            totcstordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totcstordiff)
            self._arrays[array_handle] = totcstordiff
        return totcstordiff
    
    @totcstordiff.setter
    def totcstordiff(self, totcstordiff):
        self.totcstordiff[...] = totcstordiff
    
    @property
    def totordiff(self):
        """
        Element totordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1206
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totordiff = self._arrays[array_handle]
        else:
            totordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totordiff)
            self._arrays[array_handle] = totordiff
        return totordiff
    
    @totordiff.setter
    def totordiff(self, totordiff):
        self.totordiff[...] = totordiff
    
    @property
    def totdpdiff(self):
        """
        Element totdpdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1207
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totdpdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totdpdiff = self._arrays[array_handle]
        else:
            totdpdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totdpdiff)
            self._arrays[array_handle] = totdpdiff
        return totdpdiff
    
    @totdpdiff.setter
    def totdpdiff(self, totdpdiff):
        self.totdpdiff[...] = totdpdiff
    
    @property
    def totgdegas(self):
        """
        Element totgdegas ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1208
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgdegas(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgdegas = self._arrays[array_handle]
        else:
            totgdegas = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgdegas)
            self._arrays[array_handle] = totgdegas
        return totgdegas
    
    @totgdegas.setter
    def totgdegas(self, totgdegas):
        self.totgdegas[...] = totgdegas
    
    @property
    def totgdiff(self):
        """
        Element totgdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1209
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgdiff = self._arrays[array_handle]
        else:
            totgdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgdiff)
            self._arrays[array_handle] = totgdiff
        return totgdiff
    
    @totgdiff.setter
    def totgdiff(self, totgdiff):
        self.totgdiff[...] = totgdiff
    
    @property
    def totgfluxin(self):
        """
        Element totgfluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1210
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgfluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgfluxin = self._arrays[array_handle]
        else:
            totgfluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgfluxin)
            self._arrays[array_handle] = totgfluxin
        return totgfluxin
    
    @totgfluxin.setter
    def totgfluxin(self, totgfluxin):
        self.totgfluxin[...] = totgfluxin
    
    @property
    def totgfluxout(self):
        """
        Element totgfluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1211
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgfluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgfluxout = self._arrays[array_handle]
        else:
            totgfluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgfluxout)
            self._arrays[array_handle] = totgfluxout
        return totgfluxout
    
    @totgfluxout.setter
    def totgfluxout(self, totgfluxout):
        self.totgfluxout[...] = totgfluxout
    
    @property
    def totgafluxin(self):
        """
        Element totgafluxin ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1212
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgafluxin(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgafluxin = self._arrays[array_handle]
        else:
            totgafluxin = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgafluxin)
            self._arrays[array_handle] = totgafluxin
        return totgafluxin
    
    @totgafluxin.setter
    def totgafluxin(self, totgafluxin):
        self.totgafluxin[...] = totgafluxin
    
    @property
    def totgafluxout(self):
        """
        Element totgafluxout ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1213
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgafluxout(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgafluxout = self._arrays[array_handle]
        else:
            totgafluxout = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgafluxout)
            self._arrays[array_handle] = totgafluxout
        return totgafluxout
    
    @totgafluxout.setter
    def totgafluxout(self, totgafluxout):
        self.totgafluxout[...] = totgafluxout
    
    @property
    def totgstordiff(self):
        """
        Element totgstordiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1214
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totgstordiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totgstordiff = self._arrays[array_handle]
        else:
            totgstordiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totgstordiff)
            self._arrays[array_handle] = totgstordiff
        return totgstordiff
    
    @totgstordiff.setter
    def totgstordiff(self, totgstordiff):
        self.totgstordiff[...] = totgstordiff
    
    @property
    def totsbdiff(self):
        """
        Element totsbdiff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1215
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totsbdiff(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totsbdiff = self._arrays[array_handle]
        else:
            totsbdiff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totsbdiff)
            self._arrays[array_handle] = totsbdiff
        return totsbdiff
    
    @totsbdiff.setter
    def totsbdiff(self, totsbdiff):
        self.totsbdiff[...] = totsbdiff
    
    @property
    def dpdiffp(self):
        """
        Element dpdiffp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1216
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dpdiffp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dpdiffp = self._arrays[array_handle]
        else:
            dpdiffp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dpdiffp)
            self._arrays[array_handle] = dpdiffp
        return dpdiffp
    
    @dpdiffp.setter
    def dpdiffp(self, dpdiffp):
        self.dpdiffp[...] = dpdiffp
    
    @property
    def totdpdiffp(self):
        """
        Element totdpdiffp ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1217
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__totdpdiffp(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            totdpdiffp = self._arrays[array_handle]
        else:
            totdpdiffp = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__totdpdiffp)
            self._arrays[array_handle] = totdpdiffp
        return totdpdiffp
    
    @totdpdiffp.setter
    def totdpdiffp(self, totdpdiffp):
        self.totdpdiffp[...] = totdpdiffp
    
    @property
    def sw_star(self):
        """
        Element sw_star ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1257
        
        """
        return _min3p.f90wrap_gen__get__sw_star()
    
    @sw_star.setter
    def sw_star(self, sw_star):
        _min3p.f90wrap_gen__set__sw_star(sw_star)
    
    @property
    def uvslim(self):
        """
        Element uvslim ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1258
        
        """
        return _min3p.f90wrap_gen__get__uvslim()
    
    @uvslim.setter
    def uvslim(self, uvslim):
        _min3p.f90wrap_gen__set__uvslim(uvslim)
    
    @property
    def iter_seep(self):
        """
        Element iter_seep ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1260
        
        """
        return _min3p.f90wrap_gen__get__iter_seep()
    
    @iter_seep.setter
    def iter_seep(self, iter_seep):
        _min3p.f90wrap_gen__set__iter_seep(iter_seep)
    
    @property
    def itseep_tot(self):
        """
        Element itseep_tot ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1261
        
        """
        return _min3p.f90wrap_gen__get__itseep_tot()
    
    @itseep_tot.setter
    def itseep_tot(self, itseep_tot):
        _min3p.f90wrap_gen__set__itseep_tot(itseep_tot)
    
    @property
    def itsolvtot_vs(self):
        """
        Element itsolvtot_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1262
        
        """
        return _min3p.f90wrap_gen__get__itsolvtot_vs()
    
    @itsolvtot_vs.setter
    def itsolvtot_vs(self, itsolvtot_vs):
        _min3p.f90wrap_gen__set__itsolvtot_vs(itsolvtot_vs)
    
    @property
    def nseep_first(self):
        """
        Element nseep_first ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1263
        
        """
        return _min3p.f90wrap_gen__get__nseep_first()
    
    @nseep_first.setter
    def nseep_first(self, nseep_first):
        _min3p.f90wrap_gen__set__nseep_first(nseep_first)
    
    @property
    def pressure_head(self):
        """
        Element pressure_head ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1265
        
        """
        return _min3p.f90wrap_gen__get__pressure_head()
    
    @pressure_head.setter
    def pressure_head(self, pressure_head):
        _min3p.f90wrap_gen__set__pressure_head(pressure_head)
    
    @property
    def hydraulic_head(self):
        """
        Element hydraulic_head ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1266
        
        """
        return _min3p.f90wrap_gen__get__hydraulic_head()
    
    @hydraulic_head.setter
    def hydraulic_head(self, hydraulic_head):
        _min3p.f90wrap_gen__set__hydraulic_head(hydraulic_head)
    
    @property
    def seepage_face(self):
        """
        Element seepage_face ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1267
        
        """
        return _min3p.f90wrap_gen__get__seepage_face()
    
    @seepage_face.setter
    def seepage_face(self, seepage_face):
        _min3p.f90wrap_gen__set__seepage_face(seepage_face)
    
    @property
    def seep_iter(self):
        """
        Element seep_iter ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1268
        
        """
        return _min3p.f90wrap_gen__get__seep_iter()
    
    @seep_iter.setter
    def seep_iter(self, seep_iter):
        _min3p.f90wrap_gen__set__seep_iter(seep_iter)
    
    @property
    def mass_balance_vs(self):
        """
        Element mass_balance_vs ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1269
        
        """
        return _min3p.f90wrap_gen__get__mass_balance_vs()
    
    @mass_balance_vs.setter
    def mass_balance_vs(self, mass_balance_vs):
        _min3p.f90wrap_gen__set__mass_balance_vs(mass_balance_vs)
    
    @property
    def uvsnew(self):
        """
        Element uvsnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1315
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__uvsnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            uvsnew = self._arrays[array_handle]
        else:
            uvsnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__uvsnew)
            self._arrays[array_handle] = uvsnew
        return uvsnew
    
    @uvsnew.setter
    def uvsnew(self, uvsnew):
        self.uvsnew[...] = uvsnew
    
    @property
    def uvsold(self):
        """
        Element uvsold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1316
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__uvsold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            uvsold = self._arrays[array_handle]
        else:
            uvsold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__uvsold)
            self._arrays[array_handle] = uvsold
        return uvsold
    
    @uvsold.setter
    def uvsold(self, uvsold):
        self.uvsold[...] = uvsold
    
    @property
    def uvsinc(self):
        """
        Element uvsinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1317
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__uvsinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            uvsinc = self._arrays[array_handle]
        else:
            uvsinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__uvsinc)
            self._arrays[array_handle] = uvsinc
        return uvsinc
    
    @uvsinc.setter
    def uvsinc(self, uvsinc):
        self.uvsinc[...] = uvsinc
    
    @property
    def hhead(self):
        """
        Element hhead ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1318
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__hhead(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            hhead = self._arrays[array_handle]
        else:
            hhead = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__hhead)
            self._arrays[array_handle] = hhead
        return hhead
    
    @hhead.setter
    def hhead(self, hhead):
        self.hhead[...] = hhead
    
    @property
    def saold(self):
        """
        Element saold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1319
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__saold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            saold = self._arrays[array_handle]
        else:
            saold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__saold)
            self._arrays[array_handle] = saold
        return saold
    
    @saold.setter
    def saold(self, saold):
        self.saold[...] = saold
    
    @property
    def sanew(self):
        """
        Element sanew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1321
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sanew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sanew = self._arrays[array_handle]
        else:
            sanew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sanew)
            self._arrays[array_handle] = sanew
        return sanew
    
    @sanew.setter
    def sanew(self, sanew):
        self.sanew[...] = sanew
    
    @property
    def sgold(self):
        """
        Element sgold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1322
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sgold(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sgold = self._arrays[array_handle]
        else:
            sgold = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sgold)
            self._arrays[array_handle] = sgold
        return sgold
    
    @sgold.setter
    def sgold(self, sgold):
        self.sgold[...] = sgold
    
    @property
    def sgnew(self):
        """
        Element sgnew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1323
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sgnew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sgnew = self._arrays[array_handle]
        else:
            sgnew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sgnew)
            self._arrays[array_handle] = sgnew
        return sgnew
    
    @sgnew.setter
    def sgnew(self, sgnew):
        self.sgnew[...] = sgnew
    
    @property
    def sainc(self):
        """
        Element sainc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1324
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sainc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sainc = self._arrays[array_handle]
        else:
            sainc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sainc)
            self._arrays[array_handle] = sainc
        return sainc
    
    @sainc.setter
    def sainc(self, sainc):
        self.sainc[...] = sainc
    
    @property
    def sonew(self):
        """
        Element sonew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1325
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__sonew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            sonew = self._arrays[array_handle]
        else:
            sonew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__sonew)
            self._arrays[array_handle] = sonew
        return sonew
    
    @sonew.setter
    def sonew(self, sonew):
        self.sonew[...] = sonew
    
    @property
    def relperm(self):
        """
        Element relperm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1326
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__relperm(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            relperm = self._arrays[array_handle]
        else:
            relperm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__relperm)
            self._arrays[array_handle] = relperm
        return relperm
    
    @relperm.setter
    def relperm(self, relperm):
        self.relperm[...] = relperm
    
    @property
    def relpinc(self):
        """
        Element relpinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1327
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__relpinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            relpinc = self._arrays[array_handle]
        else:
            relpinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__relpinc)
            self._arrays[array_handle] = relpinc
        return relpinc
    
    @relpinc.setter
    def relpinc(self, relpinc):
        self.relpinc[...] = relpinc
    
    @property
    def pornew(self):
        """
        Element pornew ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1329
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__pornew(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            pornew = self._arrays[array_handle]
        else:
            pornew = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__pornew)
            self._arrays[array_handle] = pornew
        return pornew
    
    @pornew.setter
    def pornew(self, pornew):
        self.pornew[...] = pornew
    
    @property
    def por_init(self):
        """
        Element por_init ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1331
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__por_init(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            por_init = self._arrays[array_handle]
        else:
            por_init = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__por_init)
            self._arrays[array_handle] = por_init
        return por_init
    
    @por_init.setter
    def por_init(self, por_init):
        self.por_init[...] = por_init
    
    @property
    def perm_fac(self):
        """
        Element perm_fac ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1332
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__perm_fac(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            perm_fac = self._arrays[array_handle]
        else:
            perm_fac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__perm_fac)
            self._arrays[array_handle] = perm_fac
        return perm_fac
    
    @perm_fac.setter
    def perm_fac(self, perm_fac):
        self.perm_fac[...] = perm_fac
    
    @property
    def cinfvs(self):
        """
        Element cinfvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1333
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfvs = self._arrays[array_handle]
        else:
            cinfvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfvs)
            self._arrays[array_handle] = cinfvs
        return cinfvs
    
    @cinfvs.setter
    def cinfvs(self, cinfvs):
        self.cinfvs[...] = cinfvs
    
    @property
    def permij(self):
        """
        Element permij ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1334
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__permij(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            permij = self._arrays[array_handle]
        else:
            permij = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__permij)
            self._arrays[array_handle] = permij
        return permij
    
    @permij.setter
    def permij(self, permij):
        self.permij[...] = permij
    
    @property
    def relpermg(self):
        """
        Element relpermg ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1336
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__relpermg(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            relpermg = self._arrays[array_handle]
        else:
            relpermg = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__relpermg)
            self._arrays[array_handle] = relpermg
        return relpermg
    
    @relpermg.setter
    def relpermg(self, relpermg):
        self.relpermg[...] = relpermg
    
    @property
    def cinfvs_a(self):
        """
        Element cinfvs_a ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1337
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfvs_a(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfvs_a = self._arrays[array_handle]
        else:
            cinfvs_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfvs_a)
            self._arrays[array_handle] = cinfvs_a
        return cinfvs_a
    
    @cinfvs_a.setter
    def cinfvs_a(self, cinfvs_a):
        self.cinfvs_a[...] = cinfvs_a
    
    @property
    def cinfvs_g(self):
        """
        Element cinfvs_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1338
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__cinfvs_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            cinfvs_g = self._arrays[array_handle]
        else:
            cinfvs_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__cinfvs_g)
            self._arrays[array_handle] = cinfvs_g
        return cinfvs_g
    
    @cinfvs_g.setter
    def cinfvs_g(self, cinfvs_g):
        self.cinfvs_g[...] = cinfvs_g
    
    @property
    def tauivol(self):
        """
        Element tauivol ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1340
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__tauivol(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            tauivol = self._arrays[array_handle]
        else:
            tauivol = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__tauivol)
            self._arrays[array_handle] = tauivol
        return tauivol
    
    @tauivol.setter
    def tauivol(self, tauivol):
        self.tauivol[...] = tauivol
    
    @property
    def mpropvs(self):
        """
        Element mpropvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1342
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__mpropvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            mpropvs = self._arrays[array_handle]
        else:
            mpropvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__mpropvs)
            self._arrays[array_handle] = mpropvs
        return mpropvs
    
    @mpropvs.setter
    def mpropvs(self, mpropvs):
        self.mpropvs[...] = mpropvs
    
    @property
    def binev(self):
        """
        Element binev ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1359
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__binev(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            binev = self._arrays[array_handle]
        else:
            binev = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__binev)
            self._arrays[array_handle] = binev
        return binev
    
    @binev.setter
    def binev(self, binev):
        self.binev[...] = binev
    
    @property
    def bint(self):
        """
        Element bint ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1360
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bint(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bint = self._arrays[array_handle]
        else:
            bint = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bint)
            self._arrays[array_handle] = bint
        return bint
    
    @bint.setter
    def bint(self, bint):
        self.bint[...] = bint
    
    @property
    def qroot(self):
        """
        Element qroot ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1371
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__qroot(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            qroot = self._arrays[array_handle]
        else:
            qroot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__qroot)
            self._arrays[array_handle] = qroot
        return qroot
    
    @qroot.setter
    def qroot(self, qroot):
        self.qroot[...] = qroot
    
    @property
    def qrootinc(self):
        """
        Element qrootinc ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1372
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__qrootinc(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            qrootinc = self._arrays[array_handle]
        else:
            qrootinc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__qrootinc)
            self._arrays[array_handle] = qrootinc
        return qrootinc
    
    @qrootinc.setter
    def qrootinc(self, qrootinc):
        self.qrootinc[...] = qrootinc
    
    @property
    def dqroot(self):
        """
        Element dqroot ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1373
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__dqroot(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dqroot = self._arrays[array_handle]
        else:
            dqroot = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__dqroot)
            self._arrays[array_handle] = dqroot
        return dqroot
    
    @dqroot.setter
    def dqroot(self, dqroot):
        self.dqroot[...] = dqroot
    
    @property
    def totvsmass(self):
        """
        Element totvsmass ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1388
        
        """
        return _min3p.f90wrap_gen__get__totvsmass()
    
    @totvsmass.setter
    def totvsmass(self, totvsmass):
        _min3p.f90wrap_gen__set__totvsmass(totvsmass)
    
    @property
    def culabsbalvs(self):
        """
        Element culabsbalvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1389
        
        """
        return _min3p.f90wrap_gen__get__culabsbalvs()
    
    @culabsbalvs.setter
    def culabsbalvs(self, culabsbalvs):
        _min3p.f90wrap_gen__set__culabsbalvs(culabsbalvs)
    
    @property
    def time_bcvs(self):
        """
        Element time_bcvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1430
        
        """
        return _min3p.f90wrap_gen__get__time_bcvs()
    
    @time_bcvs.setter
    def time_bcvs(self, time_bcvs):
        _min3p.f90wrap_gen__set__time_bcvs(time_bcvs)
    
    @property
    def bcondvs(self):
        """
        Element bcondvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1431
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bcondvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bcondvs = self._arrays[array_handle]
        else:
            bcondvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bcondvs)
            self._arrays[array_handle] = bcondvs
        return bcondvs
    
    @bcondvs.setter
    def bcondvs(self, bcondvs):
        self.bcondvs[...] = bcondvs
    
    @property
    def iabvs(self):
        """
        Element iabvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1433
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iabvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iabvs = self._arrays[array_handle]
        else:
            iabvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iabvs)
            self._arrays[array_handle] = iabvs
        return iabvs
    
    @iabvs.setter
    def iabvs(self, iabvs):
        self.iabvs[...] = iabvs
    
    @property
    def nbvs(self):
        """
        Element nbvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1435
        
        """
        return _min3p.f90wrap_gen__get__nbvs()
    
    @nbvs.setter
    def nbvs(self, nbvs):
        _min3p.f90wrap_gen__set__nbvs(nbvs)
    
    @property
    def ibcvs(self):
        """
        Element ibcvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1436
        
        """
        return _min3p.f90wrap_gen__get__ibcvs()
    
    @ibcvs.setter
    def ibcvs(self, ibcvs):
        _min3p.f90wrap_gen__set__ibcvs(ibcvs)
    
    @property
    def ibcrt(self):
        """
        Element ibcrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1437
        
        """
        return _min3p.f90wrap_gen__get__ibcrt()
    
    @ibcrt.setter
    def ibcrt(self, ibcrt):
        _min3p.f90wrap_gen__set__ibcrt(ibcrt)
    
    @property
    def update_bcvs(self):
        """
        Element update_bcvs ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1439
        
        """
        return _min3p.f90wrap_gen__get__update_bcvs()
    
    @update_bcvs.setter
    def update_bcvs(self, update_bcvs):
        _min3p.f90wrap_gen__set__update_bcvs(update_bcvs)
    
    @property
    def vsflux(self):
        """
        Element vsflux ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1483
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__vsflux(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            vsflux = self._arrays[array_handle]
        else:
            vsflux = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__vsflux)
            self._arrays[array_handle] = vsflux
        return vsflux
    
    @vsflux.setter
    def vsflux(self, vsflux):
        self.vsflux[...] = vsflux
    
    @property
    def dinc_vs(self):
        """
        Element dinc_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1485
        
        """
        return _min3p.f90wrap_gen__get__dinc_vs()
    
    @dinc_vs.setter
    def dinc_vs(self, dinc_vs):
        _min3p.f90wrap_gen__set__dinc_vs(dinc_vs)
    
    @property
    def tol_vs(self):
        """
        Element tol_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1486
        
        """
        return _min3p.f90wrap_gen__get__tol_vs()
    
    @tol_vs.setter
    def tol_vs(self, tol_vs):
        _min3p.f90wrap_gen__set__tol_vs(tol_vs)
    
    @property
    def uvsmaxold(self):
        """
        Element uvsmaxold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1487
        
        """
        return _min3p.f90wrap_gen__get__uvsmaxold()
    
    @uvsmaxold.setter
    def uvsmaxold(self, uvsmaxold):
        _min3p.f90wrap_gen__set__uvsmaxold(uvsmaxold)
    
    @property
    def relfacold(self):
        """
        Element relfacold ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1488
        
        """
        return _min3p.f90wrap_gen__get__relfacold()
    
    @relfacold.setter
    def relfacold(self, relfacold):
        _min3p.f90wrap_gen__set__relfacold(relfacold)
    
    @property
    def srelfac_vs(self):
        """
        Element srelfac_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1489
        
        """
        return _min3p.f90wrap_gen__get__srelfac_vs()
    
    @srelfac_vs.setter
    def srelfac_vs(self, srelfac_vs):
        _min3p.f90wrap_gen__set__srelfac_vs(srelfac_vs)
    
    @property
    def maxit_vs(self):
        """
        Element maxit_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1491
        
        """
        return _min3p.f90wrap_gen__get__maxit_vs()
    
    @maxit_vs.setter
    def maxit_vs(self, maxit_vs):
        _min3p.f90wrap_gen__set__maxit_vs(maxit_vs)
    
    @property
    def iter_vs(self):
        """
        Element iter_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1492
        
        """
        return _min3p.f90wrap_gen__get__iter_vs()
    
    @iter_vs.setter
    def iter_vs(self, iter_vs):
        _min3p.f90wrap_gen__set__iter_vs(iter_vs)
    
    @property
    def ittot_vs(self):
        """
        Element ittot_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1493
        
        """
        return _min3p.f90wrap_gen__get__ittot_vs()
    
    @ittot_vs.setter
    def ittot_vs(self, ittot_vs):
        _min3p.f90wrap_gen__set__ittot_vs(ittot_vs)
    
    @property
    def upstream(self):
        """
        Element upstream ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1495
        
        """
        return _min3p.f90wrap_gen__get__upstream()
    
    @upstream.setter
    def upstream(self, upstream):
        _min3p.f90wrap_gen__set__upstream(upstream)
    
    @property
    def under_relax(self):
        """
        Element under_relax ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1496
        
        """
        return _min3p.f90wrap_gen__get__under_relax()
    
    @under_relax.setter
    def under_relax(self, under_relax):
        _min3p.f90wrap_gen__set__under_relax(under_relax)
    
    @property
    def comp_relax(self):
        """
        Element comp_relax ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1497
        
        """
        return _min3p.f90wrap_gen__get__comp_relax()
    
    @comp_relax.setter
    def comp_relax(self, comp_relax):
        _min3p.f90wrap_gen__set__comp_relax(comp_relax)
    
    @property
    def avs(self):
        """
        Element avs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1543
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__avs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            avs = self._arrays[array_handle]
        else:
            avs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__avs)
            self._arrays[array_handle] = avs
        return avs
    
    @avs.setter
    def avs(self, avs):
        self.avs[...] = avs
    
    @property
    def bvs(self):
        """
        Element bvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1544
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__bvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            bvs = self._arrays[array_handle]
        else:
            bvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__bvs)
            self._arrays[array_handle] = bvs
        return bvs
    
    @bvs.setter
    def bvs(self, bvs):
        self.bvs[...] = bvs
    
    @property
    def uvs(self):
        """
        Element uvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1545
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__uvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            uvs = self._arrays[array_handle]
        else:
            uvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__uvs)
            self._arrays[array_handle] = uvs
        return uvs
    
    @uvs.setter
    def uvs(self, uvs):
        self.uvs[...] = uvs
    
    @property
    def resvs(self):
        """
        Element resvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1546
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__resvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            resvs = self._arrays[array_handle]
        else:
            resvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__resvs)
            self._arrays[array_handle] = resvs
        return resvs
    
    @resvs.setter
    def resvs(self, resvs):
        self.resvs[...] = resvs
    
    @property
    def afvs(self):
        """
        Element afvs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1547
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__afvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            afvs = self._arrays[array_handle]
        else:
            afvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__afvs)
            self._arrays[array_handle] = afvs
        return afvs
    
    @afvs.setter
    def afvs(self, afvs):
        self.afvs[...] = afvs
    
    @property
    def restol_vs(self):
        """
        Element restol_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1549
        
        """
        return _min3p.f90wrap_gen__get__restol_vs()
    
    @restol_vs.setter
    def restol_vs(self, restol_vs):
        _min3p.f90wrap_gen__set__restol_vs(restol_vs)
    
    @property
    def deltol_vs(self):
        """
        Element deltol_vs ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1550
        
        """
        return _min3p.f90wrap_gen__get__deltol_vs()
    
    @deltol_vs.setter
    def deltol_vs(self, deltol_vs):
        _min3p.f90wrap_gen__set__deltol_vs(deltol_vs)
    
    @property
    def iavs(self):
        """
        Element iavs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1552
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iavs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iavs = self._arrays[array_handle]
        else:
            iavs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iavs)
            self._arrays[array_handle] = iavs
        return iavs
    
    @iavs.setter
    def iavs(self, iavs):
        self.iavs[...] = iavs
    
    @property
    def javs(self):
        """
        Element javs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1553
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__javs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            javs = self._arrays[array_handle]
        else:
            javs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__javs)
            self._arrays[array_handle] = javs
        return javs
    
    @javs.setter
    def javs(self, javs):
        self.javs[...] = javs
    
    @property
    def iafvs(self):
        """
        Element iafvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1554
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iafvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iafvs = self._arrays[array_handle]
        else:
            iafvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iafvs)
            self._arrays[array_handle] = iafvs
        return iafvs
    
    @iafvs.setter
    def iafvs(self, iafvs):
        self.iafvs[...] = iafvs
    
    @property
    def jafvs(self):
        """
        Element jafvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1555
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__jafvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            jafvs = self._arrays[array_handle]
        else:
            jafvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__jafvs)
            self._arrays[array_handle] = jafvs
        return jafvs
    
    @jafvs.setter
    def jafvs(self, jafvs):
        self.jafvs[...] = jafvs
    
    @property
    def iafdvs(self):
        """
        Element iafdvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1556
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iafdvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iafdvs = self._arrays[array_handle]
        else:
            iafdvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iafdvs)
            self._arrays[array_handle] = iafdvs
        return iafdvs
    
    @iafdvs.setter
    def iafdvs(self, iafdvs):
        self.iafdvs[...] = iafdvs
    
    @property
    def isymvs(self):
        """
        Element isymvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1557
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__isymvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            isymvs = self._arrays[array_handle]
        else:
            isymvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__isymvs)
            self._arrays[array_handle] = isymvs
        return isymvs
    
    @isymvs.setter
    def isymvs(self, isymvs):
        self.isymvs[...] = isymvs
    
    @property
    def lordervs(self):
        """
        Element lordervs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1558
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__lordervs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            lordervs = self._arrays[array_handle]
        else:
            lordervs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__lordervs)
            self._arrays[array_handle] = lordervs
        return lordervs
    
    @lordervs.setter
    def lordervs(self, lordervs):
        self.lordervs[...] = lordervs
    
    @property
    def invordvs(self):
        """
        Element invordvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1559
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__invordvs(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            invordvs = self._arrays[array_handle]
        else:
            invordvs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__invordvs)
            self._arrays[array_handle] = invordvs
        return invordvs
    
    @invordvs.setter
    def invordvs(self, invordvs):
        self.invordvs[...] = invordvs
    
    @property
    def mnjavs(self):
        """
        Element mnjavs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1561
        
        """
        return _min3p.f90wrap_gen__get__mnjavs()
    
    @mnjavs.setter
    def mnjavs(self, mnjavs):
        _min3p.f90wrap_gen__set__mnjavs(mnjavs)
    
    @property
    def mnjafvs(self):
        """
        Element mnjafvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1562
        
        """
        return _min3p.f90wrap_gen__get__mnjafvs()
    
    @mnjafvs.setter
    def mnjafvs(self, mnjafvs):
        _min3p.f90wrap_gen__set__mnjafvs(mnjafvs)
    
    @property
    def njavs(self):
        """
        Element njavs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1563
        
        """
        return _min3p.f90wrap_gen__get__njavs()
    
    @njavs.setter
    def njavs(self, njavs):
        _min3p.f90wrap_gen__set__njavs(njavs)
    
    @property
    def njafvs(self):
        """
        Element njafvs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1564
        
        """
        return _min3p.f90wrap_gen__get__njafvs()
    
    @njafvs.setter
    def njafvs(self, njafvs):
        _min3p.f90wrap_gen__set__njafvs(njafvs)
    
    @property
    def level_vs(self):
        """
        Element level_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1565
        
        """
        return _min3p.f90wrap_gen__get__level_vs()
    
    @level_vs.setter
    def level_vs(self, level_vs):
        _min3p.f90wrap_gen__set__level_vs(level_vs)
    
    @property
    def msolvit_vs(self):
        """
        Element msolvit_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1566
        
        """
        return _min3p.f90wrap_gen__get__msolvit_vs()
    
    @msolvit_vs.setter
    def msolvit_vs(self, msolvit_vs):
        _min3p.f90wrap_gen__set__msolvit_vs(msolvit_vs)
    
    @property
    def idetail_vs(self):
        """
        Element idetail_vs ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1567
        
        """
        return _min3p.f90wrap_gen__get__idetail_vs()
    
    @idetail_vs.setter
    def idetail_vs(self, idetail_vs):
        _min3p.f90wrap_gen__set__idetail_vs(idetail_vs)
    
    @property
    def rcm_ordering_vs(self):
        """
        Element rcm_ordering_vs ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1569
        
        """
        return _min3p.f90wrap_gen__get__rcm_ordering_vs()
    
    @rcm_ordering_vs.setter
    def rcm_ordering_vs(self, rcm_ordering_vs):
        _min3p.f90wrap_gen__set__rcm_ordering_vs(rcm_ordering_vs)
    
    @property
    def rwork(self):
        """
        Element rwork ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1592
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__rwork(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rwork = self._arrays[array_handle]
        else:
            rwork = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__rwork)
            self._arrays[array_handle] = rwork
        return rwork
    
    @rwork.setter
    def rwork(self, rwork):
        self.rwork[...] = rwork
    
    @property
    def rnorm(self):
        """
        Element rnorm ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1594
        
        """
        return _min3p.f90wrap_gen__get__rnorm()
    
    @rnorm.setter
    def rnorm(self, rnorm):
        _min3p.f90wrap_gen__set__rnorm(rnorm)
    
    @property
    def rmupdate(self):
        """
        Element rmupdate ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1595
        
        """
        return _min3p.f90wrap_gen__get__rmupdate()
    
    @rmupdate.setter
    def rmupdate(self, rmupdate):
        _min3p.f90wrap_gen__set__rmupdate(rmupdate)
    
    @property
    def iwork(self):
        """
        Element iwork ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1597
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__iwork(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            iwork = self._arrays[array_handle]
        else:
            iwork = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__iwork)
            self._arrays[array_handle] = iwork
        return iwork
    
    @iwork.setter
    def iwork(self, iwork):
        self.iwork[...] = iwork
    
    @property
    def itsolv(self):
        """
        Element itsolv ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1599
        
        """
        return _min3p.f90wrap_gen__get__itsolv()
    
    @itsolv.setter
    def itsolv(self, itsolv):
        _min3p.f90wrap_gen__set__itsolv(itsolv)
    
    @property
    def lwork(self):
        """
        Element lwork ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1601
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__lwork(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            lwork = self._arrays[array_handle]
        else:
            lwork = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__lwork)
            self._arrays[array_handle] = lwork
        return lwork
    
    @lwork.setter
    def lwork(self, lwork):
        self.lwork[...] = lwork
    
    @property
    def skip(self):
        """
        Element skip ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1605
        
        """
        return _min3p.f90wrap_gen__get__skip()
    
    @skip.setter
    def skip(self, skip):
        _min3p.f90wrap_gen__set__skip(skip)
    
    @property
    def nskip(self):
        """
        Element nskip ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1605
        
        """
        return _min3p.f90wrap_gen__get__nskip()
    
    @nskip.setter
    def nskip(self, nskip):
        _min3p.f90wrap_gen__set__nskip(nskip)
    
    @property
    def chemical_water(self):
        """
        Element chemical_water ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1608
        
        """
        return _min3p.f90wrap_gen__get__chemical_water()
    
    @chemical_water.setter
    def chemical_water(self, chemical_water):
        _min3p.f90wrap_gen__set__chemical_water(chemical_water)
    
    @property
    def qwater(self):
        """
        Element qwater ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/gen.f line 1610
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_gen__array__qwater(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            qwater = self._arrays[array_handle]
        else:
            qwater = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_gen__array__qwater)
            self._arrays[array_handle] = qwater
        return qwater
    
    @qwater.setter
    def qwater(self, qwater):
        self.qwater[...] = qwater
    
    @property
    def rsrt_cnt(self):
        """
        Element rsrt_cnt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1613
        
        """
        return _min3p.f90wrap_gen__get__rsrt_cnt()
    
    @rsrt_cnt.setter
    def rsrt_cnt(self, rsrt_cnt):
        _min3p.f90wrap_gen__set__rsrt_cnt(rsrt_cnt)
    
    @property
    def irsrt(self):
        """
        Element irsrt ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1614
        
        """
        return _min3p.f90wrap_gen__get__irsrt()
    
    @irsrt.setter
    def irsrt(self, irsrt):
        _min3p.f90wrap_gen__set__irsrt(irsrt)
    
    @property
    def backup_frequency(self):
        """
        Element backup_frequency ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/gen.f line 1615
        
        """
        return _min3p.f90wrap_gen__get__backup_frequency()
    
    @backup_frequency.setter
    def backup_frequency(self, backup_frequency):
        _min3p.f90wrap_gen__set__backup_frequency(backup_frequency)
    
    @property
    def restart_sim(self):
        """
        Element restart_sim ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1616
        
        """
        return _min3p.f90wrap_gen__get__restart_sim()
    
    @restart_sim.setter
    def restart_sim(self, restart_sim):
        _min3p.f90wrap_gen__set__restart_sim(restart_sim)
    
    @property
    def ovr_sat(self):
        """
        Element ovr_sat ftype=logical pytype=bool
        
        
        Defined at ../src/gen.f line 1619
        
        """
        return _min3p.f90wrap_gen__get__ovr_sat()
    
    @ovr_sat.setter
    def ovr_sat(self, ovr_sat):
        _min3p.f90wrap_gen__set__ovr_sat(ovr_sat)
    
    def __str__(self):
        ret = ['<gen>{\n']
        ret.append('    cpuint : ')
        ret.append(repr(self.cpuint))
        ret.append(',\n    csec : ')
        ret.append(repr(self.csec))
        ret.append(',\n    varsat_flow : ')
        ret.append(repr(self.varsat_flow))
        ret.append(',\n    steady_flow : ')
        ret.append(repr(self.steady_flow))
        ret.append(',\n    transient_flow : ')
        ret.append(repr(self.transient_flow))
        ret.append(',\n    not_converged : ')
        ret.append(repr(self.not_converged))
        ret.append(',\n    full_path : ')
        ret.append(repr(self.full_path))
        ret.append(',\n    fully_saturated : ')
        ret.append(repr(self.fully_saturated))
        ret.append(',\n    variably_saturated : ')
        ret.append(repr(self.variably_saturated))
        ret.append(',\n    geo_chemistry : ')
        ret.append(repr(self.geo_chemistry))
        ret.append(',\n    reactive_transport : ')
        ret.append(repr(self.reactive_transport))
        ret.append(',\n    show_module : ')
        ret.append(repr(self.show_module))
        ret.append(',\n    log_file : ')
        ret.append(repr(self.log_file))
        ret.append(',\n    depth_output : ')
        ret.append(repr(self.depth_output))
        ret.append(',\n    update_porosity : ')
        ret.append(repr(self.update_porosity))
        ret.append(',\n    update_permeability : ')
        ret.append(repr(self.update_permeability))
        ret.append(',\n    pure_evap : ')
        ret.append(repr(self.pure_evap))
        ret.append(',\n    sec_per_days : ')
        ret.append(repr(self.sec_per_days))
        ret.append(',\n    gacc : ')
        ret.append(repr(self.gacc))
        ret.append(',\n    xg : ')
        ret.append(repr(self.xg))
        ret.append(',\n    yg : ')
        ret.append(repr(self.yg))
        ret.append(',\n    zg : ')
        ret.append(repr(self.zg))
        ret.append(',\n    dimcv : ')
        ret.append(repr(self.dimcv))
        ret.append(',\n    cvol : ')
        ret.append(repr(self.cvol))
        ret.append(',\n    delx : ')
        ret.append(repr(self.delx))
        ret.append(',\n    dely : ')
        ret.append(repr(self.dely))
        ret.append(',\n    delz : ')
        ret.append(repr(self.delz))
        ret.append(',\n    xmax : ')
        ret.append(repr(self.xmax))
        ret.append(',\n    xmin : ')
        ret.append(repr(self.xmin))
        ret.append(',\n    ymax : ')
        ret.append(repr(self.ymax))
        ret.append(',\n    ymin : ')
        ret.append(repr(self.ymin))
        ret.append(',\n    zmax : ')
        ret.append(repr(self.zmax))
        ret.append(',\n    zmin : ')
        ret.append(repr(self.zmin))
        ret.append(',\n    elevmax : ')
        ret.append(repr(self.elevmax))
        ret.append(',\n    toparea : ')
        ret.append(repr(self.toparea))
        ret.append(',\n    nvix : ')
        ret.append(repr(self.nvix))
        ret.append(',\n    nviy : ')
        ret.append(repr(self.nviy))
        ret.append(',\n    nviz : ')
        ret.append(repr(self.nviz))
        ret.append(',\n    nxx : ')
        ret.append(repr(self.nxx))
        ret.append(',\n    nyy : ')
        ret.append(repr(self.nyy))
        ret.append(',\n    nzz : ')
        ret.append(repr(self.nzz))
        ret.append(',\n    nvx : ')
        ret.append(repr(self.nvx))
        ret.append(',\n    nvy : ')
        ret.append(repr(self.nvy))
        ret.append(',\n    nvz : ')
        ret.append(repr(self.nvz))
        ret.append(',\n    nn : ')
        ret.append(repr(self.nn))
        ret.append(',\n    half_cells : ')
        ret.append(repr(self.half_cells))
        ret.append(',\n    delta_c : ')
        ret.append(repr(self.delta_c))
        ret.append(',\n    delta_c_max : ')
        ret.append(repr(self.delta_c_max))
        ret.append(',\n    time : ')
        ret.append(repr(self.time))
        ret.append(',\n    time_io : ')
        ret.append(repr(self.time_io))
        ret.append(',\n    time_io_bis : ')
        ret.append(repr(self.time_io_bis))
        ret.append(',\n    time_io_prec : ')
        ret.append(repr(self.time_io_prec))
        ret.append(',\n    time_factor : ')
        ret.append(repr(self.time_factor))
        ret.append(',\n    tfinal : ')
        ret.append(repr(self.tfinal))
        ret.append(',\n    tfinal_bis : ')
        ret.append(repr(self.tfinal_bis))
        ret.append(',\n    delt : ')
        ret.append(repr(self.delt))
        ret.append(',\n    delt_io : ')
        ret.append(repr(self.delt_io))
        ret.append(',\n    delt_vs : ')
        ret.append(repr(self.delt_vs))
        ret.append(',\n    delt_rt : ')
        ret.append(repr(self.delt_rt))
        ret.append(',\n    deltmin : ')
        ret.append(repr(self.deltmin))
        ret.append(',\n    deltmax : ')
        ret.append(repr(self.deltmax))
        ret.append(',\n    urtant_log : ')
        ret.append(repr(self.urtant_log))
        ret.append(',\n    l_time_unit : ')
        ret.append(repr(self.l_time_unit))
        ret.append(',\n    mtime : ')
        ret.append(repr(self.mtime))
        ret.append(',\n    mtime_f : ')
        ret.append(repr(self.mtime_f))
        ret.append(',\n    reduce_timestep : ')
        ret.append(repr(self.reduce_timestep))
        ret.append(',\n    gs_tout : ')
        ret.append(repr(self.gs_tout))
        ret.append(',\n    iamb : ')
        ret.append(repr(self.iamb))
        ret.append(',\n    ngb_vol : ')
        ret.append(repr(self.ngb_vol))
        ret.append(',\n    ngb : ')
        ret.append(repr(self.ngb))
        ret.append(',\n    ngs : ')
        ret.append(repr(self.ngs))
        ret.append(',\n    igstime : ')
        ret.append(repr(self.igstime))
        ret.append(',\n    ngb_step : ')
        ret.append(repr(self.ngb_step))
        ret.append(',\n    nmb : ')
        ret.append(repr(self.nmb))
        ret.append(',\n    l_prfx : ')
        ret.append(repr(self.l_prfx))
        ret.append(',\n    l_dbs_dir : ')
        ret.append(repr(self.l_dbs_dir))
        ret.append(',\n    idat : ')
        ret.append(repr(self.idat))
        ret.append(',\n    igen : ')
        ret.append(repr(self.igen))
        ret.append(',\n    ifls : ')
        ret.append(repr(self.ifls))
        ret.append(',\n    idbg : ')
        ret.append(repr(self.idbg))
        ret.append(',\n    ilog : ')
        ret.append(repr(self.ilog))
        ret.append(',\n    idelt : ')
        ret.append(repr(self.idelt))
        ret.append(',\n    icnv : ')
        ret.append(repr(self.icnv))
        ret.append(',\n    ihyc : ')
        ret.append(repr(self.ihyc))
        ret.append(',\n    itmp : ')
        ret.append(repr(self.itmp))
        ret.append(',\n    ivel : ')
        ret.append(repr(self.ivel))
        ret.append(',\n    icdbs : ')
        ret.append(repr(self.icdbs))
        ret.append(',\n    ixdbs : ')
        ret.append(repr(self.ixdbs))
        ret.append(',\n    imdbs : ')
        ret.append(repr(self.imdbs))
        ret.append(',\n    isdbs : ')
        ret.append(repr(self.isdbs))
        ret.append(',\n    irdbs : ')
        ret.append(repr(self.irdbs))
        ret.append(',\n    igdbs : ')
        ret.append(repr(self.igdbs))
        ret.append(',\n    imvs : ')
        ret.append(repr(self.imvs))
        ret.append(',\n    imvs_first : ')
        ret.append(repr(self.imvs_first))
        ret.append(',\n    imvs_last : ')
        ret.append(repr(self.imvs_last))
        ret.append(',\n    imrt : ')
        ret.append(repr(self.imrt))
        ret.append(',\n    imrt_first : ')
        ret.append(repr(self.imrt_first))
        ret.append(',\n    imrt_last : ')
        ret.append(repr(self.imrt_last))
        ret.append(',\n    igsp : ')
        ret.append(repr(self.igsp))
        ret.append(',\n    igsb : ')
        ret.append(repr(self.igsb))
        ret.append(',\n    igsc : ')
        ret.append(repr(self.igsc))
        ret.append(',\n    igsd : ')
        ret.append(repr(self.igsd))
        ret.append(',\n    igsg : ')
        ret.append(repr(self.igsg))
        ret.append(',\n    igsgr : ')
        ret.append(repr(self.igsgr))
        ret.append(',\n    igsm : ')
        ret.append(repr(self.igsm))
        ret.append(',\n    igsi : ')
        ret.append(repr(self.igsi))
        ret.append(',\n    igss : ')
        ret.append(repr(self.igss))
        ret.append(',\n    igst : ')
        ret.append(repr(self.igst))
        ret.append(',\n    igsv : ')
        ret.append(repr(self.igsv))
        ret.append(',\n    igsx : ')
        ret.append(repr(self.igsx))
        ret.append(',\n    igb_start : ')
        ret.append(repr(self.igb_start))
        ret.append(',\n    igbb : ')
        ret.append(repr(self.igbb))
        ret.append(',\n    igbc : ')
        ret.append(repr(self.igbc))
        ret.append(',\n    igbd : ')
        ret.append(repr(self.igbd))
        ret.append(',\n    igbg : ')
        ret.append(repr(self.igbg))
        ret.append(',\n    igbgr : ')
        ret.append(repr(self.igbgr))
        ret.append(',\n    igbm : ')
        ret.append(repr(self.igbm))
        ret.append(',\n    igbp : ')
        ret.append(repr(self.igbp))
        ret.append(',\n    igbi : ')
        ret.append(repr(self.igbi))
        ret.append(',\n    igbs : ')
        ret.append(repr(self.igbs))
        ret.append(',\n    igbt : ')
        ret.append(repr(self.igbt))
        ret.append(',\n    igbv : ')
        ret.append(repr(self.igbv))
        ret.append(',\n    igbx : ')
        ret.append(repr(self.igbx))
        ret.append(',\n    ipsp : ')
        ret.append(repr(self.ipsp))
        ret.append(',\n    itec : ')
        ret.append(repr(self.itec))
        ret.append(',\n    item : ')
        ret.append(repr(self.item))
        ret.append(',\n    jtec : ')
        ret.append(repr(self.jtec))
        ret.append(',\n    ktec : ')
        ret.append(repr(self.ktec))
        ret.append(',\n    l_zone_name : ')
        ret.append(repr(self.l_zone_name))
        ret.append(',\n    igsa : ')
        ret.append(repr(self.igsa))
        ret.append(',\n    igsa_first : ')
        ret.append(repr(self.igsa_first))
        ret.append(',\n    igsa_last : ')
        ret.append(repr(self.igsa_last))
        ret.append(',\n    igs2 : ')
        ret.append(repr(self.igs2))
        ret.append(',\n    igsr : ')
        ret.append(repr(self.igsr))
        ret.append(',\n    igsy : ')
        ret.append(repr(self.igsy))
        ret.append(',\n    igsf : ')
        ret.append(repr(self.igsf))
        ret.append(',\n    igsf_first : ')
        ret.append(repr(self.igsf_first))
        ret.append(',\n    igsf_last : ')
        ret.append(repr(self.igsf_last))
        ret.append(',\n    igsk : ')
        ret.append(repr(self.igsk))
        ret.append(',\n    igsw : ')
        ret.append(repr(self.igsw))
        ret.append(',\n    initial_condition : ')
        ret.append(repr(self.initial_condition))
        ret.append(',\n    extended_output : ')
        ret.append(repr(self.extended_output))
        ret.append(',\n    gs_output : ')
        ret.append(repr(self.gs_output))
        ret.append(',\n    gb_output : ')
        ret.append(repr(self.gb_output))
        ret.append(',\n    tec_header : ')
        ret.append(repr(self.tec_header))
        ret.append(',\n    dinc_rt : ')
        ret.append(repr(self.dinc_rt))
        ret.append(',\n    tol_rt : ')
        ret.append(repr(self.tol_rt))
        ret.append(',\n    srelfac_rt : ')
        ret.append(repr(self.srelfac_rt))
        ret.append(',\n    n : ')
        ret.append(repr(self.n))
        ret.append(',\n    iter_rt : ')
        ret.append(repr(self.iter_rt))
        ret.append(',\n    iter_rt_ant : ')
        ret.append(repr(self.iter_rt_ant))
        ret.append(',\n    maxit_rt : ')
        ret.append(repr(self.maxit_rt))
        ret.append(',\n    itsolvtot_rt : ')
        ret.append(repr(self.itsolvtot_rt))
        ret.append(',\n    ittot_rt : ')
        ret.append(repr(self.ittot_rt))
        ret.append(',\n    analyt_deriv_rt : ')
        ret.append(repr(self.analyt_deriv_rt))
        ret.append(',\n    mass_balance_rt : ')
        ret.append(repr(self.mass_balance_rt))
        ret.append(',\n    sparse_blocks : ')
        ret.append(repr(self.sparse_blocks))
        ret.append(',\n    redox_equil_rt : ')
        ret.append(repr(self.redox_equil_rt))
        ret.append(',\n    under_relax_rt : ')
        ret.append(repr(self.under_relax_rt))
        ret.append(',\n    gas_advection : ')
        ret.append(repr(self.gas_advection))
        ret.append(',\n    cum_molfrac : ')
        ret.append(repr(self.cum_molfrac))
        ret.append(',\n    gas_gravity : ')
        ret.append(repr(self.gas_gravity))
        ret.append(',\n    update_tortuosity : ')
        ret.append(repr(self.update_tortuosity))
        ret.append(',\n    c : ')
        ret.append(repr(self.c))
        ret.append(',\n    cnew : ')
        ret.append(repr(self.cnew))
        ret.append(',\n    cec_g : ')
        ret.append(repr(self.cec_g))
        ret.append(',\n    gamma : ')
        ret.append(repr(self.gamma))
        ret.append(',\n    totaold : ')
        ret.append(repr(self.totaold))
        ret.append(',\n    totanew : ')
        ret.append(repr(self.totanew))
        ret.append(',\n    totcold : ')
        ret.append(repr(self.totcold))
        ret.append(',\n    totcnew : ')
        ret.append(repr(self.totcnew))
        ret.append(',\n    totgold : ')
        ret.append(repr(self.totgold))
        ret.append(',\n    totgnew : ')
        ret.append(repr(self.totgnew))
        ret.append(',\n    totsold : ')
        ret.append(repr(self.totsold))
        ret.append(',\n    totsnew : ')
        ret.append(repr(self.totsnew))
        ret.append(',\n    cmold : ')
        ret.append(repr(self.cmold))
        ret.append(',\n    cmnew : ')
        ret.append(repr(self.cmnew))
        ret.append(',\n    distcoff_rt : ')
        ret.append(repr(self.distcoff_rt))
        ret.append(',\n    ksb2 : ')
        ret.append(repr(self.ksb2))
        ret.append(',\n    pdm_rt : ')
        ret.append(repr(self.pdm_rt))
        ret.append(',\n    gold : ')
        ret.append(repr(self.gold))
        ret.append(',\n    gnew : ')
        ret.append(repr(self.gnew))
        ret.append(',\n    cx : ')
        ret.append(repr(self.cx))
        ret.append(',\n    sionnew : ')
        ret.append(repr(self.sionnew))
        ret.append(',\n    sionold : ')
        ret.append(repr(self.sionold))
        ret.append(',\n    phi : ')
        ret.append(repr(self.phi))
        ret.append(',\n    phiold : ')
        ret.append(repr(self.phiold))
        ret.append(',\n    phi_init : ')
        ret.append(repr(self.phi_init))
        ret.append(',\n    area : ')
        ret.append(repr(self.area))
        ret.append(',\n    cinfrt_va : ')
        ret.append(repr(self.cinfrt_va))
        ret.append(',\n    cinfrt_da : ')
        ret.append(repr(self.cinfrt_da))
        ret.append(',\n    cinfrt_dg : ')
        ret.append(repr(self.cinfrt_dg))
        ret.append(',\n    deltaij : ')
        ret.append(repr(self.deltaij))
        ret.append(',\n    tauij : ')
        ret.append(repr(self.tauij))
        ret.append(',\n    gporij : ')
        ret.append(repr(self.gporij))
        ret.append(',\n    gsatij : ')
        ret.append(repr(self.gsatij))
        ret.append(',\n    tkel : ')
        ret.append(repr(self.tkel))
        ret.append(',\n    gmfrac : ')
        ret.append(repr(self.gmfrac))
        ret.append(',\n    totgmfrac : ')
        ret.append(repr(self.totgmfrac))
        ret.append(',\n    mpropc : ')
        ret.append(repr(self.mpropc))
        ret.append(',\n    bcondrt_a : ')
        ret.append(repr(self.bcondrt_a))
        ret.append(',\n    bcondrt_g : ')
        ret.append(repr(self.bcondrt_g))
        ret.append(',\n    bdycrt_d : ')
        ret.append(repr(self.bdycrt_d))
        ret.append(',\n    zgbrt : ')
        ret.append(repr(self.zgbrt))
        ret.append(',\n    dijbrt : ')
        ret.append(repr(self.dijbrt))
        ret.append(',\n    gbrt : ')
        ret.append(repr(self.gbrt))
        ret.append(',\n    tsrc : ')
        ret.append(repr(self.tsrc))
        ret.append(',\n    permbrt : ')
        ret.append(repr(self.permbrt))
        ret.append(',\n    cinfvs_gbrt : ')
        ret.append(repr(self.cinfvs_gbrt))
        ret.append(',\n    iabrt : ')
        ret.append(repr(self.iabrt))
        ret.append(',\n    jabrt : ')
        ret.append(repr(self.jabrt))
        ret.append(',\n    itsrc : ')
        ret.append(repr(self.itsrc))
        ret.append(',\n    nbrt : ')
        ret.append(repr(self.nbrt))
        ret.append(',\n    nbzrt : ')
        ret.append(repr(self.nbzrt))
        ret.append(',\n    ntsrc : ')
        ret.append(repr(self.ntsrc))
        ret.append(',\n    spec_conc : ')
        ret.append(repr(self.spec_conc))
        ret.append(',\n    transient_source : ')
        ret.append(repr(self.transient_source))
        ret.append(',\n    update_bcrt : ')
        ret.append(repr(self.update_bcrt))
        ret.append(',\n    astor : ')
        ret.append(repr(self.astor))
        ret.append(',\n    cflux : ')
        ret.append(repr(self.cflux))
        ret.append(',\n    cstor : ')
        ret.append(repr(self.cstor))
        ret.append(',\n    gflux : ')
        ret.append(repr(self.gflux))
        ret.append(',\n    gstor : ')
        ret.append(repr(self.gstor))
        ret.append(',\n    dtotcflux : ')
        ret.append(repr(self.dtotcflux))
        ret.append(',\n    dtotgflux : ')
        ret.append(repr(self.dtotgflux))
        ret.append(',\n    ratemdp : ')
        ret.append(repr(self.ratemdp))
        ret.append(',\n    totcflux : ')
        ret.append(repr(self.totcflux))
        ret.append(',\n    totgflux : ')
        ret.append(repr(self.totgflux))
        ret.append(',\n    totgaflux : ')
        ret.append(repr(self.totgaflux))
        ret.append(',\n    totmdp : ')
        ret.append(repr(self.totmdp))
        ret.append(',\n    i2up : ')
        ret.append(repr(self.i2up))
        ret.append(',\n    art : ')
        ret.append(repr(self.art))
        ret.append(',\n    brt : ')
        ret.append(repr(self.brt))
        ret.append(',\n    urt : ')
        ret.append(repr(self.urt))
        ret.append(',\n    resrt : ')
        ret.append(repr(self.resrt))
        ret.append(',\n    afrt : ')
        ret.append(repr(self.afrt))
        ret.append(',\n    restol_rt : ')
        ret.append(repr(self.restol_rt))
        ret.append(',\n    deltol_rt : ')
        ret.append(repr(self.deltol_rt))
        ret.append(',\n    urtlim_log : ')
        ret.append(repr(self.urtlim_log))
        ret.append(',\n    iart : ')
        ret.append(repr(self.iart))
        ret.append(',\n    jart : ')
        ret.append(repr(self.jart))
        ret.append(',\n    lart : ')
        ret.append(repr(self.lart))
        ret.append(',\n    kbl : ')
        ret.append(repr(self.kbl))
        ret.append(',\n    kart : ')
        ret.append(repr(self.kart))
        ret.append(',\n    iafrt : ')
        ret.append(repr(self.iafrt))
        ret.append(',\n    jafrt : ')
        ret.append(repr(self.jafrt))
        ret.append(',\n    iafdrt : ')
        ret.append(repr(self.iafdrt))
        ret.append(',\n    lorderrt : ')
        ret.append(repr(self.lorderrt))
        ret.append(',\n    invordrt : ')
        ret.append(repr(self.invordrt))
        ret.append(',\n    iadbl : ')
        ret.append(repr(self.iadbl))
        ret.append(',\n    jadbl : ')
        ret.append(repr(self.jadbl))
        ret.append(',\n    kadbl : ')
        ret.append(repr(self.kadbl))
        ret.append(',\n    iaobl : ')
        ret.append(repr(self.iaobl))
        ret.append(',\n    jaobl : ')
        ret.append(repr(self.jaobl))
        ret.append(',\n    kaobl : ')
        ret.append(repr(self.kaobl))
        ret.append(',\n    mnjart : ')
        ret.append(repr(self.mnjart))
        ret.append(',\n    mnjafrt : ')
        ret.append(repr(self.mnjafrt))
        ret.append(',\n    njart : ')
        ret.append(repr(self.njart))
        ret.append(',\n    njafrt : ')
        ret.append(repr(self.njafrt))
        ret.append(',\n    njadbl : ')
        ret.append(repr(self.njadbl))
        ret.append(',\n    njaobl : ')
        ret.append(repr(self.njaobl))
        ret.append(',\n    level_rt : ')
        ret.append(repr(self.level_rt))
        ret.append(',\n    msolvit_rt : ')
        ret.append(repr(self.msolvit_rt))
        ret.append(',\n    nexvol_old_rt : ')
        ret.append(repr(self.nexvol_old_rt))
        ret.append(',\n    idetail_rt : ')
        ret.append(repr(self.idetail_rt))
        ret.append(',\n    rcm_ordering_rt : ')
        ret.append(repr(self.rcm_ordering_rt))
        ret.append(',\n    cfluxin : ')
        ret.append(repr(self.cfluxin))
        ret.append(',\n    cfluxout : ')
        ret.append(repr(self.cfluxout))
        ret.append(',\n    gfluxtbdy : ')
        ret.append(repr(self.gfluxtbdy))
        ret.append(',\n    gfluxin : ')
        ret.append(repr(self.gfluxin))
        ret.append(',\n    gfluxout : ')
        ret.append(repr(self.gfluxout))
        ret.append(',\n    gafluxin : ')
        ret.append(repr(self.gafluxin))
        ret.append(',\n    gafluxout : ')
        ret.append(repr(self.gafluxout))
        ret.append(',\n    cstordiff : ')
        ret.append(repr(self.cstordiff))
        ret.append(',\n    gdegas : ')
        ret.append(repr(self.gdegas))
        ret.append(',\n    gstordiff : ')
        ret.append(repr(self.gstordiff))
        ret.append(',\n    ordiff : ')
        ret.append(repr(self.ordiff))
        ret.append(',\n    dpdiff : ')
        ret.append(repr(self.dpdiff))
        ret.append(',\n    gdiff : ')
        ret.append(repr(self.gdiff))
        ret.append(',\n    amass : ')
        ret.append(repr(self.amass))
        ret.append(',\n    tmass : ')
        ret.append(repr(self.tmass))
        ret.append(',\n    cmass : ')
        ret.append(repr(self.cmass))
        ret.append(',\n    gmass : ')
        ret.append(repr(self.gmass))
        ret.append(',\n    cmmass : ')
        ret.append(repr(self.cmmass))
        ret.append(',\n    csbmass : ')
        ret.append(repr(self.csbmass))
        ret.append(',\n    csbmass_c : ')
        ret.append(repr(self.csbmass_c))
        ret.append(',\n    cculabsbal : ')
        ret.append(repr(self.cculabsbal))
        ret.append(',\n    cculrelbal : ')
        ret.append(repr(self.cculrelbal))
        ret.append(',\n    gculabsbal : ')
        ret.append(repr(self.gculabsbal))
        ret.append(',\n    gculrelbal : ')
        ret.append(repr(self.gculrelbal))
        ret.append(',\n    cmculabsbal : ')
        ret.append(repr(self.cmculabsbal))
        ret.append(',\n    cmculrelbal : ')
        ret.append(repr(self.cmculrelbal))
        ret.append(',\n    smass : ')
        ret.append(repr(self.smass))
        ret.append(',\n    sbdiff : ')
        ret.append(repr(self.sbdiff))
        ret.append(',\n    rateaqtot : ')
        ret.append(repr(self.rateaqtot))
        ret.append(',\n    contaqtot : ')
        ret.append(repr(self.contaqtot))
        ret.append(',\n    contmintot : ')
        ret.append(repr(self.contmintot))
        ret.append(',\n    totcfluxin : ')
        ret.append(repr(self.totcfluxin))
        ret.append(',\n    totcfluxout : ')
        ret.append(repr(self.totcfluxout))
        ret.append(',\n    totcstordiff : ')
        ret.append(repr(self.totcstordiff))
        ret.append(',\n    totordiff : ')
        ret.append(repr(self.totordiff))
        ret.append(',\n    totdpdiff : ')
        ret.append(repr(self.totdpdiff))
        ret.append(',\n    totgdegas : ')
        ret.append(repr(self.totgdegas))
        ret.append(',\n    totgdiff : ')
        ret.append(repr(self.totgdiff))
        ret.append(',\n    totgfluxin : ')
        ret.append(repr(self.totgfluxin))
        ret.append(',\n    totgfluxout : ')
        ret.append(repr(self.totgfluxout))
        ret.append(',\n    totgafluxin : ')
        ret.append(repr(self.totgafluxin))
        ret.append(',\n    totgafluxout : ')
        ret.append(repr(self.totgafluxout))
        ret.append(',\n    totgstordiff : ')
        ret.append(repr(self.totgstordiff))
        ret.append(',\n    totsbdiff : ')
        ret.append(repr(self.totsbdiff))
        ret.append(',\n    dpdiffp : ')
        ret.append(repr(self.dpdiffp))
        ret.append(',\n    totdpdiffp : ')
        ret.append(repr(self.totdpdiffp))
        ret.append(',\n    sw_star : ')
        ret.append(repr(self.sw_star))
        ret.append(',\n    uvslim : ')
        ret.append(repr(self.uvslim))
        ret.append(',\n    iter_seep : ')
        ret.append(repr(self.iter_seep))
        ret.append(',\n    itseep_tot : ')
        ret.append(repr(self.itseep_tot))
        ret.append(',\n    itsolvtot_vs : ')
        ret.append(repr(self.itsolvtot_vs))
        ret.append(',\n    nseep_first : ')
        ret.append(repr(self.nseep_first))
        ret.append(',\n    pressure_head : ')
        ret.append(repr(self.pressure_head))
        ret.append(',\n    hydraulic_head : ')
        ret.append(repr(self.hydraulic_head))
        ret.append(',\n    seepage_face : ')
        ret.append(repr(self.seepage_face))
        ret.append(',\n    seep_iter : ')
        ret.append(repr(self.seep_iter))
        ret.append(',\n    mass_balance_vs : ')
        ret.append(repr(self.mass_balance_vs))
        ret.append(',\n    uvsnew : ')
        ret.append(repr(self.uvsnew))
        ret.append(',\n    uvsold : ')
        ret.append(repr(self.uvsold))
        ret.append(',\n    uvsinc : ')
        ret.append(repr(self.uvsinc))
        ret.append(',\n    hhead : ')
        ret.append(repr(self.hhead))
        ret.append(',\n    saold : ')
        ret.append(repr(self.saold))
        ret.append(',\n    sanew : ')
        ret.append(repr(self.sanew))
        ret.append(',\n    sgold : ')
        ret.append(repr(self.sgold))
        ret.append(',\n    sgnew : ')
        ret.append(repr(self.sgnew))
        ret.append(',\n    sainc : ')
        ret.append(repr(self.sainc))
        ret.append(',\n    sonew : ')
        ret.append(repr(self.sonew))
        ret.append(',\n    relperm : ')
        ret.append(repr(self.relperm))
        ret.append(',\n    relpinc : ')
        ret.append(repr(self.relpinc))
        ret.append(',\n    pornew : ')
        ret.append(repr(self.pornew))
        ret.append(',\n    por_init : ')
        ret.append(repr(self.por_init))
        ret.append(',\n    perm_fac : ')
        ret.append(repr(self.perm_fac))
        ret.append(',\n    cinfvs : ')
        ret.append(repr(self.cinfvs))
        ret.append(',\n    permij : ')
        ret.append(repr(self.permij))
        ret.append(',\n    relpermg : ')
        ret.append(repr(self.relpermg))
        ret.append(',\n    cinfvs_a : ')
        ret.append(repr(self.cinfvs_a))
        ret.append(',\n    cinfvs_g : ')
        ret.append(repr(self.cinfvs_g))
        ret.append(',\n    tauivol : ')
        ret.append(repr(self.tauivol))
        ret.append(',\n    mpropvs : ')
        ret.append(repr(self.mpropvs))
        ret.append(',\n    binev : ')
        ret.append(repr(self.binev))
        ret.append(',\n    bint : ')
        ret.append(repr(self.bint))
        ret.append(',\n    qroot : ')
        ret.append(repr(self.qroot))
        ret.append(',\n    qrootinc : ')
        ret.append(repr(self.qrootinc))
        ret.append(',\n    dqroot : ')
        ret.append(repr(self.dqroot))
        ret.append(',\n    totvsmass : ')
        ret.append(repr(self.totvsmass))
        ret.append(',\n    culabsbalvs : ')
        ret.append(repr(self.culabsbalvs))
        ret.append(',\n    time_bcvs : ')
        ret.append(repr(self.time_bcvs))
        ret.append(',\n    bcondvs : ')
        ret.append(repr(self.bcondvs))
        ret.append(',\n    iabvs : ')
        ret.append(repr(self.iabvs))
        ret.append(',\n    nbvs : ')
        ret.append(repr(self.nbvs))
        ret.append(',\n    ibcvs : ')
        ret.append(repr(self.ibcvs))
        ret.append(',\n    ibcrt : ')
        ret.append(repr(self.ibcrt))
        ret.append(',\n    update_bcvs : ')
        ret.append(repr(self.update_bcvs))
        ret.append(',\n    vsflux : ')
        ret.append(repr(self.vsflux))
        ret.append(',\n    dinc_vs : ')
        ret.append(repr(self.dinc_vs))
        ret.append(',\n    tol_vs : ')
        ret.append(repr(self.tol_vs))
        ret.append(',\n    uvsmaxold : ')
        ret.append(repr(self.uvsmaxold))
        ret.append(',\n    relfacold : ')
        ret.append(repr(self.relfacold))
        ret.append(',\n    srelfac_vs : ')
        ret.append(repr(self.srelfac_vs))
        ret.append(',\n    maxit_vs : ')
        ret.append(repr(self.maxit_vs))
        ret.append(',\n    iter_vs : ')
        ret.append(repr(self.iter_vs))
        ret.append(',\n    ittot_vs : ')
        ret.append(repr(self.ittot_vs))
        ret.append(',\n    upstream : ')
        ret.append(repr(self.upstream))
        ret.append(',\n    under_relax : ')
        ret.append(repr(self.under_relax))
        ret.append(',\n    comp_relax : ')
        ret.append(repr(self.comp_relax))
        ret.append(',\n    avs : ')
        ret.append(repr(self.avs))
        ret.append(',\n    bvs : ')
        ret.append(repr(self.bvs))
        ret.append(',\n    uvs : ')
        ret.append(repr(self.uvs))
        ret.append(',\n    resvs : ')
        ret.append(repr(self.resvs))
        ret.append(',\n    afvs : ')
        ret.append(repr(self.afvs))
        ret.append(',\n    restol_vs : ')
        ret.append(repr(self.restol_vs))
        ret.append(',\n    deltol_vs : ')
        ret.append(repr(self.deltol_vs))
        ret.append(',\n    iavs : ')
        ret.append(repr(self.iavs))
        ret.append(',\n    javs : ')
        ret.append(repr(self.javs))
        ret.append(',\n    iafvs : ')
        ret.append(repr(self.iafvs))
        ret.append(',\n    jafvs : ')
        ret.append(repr(self.jafvs))
        ret.append(',\n    iafdvs : ')
        ret.append(repr(self.iafdvs))
        ret.append(',\n    isymvs : ')
        ret.append(repr(self.isymvs))
        ret.append(',\n    lordervs : ')
        ret.append(repr(self.lordervs))
        ret.append(',\n    invordvs : ')
        ret.append(repr(self.invordvs))
        ret.append(',\n    mnjavs : ')
        ret.append(repr(self.mnjavs))
        ret.append(',\n    mnjafvs : ')
        ret.append(repr(self.mnjafvs))
        ret.append(',\n    njavs : ')
        ret.append(repr(self.njavs))
        ret.append(',\n    njafvs : ')
        ret.append(repr(self.njafvs))
        ret.append(',\n    level_vs : ')
        ret.append(repr(self.level_vs))
        ret.append(',\n    msolvit_vs : ')
        ret.append(repr(self.msolvit_vs))
        ret.append(',\n    idetail_vs : ')
        ret.append(repr(self.idetail_vs))
        ret.append(',\n    rcm_ordering_vs : ')
        ret.append(repr(self.rcm_ordering_vs))
        ret.append(',\n    rwork : ')
        ret.append(repr(self.rwork))
        ret.append(',\n    rnorm : ')
        ret.append(repr(self.rnorm))
        ret.append(',\n    rmupdate : ')
        ret.append(repr(self.rmupdate))
        ret.append(',\n    iwork : ')
        ret.append(repr(self.iwork))
        ret.append(',\n    itsolv : ')
        ret.append(repr(self.itsolv))
        ret.append(',\n    lwork : ')
        ret.append(repr(self.lwork))
        ret.append(',\n    skip : ')
        ret.append(repr(self.skip))
        ret.append(',\n    nskip : ')
        ret.append(repr(self.nskip))
        ret.append(',\n    chemical_water : ')
        ret.append(repr(self.chemical_water))
        ret.append(',\n    qwater : ')
        ret.append(repr(self.qwater))
        ret.append(',\n    rsrt_cnt : ')
        ret.append(repr(self.rsrt_cnt))
        ret.append(',\n    irsrt : ')
        ret.append(repr(self.irsrt))
        ret.append(',\n    backup_frequency : ')
        ret.append(repr(self.backup_frequency))
        ret.append(',\n    restart_sim : ')
        ret.append(repr(self.restart_sim))
        ret.append(',\n    ovr_sat : ')
        ret.append(repr(self.ovr_sat))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

gen = Gen()

class Parm(f90wrap.runtime.FortranModule):
    """
    Module parm
    
    
    Defined at ../src/parm.f lines 1-64
    
    """
    @f90wrap.runtime.register_class("polanyi")
    class polanyi(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=polanyi)
        
        
        Defined at ../src/parm.f lines 57-62
        
        """
        def __init__(self, handle=None):
            """
            self = Polanyi()
            
            
            Defined at ../src/parm.f lines 57-62
            
            
            Returns
            -------
            this : Polanyi
            	Object to be constructed
            
            
            Automatically generated constructor for polanyi
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _min3p.f90wrap_polanyi_initialise()
        
        def __del__(self):
            """
            Destructor for class Polanyi
            
            
            Defined at ../src/parm.f lines 57-62
            
            Parameters
            ----------
            this : Polanyi
            	Object to be destructed
            
            
            Automatically generated destructor for polanyi
            """
            if self._alloc:
                _min3p.f90wrap_polanyi_finalise(this=self._handle)
        
        _dt_array_initialisers = []
        
    
    @property
    def type_i4(self):
        """
        Element type_i4 ftype=integer pytype=int
        
        
        Defined at ../src/parm.f line 10
        
        """
        return _min3p.f90wrap_parm__get__type_i4()
    
    @property
    def type_i2(self):
        """
        Element type_i2 ftype=integer pytype=int
        
        
        Defined at ../src/parm.f line 11
        
        """
        return _min3p.f90wrap_parm__get__type_i2()
    
    @property
    def type_i1(self):
        """
        Element type_i1 ftype=integer pytype=int
        
        
        Defined at ../src/parm.f line 12
        
        """
        return _min3p.f90wrap_parm__get__type_i1()
    
    @property
    def type_r4(self):
        """
        Element type_r4 ftype=integer pytype=int
        
        
        Defined at ../src/parm.f line 13
        
        """
        return _min3p.f90wrap_parm__get__type_r4()
    
    @property
    def type_r8(self):
        """
        Element type_r8 ftype=integer pytype=int
        
        
        Defined at ../src/parm.f line 15
        
        """
        return _min3p.f90wrap_parm__get__type_r8()
    
    @property
    def ncon(self):
        """
        Element ncon ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/parm.f line 35
        
        """
        return _min3p.f90wrap_parm__get__ncon()
    
    @property
    def maxndr(self):
        """
        Element maxndr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/parm.f line 36
        
        """
        return _min3p.f90wrap_parm__get__maxndr()
    
    @property
    def maxnpr(self):
        """
        Element maxnpr ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/parm.f line 37
        
        """
        return _min3p.f90wrap_parm__get__maxnpr()
    
    @property
    def maxnrc(self):
        """
        Element maxnrc ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/parm.f line 38
        
        """
        return _min3p.f90wrap_parm__get__maxnrc()
    
    @property
    def maxnor(self):
        """
        Element maxnor ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/parm.f line 39
        
        """
        return _min3p.f90wrap_parm__get__maxnor()
    
    def __str__(self):
        ret = ['<parm>{\n']
        ret.append('    type_i4 : ')
        ret.append(repr(self.type_i4))
        ret.append(',\n    type_i2 : ')
        ret.append(repr(self.type_i2))
        ret.append(',\n    type_i1 : ')
        ret.append(repr(self.type_i1))
        ret.append(',\n    type_r4 : ')
        ret.append(repr(self.type_r4))
        ret.append(',\n    type_r8 : ')
        ret.append(repr(self.type_r8))
        ret.append(',\n    ncon : ')
        ret.append(repr(self.ncon))
        ret.append(',\n    maxndr : ')
        ret.append(repr(self.maxndr))
        ret.append(',\n    maxnpr : ')
        ret.append(repr(self.maxnpr))
        ret.append(',\n    maxnrc : ')
        ret.append(repr(self.maxnrc))
        ret.append(',\n    maxnor : ')
        ret.append(repr(self.maxnor))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

parm = Parm()

class Phys(f90wrap.runtime.FortranModule):
    """
    Module phys
    
    
    Defined at ../src/phys.f lines 1-181
    
    """
    @property
    def por(self):
        """
        Element por ftype=real (type_r4) pytype=float
        
        
        Defined at ../src/phys.f line 25
        
        """
        return _min3p.f90wrap_phys__get__por()
    
    @por.setter
    def por(self, por):
        _min3p.f90wrap_phys__set__por(por)
    
    @property
    def pvol(self):
        """
        Element pvol ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 80
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__pvol(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            pvol = self._arrays[array_handle]
        else:
            pvol = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__pvol)
            self._arrays[array_handle] = pvol
        return pvol
    
    @pvol.setter
    def pvol(self, pvol):
        self.pvol[...] = pvol
    
    @property
    def condxx(self):
        """
        Element condxx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 81
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__condxx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            condxx = self._arrays[array_handle]
        else:
            condxx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__condxx)
            self._arrays[array_handle] = condxx
        return condxx
    
    @condxx.setter
    def condxx(self, condxx):
        self.condxx[...] = condxx
    
    @property
    def condyy(self):
        """
        Element condyy ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 82
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__condyy(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            condyy = self._arrays[array_handle]
        else:
            condyy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__condyy)
            self._arrays[array_handle] = condyy
        return condyy
    
    @condyy.setter
    def condyy(self, condyy):
        self.condyy[...] = condyy
    
    @property
    def condzz(self):
        """
        Element condzz ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 83
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__condzz(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            condzz = self._arrays[array_handle]
        else:
            condzz = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__condzz)
            self._arrays[array_handle] = condzz
        return condzz
    
    @condzz.setter
    def condzz(self, condzz):
        self.condzz[...] = condzz
    
    @property
    def permx(self):
        """
        Element permx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 84
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__permx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            permx = self._arrays[array_handle]
        else:
            permx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__permx)
            self._arrays[array_handle] = permx
        return permx
    
    @permx.setter
    def permx(self, permx):
        self.permx[...] = permx
    
    @property
    def permy(self):
        """
        Element permy ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 85
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__permy(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            permy = self._arrays[array_handle]
        else:
            permy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__permy)
            self._arrays[array_handle] = permy
        return permy
    
    @permy.setter
    def permy(self, permy):
        self.permy[...] = permy
    
    @property
    def permz(self):
        """
        Element permz ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 86
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__permz(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            permz = self._arrays[array_handle]
        else:
            permz = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__permz)
            self._arrays[array_handle] = permz
        return permz
    
    @permz.setter
    def permz(self, permz):
        self.permz[...] = permz
    
    @property
    def spstor(self):
        """
        Element spstor ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 87
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__spstor(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            spstor = self._arrays[array_handle]
        else:
            spstor = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__spstor)
            self._arrays[array_handle] = spstor
        return spstor
    
    @spstor.setter
    def spstor(self, spstor):
        self.spstor[...] = spstor
    
    @property
    def swr(self):
        """
        Element swr ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 88
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__swr(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            swr = self._arrays[array_handle]
        else:
            swr = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__swr)
            self._arrays[array_handle] = swr
        return swr
    
    @swr.setter
    def swr(self, swr):
        self.swr[...] = swr
    
    @property
    def spalpha(self):
        """
        Element spalpha ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 89
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__spalpha(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            spalpha = self._arrays[array_handle]
        else:
            spalpha = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__spalpha)
            self._arrays[array_handle] = spalpha
        return spalpha
    
    @spalpha.setter
    def spalpha(self, spalpha):
        self.spalpha[...] = spalpha
    
    @property
    def spbeta(self):
        """
        Element spbeta ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 90
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__spbeta(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            spbeta = self._arrays[array_handle]
        else:
            spbeta = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__spbeta)
            self._arrays[array_handle] = spbeta
        return spbeta
    
    @spbeta.setter
    def spbeta(self, spbeta):
        self.spbeta[...] = spbeta
    
    @property
    def spgamma(self):
        """
        Element spgamma ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 91
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__spgamma(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            spgamma = self._arrays[array_handle]
        else:
            spgamma = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__spgamma)
            self._arrays[array_handle] = spgamma
        return spgamma
    
    @spgamma.setter
    def spgamma(self, spgamma):
        self.spgamma[...] = spgamma
    
    @property
    def expn(self):
        """
        Element expn ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 92
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__expn(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            expn = self._arrays[array_handle]
        else:
            expn = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__expn)
            self._arrays[array_handle] = expn
        return expn
    
    @expn.setter
    def expn(self, expn):
        self.expn[...] = expn
    
    @property
    def aentry(self):
        """
        Element aentry ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 93
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__aentry(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            aentry = self._arrays[array_handle]
        else:
            aentry = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__aentry)
            self._arrays[array_handle] = aentry
        return aentry
    
    @aentry.setter
    def aentry(self, aentry):
        self.aentry[...] = aentry
    
    @property
    def satwdry(self):
        """
        Element satwdry ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 94
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__satwdry(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            satwdry = self._arrays[array_handle]
        else:
            satwdry = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__satwdry)
            self._arrays[array_handle] = satwdry
        return satwdry
    
    @satwdry.setter
    def satwdry(self, satwdry):
        self.satwdry[...] = satwdry
    
    @property
    def h1dry(self):
        """
        Element h1dry ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 95
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__h1dry(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            h1dry = self._arrays[array_handle]
        else:
            h1dry = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__h1dry)
            self._arrays[array_handle] = h1dry
        return h1dry
    
    @h1dry.setter
    def h1dry(self, h1dry):
        self.h1dry[...] = h1dry
    
    @property
    def nzn(self):
        """
        Element nzn ftype=integer (type_i4) pytype=int
        
        
        Defined at ../src/phys.f line 97
        
        """
        return _min3p.f90wrap_phys__get__nzn()
    
    @nzn.setter
    def nzn(self, nzn):
        _min3p.f90wrap_phys__set__nzn(nzn)
    
    @property
    def permeability_field(self):
        """
        Element permeability_field ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 99
        
        """
        return _min3p.f90wrap_phys__get__permeability_field()
    
    @permeability_field.setter
    def permeability_field(self, permeability_field):
        _min3p.f90wrap_phys__set__permeability_field(permeability_field)
    
    @property
    def randomdistrib_k(self):
        """
        Element randomdistrib_k ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 100
        
        """
        return _min3p.f90wrap_phys__get__randomdistrib_k()
    
    @randomdistrib_k.setter
    def randomdistrib_k(self, randomdistrib_k):
        _min3p.f90wrap_phys__set__randomdistrib_k(randomdistrib_k)
    
    @property
    def pure_evaporation(self):
        """
        Element pure_evaporation ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 101
        
        """
        return _min3p.f90wrap_phys__get__pure_evaporation()
    
    @pure_evaporation.setter
    def pure_evaporation(self, pure_evaporation):
        _min3p.f90wrap_phys__set__pure_evaporation(pure_evaporation)
    
    @property
    def oil_saturation(self):
        """
        Element oil_saturation ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 102
        
        """
        return _min3p.f90wrap_phys__get__oil_saturation()
    
    @oil_saturation.setter
    def oil_saturation(self, oil_saturation):
        _min3p.f90wrap_phys__set__oil_saturation(oil_saturation)
    
    @property
    def disx(self):
        """
        Element disx ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 120
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__disx(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            disx = self._arrays[array_handle]
        else:
            disx = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__disx)
            self._arrays[array_handle] = disx
        return disx
    
    @disx.setter
    def disx(self, disx):
        self.disx[...] = disx
    
    @property
    def disy(self):
        """
        Element disy ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 121
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__disy(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            disy = self._arrays[array_handle]
        else:
            disy = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__disy)
            self._arrays[array_handle] = disy
        return disy
    
    @disy.setter
    def disy(self, disy):
        self.disy[...] = disy
    
    @property
    def disz(self):
        """
        Element disz ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 122
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__disz(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            disz = self._arrays[array_handle]
        else:
            disz = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__disz)
            self._arrays[array_handle] = disz
        return disz
    
    @disz.setter
    def disz(self, disz):
        self.disz[...] = disz
    
    @property
    def diff_a(self):
        """
        Element diff_a ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 124
        
        """
        return _min3p.f90wrap_phys__get__diff_a()
    
    @diff_a.setter
    def diff_a(self, diff_a):
        _min3p.f90wrap_phys__set__diff_a(diff_a)
    
    @property
    def diff_g(self):
        """
        Element diff_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 125
        
        """
        return _min3p.f90wrap_phys__get__diff_g()
    
    @diff_g.setter
    def diff_g(self, diff_g):
        _min3p.f90wrap_phys__set__diff_g(diff_g)
    
    @property
    def dens_h2o(self):
        """
        Element dens_h2o ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 159
        
        """
        return _min3p.f90wrap_phys__get__dens_h2o()
    
    @dens_h2o.setter
    def dens_h2o(self, dens_h2o):
        _min3p.f90wrap_phys__set__dens_h2o(dens_h2o)
    
    @property
    def visc_h2o(self):
        """
        Element visc_h2o ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 160
        
        """
        return _min3p.f90wrap_phys__get__visc_h2o()
    
    @visc_h2o.setter
    def visc_h2o(self, visc_h2o):
        _min3p.f90wrap_phys__set__visc_h2o(visc_h2o)
    
    @property
    def dens_gcnst(self):
        """
        Element dens_gcnst ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 162
        
        """
        return _min3p.f90wrap_phys__get__dens_gcnst()
    
    @dens_gcnst.setter
    def dens_gcnst(self, dens_gcnst):
        _min3p.f90wrap_phys__set__dens_gcnst(dens_gcnst)
    
    @property
    def visc_gcnst(self):
        """
        Element visc_gcnst ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 163
        
        """
        return _min3p.f90wrap_phys__get__visc_gcnst()
    
    @visc_gcnst.setter
    def visc_gcnst(self, visc_gcnst):
        _min3p.f90wrap_phys__set__visc_gcnst(visc_gcnst)
    
    @property
    def theta_diff(self):
        """
        Element theta_diff ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 165
        
        """
        return _min3p.f90wrap_phys__get__theta_diff()
    
    @theta_diff.setter
    def theta_diff(self, theta_diff):
        _min3p.f90wrap_phys__set__theta_diff(theta_diff)
    
    @property
    def dens_g(self):
        """
        Element dens_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 167
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__dens_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            dens_g = self._arrays[array_handle]
        else:
            dens_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__dens_g)
            self._arrays[array_handle] = dens_g
        return dens_g
    
    @dens_g.setter
    def dens_g(self, dens_g):
        self.dens_g[...] = dens_g
    
    @property
    def visc_g(self):
        """
        Element visc_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 168
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__visc_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            visc_g = self._arrays[array_handle]
        else:
            visc_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__visc_g)
            self._arrays[array_handle] = visc_g
        return visc_g
    
    @visc_g.setter
    def visc_g(self, visc_g):
        self.visc_g[...] = visc_g
    
    @property
    def mdens_g(self):
        """
        Element mdens_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 169
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__mdens_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            mdens_g = self._arrays[array_handle]
        else:
            mdens_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__mdens_g)
            self._arrays[array_handle] = mdens_g
        return mdens_g
    
    @mdens_g.setter
    def mdens_g(self, mdens_g):
        self.mdens_g[...] = mdens_g
    
    @property
    def update_dens_g(self):
        """
        Element update_dens_g ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 171
        
        """
        return _min3p.f90wrap_phys__get__update_dens_g()
    
    @update_dens_g.setter
    def update_dens_g(self, update_dens_g):
        _min3p.f90wrap_phys__set__update_dens_g(update_dens_g)
    
    @property
    def blanc_diff_g(self):
        """
        Element blanc_diff_g ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 172
        
        """
        return _min3p.f90wrap_phys__get__blanc_diff_g()
    
    @blanc_diff_g.setter
    def blanc_diff_g(self, blanc_diff_g):
        _min3p.f90wrap_phys__set__blanc_diff_g(blanc_diff_g)
    
    @property
    def diff_press(self):
        """
        Element diff_press ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 173
        
        """
        return _min3p.f90wrap_phys__get__diff_press()
    
    @diff_press.setter
    def diff_press(self, diff_press):
        _min3p.f90wrap_phys__set__diff_press(diff_press)
    
    @property
    def diff_temp(self):
        """
        Element diff_temp ftype=logical pytype=bool
        
        
        Defined at ../src/phys.f line 174
        
        """
        return _min3p.f90wrap_phys__get__diff_temp()
    
    @diff_temp.setter
    def diff_temp(self, diff_temp):
        _min3p.f90wrap_phys__set__diff_temp(diff_temp)
    
    @property
    def visc_comp_g(self):
        """
        Element visc_comp_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 178
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__visc_comp_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            visc_comp_g = self._arrays[array_handle]
        else:
            visc_comp_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__visc_comp_g)
            self._arrays[array_handle] = visc_comp_g
        return visc_comp_g
    
    @visc_comp_g.setter
    def visc_comp_g(self, visc_comp_g):
        self.visc_comp_g[...] = visc_comp_g
    
    @property
    def diff_bin_g(self):
        """
        Element diff_bin_g ftype=real (type_r8) pytype=float
        
        
        Defined at ../src/phys.f line 179
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_phys__array__diff_bin_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            diff_bin_g = self._arrays[array_handle]
        else:
            diff_bin_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_phys__array__diff_bin_g)
            self._arrays[array_handle] = diff_bin_g
        return diff_bin_g
    
    @diff_bin_g.setter
    def diff_bin_g(self, diff_bin_g):
        self.diff_bin_g[...] = diff_bin_g
    
    def __str__(self):
        ret = ['<phys>{\n']
        ret.append('    por : ')
        ret.append(repr(self.por))
        ret.append(',\n    pvol : ')
        ret.append(repr(self.pvol))
        ret.append(',\n    condxx : ')
        ret.append(repr(self.condxx))
        ret.append(',\n    condyy : ')
        ret.append(repr(self.condyy))
        ret.append(',\n    condzz : ')
        ret.append(repr(self.condzz))
        ret.append(',\n    permx : ')
        ret.append(repr(self.permx))
        ret.append(',\n    permy : ')
        ret.append(repr(self.permy))
        ret.append(',\n    permz : ')
        ret.append(repr(self.permz))
        ret.append(',\n    spstor : ')
        ret.append(repr(self.spstor))
        ret.append(',\n    swr : ')
        ret.append(repr(self.swr))
        ret.append(',\n    spalpha : ')
        ret.append(repr(self.spalpha))
        ret.append(',\n    spbeta : ')
        ret.append(repr(self.spbeta))
        ret.append(',\n    spgamma : ')
        ret.append(repr(self.spgamma))
        ret.append(',\n    expn : ')
        ret.append(repr(self.expn))
        ret.append(',\n    aentry : ')
        ret.append(repr(self.aentry))
        ret.append(',\n    satwdry : ')
        ret.append(repr(self.satwdry))
        ret.append(',\n    h1dry : ')
        ret.append(repr(self.h1dry))
        ret.append(',\n    nzn : ')
        ret.append(repr(self.nzn))
        ret.append(',\n    permeability_field : ')
        ret.append(repr(self.permeability_field))
        ret.append(',\n    randomdistrib_k : ')
        ret.append(repr(self.randomdistrib_k))
        ret.append(',\n    pure_evaporation : ')
        ret.append(repr(self.pure_evaporation))
        ret.append(',\n    oil_saturation : ')
        ret.append(repr(self.oil_saturation))
        ret.append(',\n    disx : ')
        ret.append(repr(self.disx))
        ret.append(',\n    disy : ')
        ret.append(repr(self.disy))
        ret.append(',\n    disz : ')
        ret.append(repr(self.disz))
        ret.append(',\n    diff_a : ')
        ret.append(repr(self.diff_a))
        ret.append(',\n    diff_g : ')
        ret.append(repr(self.diff_g))
        ret.append(',\n    dens_h2o : ')
        ret.append(repr(self.dens_h2o))
        ret.append(',\n    visc_h2o : ')
        ret.append(repr(self.visc_h2o))
        ret.append(',\n    dens_gcnst : ')
        ret.append(repr(self.dens_gcnst))
        ret.append(',\n    visc_gcnst : ')
        ret.append(repr(self.visc_gcnst))
        ret.append(',\n    theta_diff : ')
        ret.append(repr(self.theta_diff))
        ret.append(',\n    dens_g : ')
        ret.append(repr(self.dens_g))
        ret.append(',\n    visc_g : ')
        ret.append(repr(self.visc_g))
        ret.append(',\n    mdens_g : ')
        ret.append(repr(self.mdens_g))
        ret.append(',\n    update_dens_g : ')
        ret.append(repr(self.update_dens_g))
        ret.append(',\n    blanc_diff_g : ')
        ret.append(repr(self.blanc_diff_g))
        ret.append(',\n    diff_press : ')
        ret.append(repr(self.diff_press))
        ret.append(',\n    diff_temp : ')
        ret.append(repr(self.diff_temp))
        ret.append(',\n    visc_comp_g : ')
        ret.append(repr(self.visc_comp_g))
        ret.append(',\n    diff_bin_g : ')
        ret.append(repr(self.diff_bin_g))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

phys = Phys()

class Root_Modu(f90wrap.runtime.FortranModule):
    """
    Module root_modu
    
    
    Defined at ../src/root_modu.f lines 1-60
    
    """
    @property
    def rsd_archi(self):
        """
        Element rsd_archi ftype=real(kind=c_double) pytype=float
        
        
        Defined at ../src/root_modu.f line 7
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__rsd_archi(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rsd_archi = self._arrays[array_handle]
        else:
            rsd_archi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__rsd_archi)
            self._arrays[array_handle] = rsd_archi
        return rsd_archi
    
    @rsd_archi.setter
    def rsd_archi(self, rsd_archi):
        self.rsd_archi[...] = rsd_archi
    
    @property
    def rsd_bonsens(self):
        """
        Element rsd_bonsens ftype=real(kind=c_double) pytype=float
        
        
        Defined at ../src/root_modu.f line 8
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__rsd_bonsens(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            rsd_bonsens = self._arrays[array_handle]
        else:
            rsd_bonsens = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__rsd_bonsens)
            self._arrays[array_handle] = rsd_bonsens
        return rsd_bonsens
    
    @rsd_bonsens.setter
    def rsd_bonsens(self, rsd_bonsens):
        self.rsd_bonsens[...] = rsd_bonsens
    
    @property
    def x_g(self):
        """
        Element x_g ftype=real(kind=c_float) pytype=float
        
        
        Defined at ../src/root_modu.f line 9
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__x_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            x_g = self._arrays[array_handle]
        else:
            x_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__x_g)
            self._arrays[array_handle] = x_g
        return x_g
    
    @x_g.setter
    def x_g(self, x_g):
        self.x_g[...] = x_g
    
    @property
    def y_g(self):
        """
        Element y_g ftype=real(kind=c_float) pytype=float
        
        
        Defined at ../src/root_modu.f line 10
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__y_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            y_g = self._arrays[array_handle]
        else:
            y_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__y_g)
            self._arrays[array_handle] = y_g
        return y_g
    
    @y_g.setter
    def y_g(self, y_g):
        self.y_g[...] = y_g
    
    @property
    def z_g(self):
        """
        Element z_g ftype=real(kind=c_float) pytype=float
        
        
        Defined at ../src/root_modu.f line 11
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__z_g(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            z_g = self._arrays[array_handle]
        else:
            z_g = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__z_g)
            self._arrays[array_handle] = z_g
        return z_g
    
    @z_g.setter
    def z_g(self, z_g):
        self.z_g[...] = z_g
    
    @property
    def humidity(self):
        """
        Element humidity ftype=real(kind=c_float) pytype=float
        
        
        Defined at ../src/root_modu.f line 12
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _min3p.f90wrap_root_modu__array__humidity(f90wrap.runtime.empty_handle)
        if array_handle in self._arrays:
            humidity = self._arrays[array_handle]
        else:
            humidity = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    f90wrap.runtime.empty_handle,
                                    _min3p.f90wrap_root_modu__array__humidity)
            self._arrays[array_handle] = humidity
        return humidity
    
    @humidity.setter
    def humidity(self, humidity):
        self.humidity[...] = humidity
    
    def __str__(self):
        ret = ['<root_modu>{\n']
        ret.append('    rsd_archi : ')
        ret.append(repr(self.rsd_archi))
        ret.append(',\n    rsd_bonsens : ')
        ret.append(repr(self.rsd_bonsens))
        ret.append(',\n    x_g : ')
        ret.append(repr(self.x_g))
        ret.append(',\n    y_g : ')
        ret.append(repr(self.y_g))
        ret.append(',\n    z_g : ')
        ret.append(repr(self.z_g))
        ret.append(',\n    humidity : ')
        ret.append(repr(self.humidity))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

root_modu = Root_Modu()

def alkcalc(alk_carb, alk_noncarb, alk_tot, alk_carb_mg, alk_noncarb_mg, \
    alk_tot_mg, alkfacc, alkfacx, c, cx, iax, jax, nc, nx, namec, namex):
    """
    alkcalc(alk_carb, alk_noncarb, alk_tot, alk_carb_mg, alk_noncarb_mg, alk_tot_mg, \
        alkfacc, alkfacx, c, cx, iax, jax, nc, nx, namec, namex)
    
    
    Defined at ../src/alkcalc.f lines 74-134
    
    Parameters
    ----------
    alk_carb : float
    alk_noncarb : float
    alk_tot : float
    alk_carb_mg : float
    alk_noncarb_mg : float
    alk_tot_mg : float
    alkfacc : float
    alkfacx : float
    c : float
    cx : float
    iax : int
    jax : int
    nc : int
    nx : int
    namec : int
    namex : int
    
    """
    _min3p.f90wrap_alkcalc(alk_carb=alk_carb, alk_noncarb=alk_noncarb, \
        alk_tot=alk_tot, alk_carb_mg=alk_carb_mg, alk_noncarb_mg=alk_noncarb_mg, \
        alk_tot_mg=alk_tot_mg, alkfacc=alkfacc, alkfacx=alkfacx, c=c, cx=cx, \
        iax=iax, jax=jax, nc=nc, nx=nx, namec=namec, namex=namex)

def alpha(im, ivol):
    """
    alpha(im, ivol)
    
    
    Defined at ../src/alpha.f lines 2-62
    
    Parameters
    ----------
    im : int
    ivol : int
    
    """
    _min3p.f90wrap_alpha(im=im, ivol=ivol)

def dalpha(im, ivol):
    """
    dalpha(im, ivol)
    
    
    Defined at ../src/alpha.f lines 65-103
    
    Parameters
    ----------
    im : int
    ivol : int
    
    """
    _min3p.f90wrap_dalpha(im=im, ivol=ivol)

def andorra(nsb, component_type, iasb, jasb, nc, cnew, csb, nelec, nsites, \
    namesb, namec, sorption_group, chargesb, xnusb, nsites2, chargec, \
    sorption_type, cap1, cap2, site_mass, site_area, totpsi, calcpsi, strionsb, \
    surfacensb):
    """
    andorra(nsb, component_type, iasb, jasb, nc, cnew, csb, nelec, nsites, namesb, \
        namec, sorption_group, chargesb, xnusb, nsites2, chargec, sorption_type, \
        cap1, cap2, site_mass, site_area, totpsi, calcpsi, strionsb, surfacensb)
    
    
    Defined at ../src/andorra.f lines 269-643
    
    Parameters
    ----------
    nsb : int
    component_type : float
    iasb : int
    jasb : int
    nc : int
    cnew : float
    csb : float
    nelec : int
    nsites : int
    namesb : int
    namec : int
    sorption_group : float
    chargesb : float
    xnusb : float
    nsites2 : int
    chargec : float
    sorption_type : float
    cap1 : float
    cap2 : float
    site_mass : float
    site_area : float
    totpsi : float
    calcpsi : float
    strionsb : float
    surfacensb : float
    
    """
    _min3p.f90wrap_andorra(nsb=nsb, component_type=component_type, iasb=iasb, \
        jasb=jasb, nc=nc, cnew=cnew, csb=csb, nelec=nelec, nsites=nsites, \
        namesb=namesb, namec=namec, sorption_group=sorption_group, \
        chargesb=chargesb, xnusb=xnusb, nsites2=nsites2, chargec=chargec, \
        sorption_type=sorption_type, cap1=cap1, cap2=cap2, site_mass=site_mass, \
        site_area=site_area, totpsi=totpsi, calcpsi=calcpsi, strionsb=strionsb, \
        surfacensb=surfacensb)

def aratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, jbl, \
    ivol):
    """
    aratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, jbl, \
        ivol)
    
    
    Defined at ../src/aratemin.f lines 177-581
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    im : int
    jbl : int
    ivol : int
    
    """
    _min3p.f90wrap_aratemin(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        ratem=ratem, phim=phim, phimold=phimold, aream=aream, im=im, jbl=jbl, \
        ivol=ivol)

def atotconc(c, cx, jbl):
    """
    atotconc(c, cx, jbl)
    
    
    Defined at ../src/atotconc.f lines 75-182
    
    Parameters
    ----------
    c : float
    cx : float
    jbl : int
    
    """
    _min3p.f90wrap_atotconc(c=c, cx=cx, jbl=jbl)

def batreac():
    """
    batreac()
    
    
    Defined at ../src/batreac.f lines 166-327
    
    
    """
    _min3p.f90wrap_batreac()

def binmatevap():
    """
    binmatevap()
    
    
    Defined at ../src/binmatevap.f lines 25-45
    
    
    """
    _min3p.f90wrap_binmatevap()

def binmattransp():
    """
    binmattransp()
    
    
    Defined at ../src/binmattransp.f lines 25-46
    
    
    """
    _min3p.f90wrap_binmattransp()

def cbalance(c, cx, zbal, zpos, zneg):
    """
    cbalance(c, cx, zbal, zpos, zneg)
    
    
    Defined at ../src/cbalance.f lines 50-90
    
    Parameters
    ----------
    c : float
    cx : float
    zbal : float
    zpos : float
    zneg : float
    
    """
    _min3p.f90wrap_cbalance(c=c, cx=cx, zbal=zbal, zpos=zpos, zneg=zneg)

def checkerr(ierr, label, ilog):
    """
    checkerr(ierr, label, ilog)
    
    
    Defined at ../src/checkerr.f lines 1-26
    
    Parameters
    ----------
    ierr : int
    label : str
    ilog : int
    
    """
    _min3p.f90wrap_checkerr(ierr=ierr, label=label, ilog=ilog)

def checksat():
    """
    checksat()
    
    
    Defined at ../src/checksat.f lines 95-172
    
    
    """
    _min3p.f90wrap_checksat()

def chrgcorr():
    """
    chrgcorr()
    
    
    Defined at ../src/chrgcorr.f lines 69-125
    
    
    """
    _min3p.f90wrap_chrgcorr()

def cliqdisp(nx, ny, nz, ix, iy, iz, fvpair, npair, aread, d, half_cells, nmax, \
    idbg, dd):
    """
    cliqdisp(nx, ny, nz, ix, iy, iz, fvpair, npair, aread, d, half_cells, nmax, \
        idbg, dd)
    
    
    Defined at ../src/cliqdisp.f lines 110-327
    
    Parameters
    ----------
    nx : int
    ny : int
    nz : int
    ix : int
    iy : int
    iz : int
    fvpair : int array
    npair : int array
    aread : float
    d : float
    half_cells : bool
    nmax : int
    idbg : int
    dd : float
    
    """
    _min3p.f90wrap_cliqdisp(nx=nx, ny=ny, nz=nz, ix=ix, iy=iy, iz=iz, fvpair=fvpair, \
        npair=npair, aread=aread, d=d, half_cells=half_cells, nmax=nmax, idbg=idbg, \
        dd=dd)

def clsgfls():
    """
    clsgfls()
    
    
    Defined at ../src/clsgfls.f lines 145-242
    
    
    """
    _min3p.f90wrap_clsgfls()

def clstpfls():
    """
    clstpfls()
    
    
    Defined at ../src/clstpfls.f lines 89-126
    
    
    """
    _min3p.f90wrap_clstpfls()

def comptotc(totc):
    """
    comptotc(totc)
    
    
    Defined at ../src/comptotc.f lines 56-81
    
    Parameters
    ----------
    totc : float
    
    """
    _min3p.f90wrap_comptotc(totc=totc)

def concsort(conc, gamma, name, n):
    """
    concsort(conc, gamma, name, n)
    
    
    Defined at ../src/concsort.f lines 61-91
    
    Parameters
    ----------
    conc : float
    gamma : float
    name : int
    n : int
    
    """
    _min3p.f90wrap_concsort(conc=conc, gamma=gamma, name=name, n=n)

def constnts():
    """
    constnts()
    
    
    Defined at ../src/constnts.f lines 35-63
    
    
    """
    _min3p.f90wrap_constnts()

def cvolume():
    """
    cvolume()
    
    
    Defined at ../src/cvolume.f lines 49-88
    
    
    """
    _min3p.f90wrap_cvolume()

def dandorra(nsb, component_type, iasb, jasb, nc, cnew, dcsb, nelec, nsites, \
    namesb, namec, sorption_group, chargesb, xnusb, nsites2, chargec, \
    sorption_type, cap1, cap2, site_mass, site_area, dtotpsi, dcalcpsi, \
    strionsb, surfacensb, cinc, drtinc):
    """
    dandorra(nsb, component_type, iasb, jasb, nc, cnew, dcsb, nelec, nsites, namesb, \
        namec, sorption_group, chargesb, xnusb, nsites2, chargec, sorption_type, \
        cap1, cap2, site_mass, site_area, dtotpsi, dcalcpsi, strionsb, surfacensb, \
        cinc, drtinc)
    
    
    Defined at ../src/dandorra.f lines 270-673
    
    Parameters
    ----------
    nsb : int
    component_type : float
    iasb : int
    jasb : int
    nc : int
    cnew : float
    dcsb : float
    nelec : int
    nsites : int
    namesb : int
    namec : int
    sorption_group : float
    chargesb : float
    xnusb : float
    nsites2 : int
    chargec : float
    sorption_type : float
    cap1 : float
    cap2 : float
    site_mass : float
    site_area : float
    dtotpsi : float
    dcalcpsi : float
    strionsb : float
    surfacensb : float
    cinc : float
    drtinc : float
    
    """
    _min3p.f90wrap_dandorra(nsb=nsb, component_type=component_type, iasb=iasb, \
        jasb=jasb, nc=nc, cnew=cnew, dcsb=dcsb, nelec=nelec, nsites=nsites, \
        namesb=namesb, namec=namec, sorption_group=sorption_group, \
        chargesb=chargesb, xnusb=xnusb, nsites2=nsites2, chargec=chargec, \
        sorption_type=sorption_type, cap1=cap1, cap2=cap2, site_mass=site_mass, \
        site_area=site_area, dtotpsi=dtotpsi, dcalcpsi=dcalcpsi, strionsb=strionsb, \
        surfacensb=surfacensb, cinc=cinc, drtinc=drtinc)

def datstr_1():
    """
    datstr_1()
    
    
    Defined at ../src/datstr_1.f lines 78-264
    
    
    """
    _min3p.f90wrap_datstr_1()

def datstr_n():
    """
    datstr_n()
    
    
    Defined at ../src/datstr_n.f lines 77-246
    
    
    """
    _min3p.f90wrap_datstr_n()

def dgefam(a, lda, n, ipvt, info):
    """
    dgefam(a, lda, n, ipvt, info)
    
    
    Defined at ../src/dgefam.f lines 1-119
    
    Parameters
    ----------
    a : unknown array
    lda : int
    n : int
    ipvt : int array
    info : int
    
    """
    _min3p.f90wrap_dgefam(a=a, lda=lda, n=n, ipvt=ipvt, info=info)

def dgeslm(a, lda, n, ipvt, b):
    """
    dgeslm(a, lda, n, ipvt, b)
    
    
    Defined at ../src/dgeslm.f lines 1-91
    
    Parameters
    ----------
    a : unknown array
    lda : int
    n : int
    ipvt : int array
    b : unknown array
    
    """
    _min3p.f90wrap_dgeslm(a=a, lda=lda, n=n, ipvt=ipvt, b=b)

def dgm_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, relp, \
    tauijx, gporx, delta_ijx, small, factor, ipvt, ludecomp, fmat, dgm_dgflux):
    """
    dgm_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, relp, \
        tauijx, gporx, delta_ijx, small, factor, ipvt, ludecomp, fmat, dgm_dgflux)
    
    
    Defined at ../src/dgm_dfluxdg.f lines 139-336
    
    Parameters
    ----------
    c_i : float
    c_j : float
    dc_i : float
    dmolfrac_i : float
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    relp : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    factor : float
    ipvt : int
    ludecomp : int
    fmat : float
    dgm_dgflux : float
    
    """
    _min3p.f90wrap_dgm_dfluxdg(c_i=c_i, c_j=c_j, dc_i=dc_i, dmolfrac_i=dmolfrac_i, \
        zgi=zgi, zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, relp=relp, \
        tauijx=tauijx, gporx=gporx, delta_ijx=delta_ijx, small=small, factor=factor, \
        ipvt=ipvt, ludecomp=ludecomp, fmat=fmat, dgm_dgflux=dgm_dgflux)

def dgm_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, permijy, \
    relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, dgm_gflux, \
    dgm_neflux):
    """
    dgm_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, permijy, \
        relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, dgm_gflux, \
        dgm_neflux)
    
    
    Defined at ../src/dgm_fluxdg.f lines 144-378
    
    Parameters
    ----------
    c_i : float
    c_j : float
    c_ij : float
    molfrac : int
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    permijy : float
    relp : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    amat : float
    bmat : float
    ipvt : int
    dgm_gflux : float
    dgm_neflux : float
    
    """
    _min3p.f90wrap_dgm_fluxdg(c_i=c_i, c_j=c_j, c_ij=c_ij, molfrac=molfrac, zgi=zgi, \
        zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, permijy=permijy, relp=relp, \
        tauijx=tauijx, gporx=gporx, delta_ijx=delta_ijx, small=small, amat=amat, \
        bmat=bmat, ipvt=ipvt, dgm_gflux=dgm_gflux, dgm_neflux=dgm_neflux)

def dgm_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, \
    permijy, relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, \
    dgm_gflux_s, dgm_neflux_s):
    """
    dgm_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, permijy, \
        relp, tauijx, gporx, delta_ijx, small, amat, bmat, ipvt, dgm_gflux_s, \
        dgm_neflux_s)
    
    
    Defined at ../src/dgm_fluxdg_s.f lines 142-318
    
    Parameters
    ----------
    c_i : float
    c_j : float
    c_ij : float
    molfrac : int
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    permijy : float
    relp : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    amat : float
    bmat : float
    ipvt : int
    dgm_gflux_s : float
    dgm_neflux_s : float
    
    """
    _min3p.f90wrap_dgm_fluxdg_s(c_i=c_i, c_j=c_j, c_ij=c_ij, molfrac=molfrac, \
        zgi=zgi, zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, permijy=permijy, \
        relp=relp, tauijx=tauijx, gporx=gporx, delta_ijx=delta_ijx, small=small, \
        amat=amat, bmat=bmat, ipvt=ipvt, dgm_gflux_s=dgm_gflux_s, \
        dgm_neflux_s=dgm_neflux_s)

def dhconst(dhad, dhbd, tempk, tconv):
    """
    dhconst(dhad, dhbd, tempk, tconv)
    
    
    Defined at ../src/dhconst.f lines 39-69
    
    Parameters
    ----------
    dhad : float
    dhbd : float
    tempk : float
    tconv : float
    
    """
    _min3p.f90wrap_dhconst(dhad=dhad, dhbd=dhbd, tempk=tempk, tconv=tconv)

def diff_grad(c_i, c_j, molfrac, zgi, zgj, dens, tempkel, gporx, delta_ijx, \
    grad_diff):
    """
    diff_grad(c_i, c_j, molfrac, zgi, zgj, dens, tempkel, gporx, delta_ijx, \
        grad_diff)
    
    
    Defined at ../src/diff_grad.f lines 66-118
    
    Parameters
    ----------
    c_i : float
    c_j : float
    molfrac : int
    zgi : float
    zgj : float
    dens : float
    tempkel : float
    gporx : float
    delta_ijx : float
    grad_diff : float
    
    """
    _min3p.f90wrap_diff_grad(c_i=c_i, c_j=c_j, molfrac=molfrac, zgi=zgi, zgj=zgj, \
        dens=dens, tempkel=tempkel, gporx=gporx, delta_ijx=delta_ijx, \
        grad_diff=grad_diff)

def distmp(cmnewm, phim, aream):
    """
    distmp(cmnewm, phim, aream)
    
    
    Defined at ../src/distmp.f lines 55-94
    
    Parameters
    ----------
    cmnewm : float
    phim : float
    aream : float
    
    """
    _min3p.f90wrap_distmp(cmnewm=cmnewm, phim=phim, aream=aream)

def draoult(c, gammac, ratem, phim, phimold, aream, drtinc, im):
    """
    draoult(c, gammac, ratem, phim, phimold, aream, drtinc, im)
    
    
    Defined at ../src/draoult.f lines 106-165
    
    Parameters
    ----------
    c : float
    gammac : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    drtinc : float
    im : int
    
    """
    _min3p.f90wrap_draoult(c=c, gammac=gammac, ratem=ratem, phim=phim, \
        phimold=phimold, aream=aream, drtinc=drtinc, im=im)

def drategas(g, tkel, hhead, zg, drtinc):
    """
    drategas(g, tkel, hhead, zg, drtinc)
    
    
    Defined at ../src/drategas.f lines 68-135
    
    Parameters
    ----------
    g : float
    tkel : float
    hhead : float
    zg : float
    drtinc : float
    
    """
    _min3p.f90wrap_drategas(g=g, tkel=tkel, hhead=hhead, zg=zg, drtinc=drtinc)

def drateint(rate, totc, c, gammac, phim, drtinc, iaq):
    """
    drateint(rate, totc, c, gammac, phim, drtinc, iaq)
    
    
    Defined at ../src/drateint.f lines 131-267
    
    Parameters
    ----------
    rate : float
    totc : float
    c : float
    gammac : float
    phim : float
    drtinc : float
    iaq : int
    
    """
    _min3p.f90wrap_drateint(rate=rate, totc=totc, c=c, gammac=gammac, phim=phim, \
        drtinc=drtinc, iaq=iaq)

def drateint_new(rate, totc, c, cx, gammac, gammax, phim, drtinc, iaq, sw, por, \
    rootdens, wrf):
    """
    drateint_new(rate, totc, c, cx, gammac, gammax, phim, drtinc, iaq, sw, por, \
        rootdens, wrf)
    
    
    Defined at ../src/drateint_new.f lines 236-591
    
    Parameters
    ----------
    rate : float
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    phim : float
    drtinc : float
    iaq : int
    sw : float
    por : float
    rootdens : float
    wrf : float
    
    """
    _min3p.f90wrap_drateint_new(rate=rate, totc=totc, c=c, cx=cx, gammac=gammac, \
        gammax=gammax, phim=phim, drtinc=drtinc, iaq=iaq, sw=sw, por=por, \
        rootdens=rootdens, wrf=wrf)

def dratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, drtinc, \
    im, ivol):
    """
    dratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, drtinc, im, \
        ivol)
    
    
    Defined at ../src/dratemin.f lines 177-505
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    drtinc : float
    im : int
    ivol : int
    
    """
    _min3p.f90wrap_dratemin(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        ratem=ratem, phim=phim, phimold=phimold, aream=aream, drtinc=drtinc, im=im, \
        ivol=ivol)

def dratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, \
    drtinc, im, ivol, sw, por, rootdens):
    """
    dratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, drtinc, \
        im, ivol, sw, por, rootdens)
    
    
    Defined at ../src/dratemin_new.f lines 241-728
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    drtinc : float
    im : int
    ivol : int
    sw : float
    por : float
    rootdens : float
    
    """
    _min3p.f90wrap_dratemin_new(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        ratem=ratem, phim=phim, phimold=phimold, aream=aream, drtinc=drtinc, im=im, \
        ivol=ivol, sw=sw, por=por, rootdens=rootdens)

def draterdx(c, cx, gammac, gammax, drate, totc, drtinc, ir, idbg):
    """
    draterdx(c, cx, gammac, gammax, drate, totc, drtinc, ir, idbg)
    
    
    Defined at ../src/draterdx.f lines 175-401
    
    Parameters
    ----------
    c : float
    cx : float
    gammac : float
    gammax : float
    drate : float
    totc : float
    drtinc : float
    ir : int
    idbg : int
    
    """
    _min3p.f90wrap_draterdx(c=c, cx=cx, gammac=gammac, gammax=gammax, drate=drate, \
        totc=totc, drtinc=drtinc, ir=ir, idbg=idbg)

def dsorbspc(dcsb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, kc):
    """
    dsorbspc(dcsb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, kc)
    
    
    Defined at ../src/dsorbspc.f lines 74-150
    
    Parameters
    ----------
    dcsb : float
    cec : float
    eqsb : float
    gammac : float
    c : float
    xnusb : float
    iasb : int
    jasb : int
    nsb : int
    isb : int
    kc : int
    
    """
    _min3p.f90wrap_dsorbspc(dcsb=dcsb, cec=cec, eqsb=eqsb, gammac=gammac, c=c, \
        xnusb=xnusb, iasb=iasb, jasb=jasb, nsb=nsb, isb=isb, kc=kc)

def dtotconc(c, cx, drtinc, jbl):
    """
    dtotconc(c, cx, drtinc, jbl)
    
    
    Defined at ../src/dtotconc.f lines 75-119
    
    Parameters
    ----------
    c : float
    cx : float
    drtinc : float
    jbl : int
    
    """
    _min3p.f90wrap_dtotconc(c=c, cx=cx, drtinc=drtinc, jbl=jbl)

def dtotcong(g, ginc, dtotg, xnug, drtinc, iaga, jaga, nc, ng, jbl, namec):
    """
    dtotcong(g, ginc, dtotg, xnug, drtinc, iaga, jaga, nc, ng, jbl, namec)
    
    
    Defined at ../src/dtotcong.f lines 65-102
    
    Parameters
    ----------
    g : float
    ginc : float
    dtotg : float
    xnug : float
    drtinc : float
    iaga : int
    jaga : int
    nc : int
    ng : int
    jbl : int
    namec : int
    
    """
    _min3p.f90wrap_dtotcong(g=g, ginc=ginc, dtotg=dtotg, xnug=xnug, drtinc=drtinc, \
        iaga=iaga, jaga=jaga, nc=nc, ng=ng, jbl=jbl, namec=namec)

def findkey(keyword1, keyword2, itmp, found_keyword, searching):
    """
    findkey(keyword1, keyword2, itmp, found_keyword, searching)
    
    
    Defined at ../src/findkey.f lines 40-58
    
    Parameters
    ----------
    keyword1 : int
    keyword2 : int
    itmp : int
    found_keyword : bool
    searching : bool
    
    """
    _min3p.f90wrap_findkey(keyword1=keyword1, keyword2=keyword2, itmp=itmp, \
        found_keyword=found_keyword, searching=searching)

def findname(name, itmp, found_name):
    """
    findname(name, itmp, found_name)
    
    
    Defined at ../src/findname.f lines 37-55
    
    Parameters
    ----------
    name : int
    itmp : int
    found_name : bool
    
    """
    _min3p.f90wrap_findname(name=name, itmp=itmp, found_name=found_name)

def findpath(ipath, im):
    """
    findpath(ipath, im)
    
    
    Defined at ../src/findpath.f lines 54-108
    
    Parameters
    ----------
    ipath : int
    im : int
    
    """
    _min3p.f90wrap_findpath(ipath=ipath, im=im)

def findstrg(subsection, itmp, found_subsection):
    """
    findstrg(subsection, itmp, found_subsection)
    
    
    Defined at ../src/findstrg.f lines 37-55
    
    Parameters
    ----------
    subsection : float
    itmp : int
    found_subsection : bool
    
    """
    _min3p.f90wrap_findstrg(subsection=subsection, itmp=itmp, \
        found_subsection=found_subsection)

def findvol(veln, x, y, z):
    """
    findvol(veln, x, y, z)
    
    
    Defined at ../src/findvol.f lines 55-116
    
    Parameters
    ----------
    veln : int
    x : float
    y : float
    z : float
    
    """
    _min3p.f90wrap_findvol(veln=veln, x=x, y=y, z=z)

def findzone(subsection, itmp, found_subsection, izone, zone_name):
    """
    findzone(subsection, itmp, found_subsection, izone, zone_name)
    
    
    Defined at ../src/findzone.f lines 44-74
    
    Parameters
    ----------
    subsection : float
    itmp : int
    found_subsection : bool
    izone : int
    zone_name : float
    
    """
    _min3p.f90wrap_findzone(subsection=subsection, itmp=itmp, \
        found_subsection=found_subsection, izone=izone, zone_name=zone_name)

def fsflow():
    """
    fsflow()
    
    
    Defined at ../src/fsflow.f lines 93-211
    
    
    """
    _min3p.f90wrap_fsflow()

def gasconc(c, gammac, g, ig, tempkel):
    """
    gasconc(c, gammac, g, ig, tempkel)
    
    
    Defined at ../src/gasconc.f lines 68-89
    
    Parameters
    ----------
    c : float
    gammac : float
    g : float
    ig : int
    tempkel : float
    
    """
    _min3p.f90wrap_gasconc(c=c, gammac=gammac, g=g, ig=ig, tempkel=tempkel)

def gcconst():
    """
    gcconst()
    
    
    Defined at ../src/gcconst.f lines 48-98
    
    
    """
    _min3p.f90wrap_gcconst()

def gcreact(cnew, cold, cx, gammac, gammax, gnew, sw, sa, por, igen, ilog, idbg, \
    tec_header, prefix, l_prfx, zone_name, l_zone_name):
    """
    gcreact(cnew, cold, cx, gammac, gammax, gnew, sw, sa, por, igen, ilog, idbg, \
        tec_header, prefix, l_prfx, zone_name, l_zone_name)
    
    
    Defined at ../src/gcreact.f lines 273-564
    
    Parameters
    ----------
    cnew : float
    cold : float
    cx : float
    gammac : float
    gammax : float
    gnew : float
    sw : float
    sa : float
    por : float
    igen : int
    ilog : int
    idbg : int
    tec_header : bool
    prefix : float
    l_prfx : int
    zone_name : float
    l_zone_name : int
    
    """
    _min3p.f90wrap_gcreact(cnew=cnew, cold=cold, cx=cx, gammac=gammac, \
        gammax=gammax, gnew=gnew, sw=sw, sa=sa, por=por, igen=igen, ilog=ilog, \
        idbg=idbg, tec_header=tec_header, prefix=prefix, l_prfx=l_prfx, \
        zone_name=zone_name, l_zone_name=l_zone_name)

def get_gam(ivol, gam, inc, diag, gamcon):
    """
    get_gam(ivol, gam, inc, diag, gamcon)
    
    
    Defined at ../src/get_gam.f lines 4-128
    
    Parameters
    ----------
    ivol : int
    gam : float
    inc : bool
    diag : bool
    gamcon : float
    
    """
    _min3p.f90wrap_get_gam(ivol=ivol, gam=gam, inc=inc, diag=diag, gamcon=gamcon)

def giups():
    """
    giups()
    
    
    Defined at ../src/giups.f lines 32-90
    
    
    """
    _min3p.f90wrap_giups()

def giups_brt(gpi, gpj, zgi, zgj, dens_i, dens_j, jbrt):
    """
    giups_brt(gpi, gpj, zgi, zgj, dens_i, dens_j, jbrt)
    
    
    Defined at ../src/giups_brt.f lines 35-60
    
    Parameters
    ----------
    gpi : float
    gpj : float
    zgi : float
    zgj : float
    dens_i : float
    dens_j : float
    jbrt : int
    
    """
    _min3p.f90wrap_giups_brt(gpi=gpi, gpj=gpj, zgi=zgi, zgj=zgj, dens_i=dens_i, \
        dens_j=dens_j, jbrt=jbrt)

def guess(cnew, cold, tempkel, ilog):
    """
    guess(cnew, cold, tempkel, ilog)
    
    
    Defined at ../src/guess.f lines 80-190
    
    Parameters
    ----------
    cnew : float
    cold : float
    tempkel : float
    ilog : int
    
    """
    _min3p.f90wrap_guess(cnew=cnew, cold=cold, tempkel=tempkel, ilog=ilog)

def i2upfind():
    """
    i2upfind()
    
    
    Defined at ../src/i2upfind.f lines 63-122
    
    
    """
    _min3p.f90wrap_i2upfind()

def iajabl():
    """
    iajabl()
    
    
    Defined at ../src/iajabl.f lines 120-431
    
    
    """
    _min3p.f90wrap_iajabl()

def iajart():
    """
    iajart()
    
    
    Defined at ../src/iajart.f lines 127-408
    
    
    """
    _min3p.f90wrap_iajart()

def iajavs():
    """
    iajavs()
    
    
    Defined at ../src/iajavs.f lines 104-266
    
    
    """
    _min3p.f90wrap_iajavs()

def iajavs_dp():
    """
    iajavs_dp()
    
    
    Defined at ../src/iajavs_dp.f lines 65-112
    
    
    """
    _min3p.f90wrap_iajavs_dp()

def icbcrt(ivol, imin):
    """
    icbcrt(ivol, imin)
    
    
    Defined at ../src/icbcrt.f lines 187-325
    
    Parameters
    ----------
    ivol : int
    imin : int
    
    """
    _min3p.f90wrap_icbcrt(ivol=ivol, imin=imin)

def icnvrt(way, num, string_bn, length, ierr):
    """
    icnvrt(way, num, string_bn, length, ierr)
    
    
    Defined at ../src/icnvrt.f lines 1-225
    
    Parameters
    ----------
    way : int
    num : int
    string_bn : float
    length : int
    ierr : int
    
    """
    _min3p.f90wrap_icnvrt(way=way, num=num, string_bn=string_bn, length=length, \
        ierr=ierr)

def icrtlczn(izone):
    """
    icrtlczn(izone)
    
    
    Defined at ../src/icrtlczn.f lines 269-1269
    
    Parameters
    ----------
    izone : int
    
    """
    _min3p.f90wrap_icrtlczn(izone=izone)

def indextec():
    """
    indextec()
    
    
    Defined at ../src/indextec.f lines 34-81
    
    
    """
    _min3p.f90wrap_indextec()

def infcrt_a(nvx, nvy, nvz, ia, ja, isymm, cinfvs_a, cinfrt_va, cinfrt_da, d, \
    mprop, nzn, diffu, disx, disy, disz, pornew, sanew, uvsnew, hhead, relperm, \
    idbg, ilog, upstream, fully_saturated, variably_saturated, njamxc, nmax, \
    tortuosity_corr, half_cells, sonew, oil_saturation):
    """
    infcrt_a(nvx, nvy, nvz, ia, ja, isymm, cinfvs_a, cinfrt_va, cinfrt_da, d, mprop, \
        nzn, diffu, disx, disy, disz, pornew, sanew, uvsnew, hhead, relperm, idbg, \
        ilog, upstream, fully_saturated, variably_saturated, njamxc, nmax, \
        tortuosity_corr, half_cells, sonew, oil_saturation)
    
    
    Defined at ../src/infcrt_a.f lines 92-485
    
    Parameters
    ----------
    nvx : int
    nvy : int
    nvz : int
    ia : int array
    ja : int array
    isymm : int array
    cinfvs_a : float
    cinfrt_va : float
    cinfrt_da : float
    d : float
    mprop : int array
    nzn : int
    diffu : float
    disx : float
    disy : float
    disz : float
    pornew : float
    sanew : float
    uvsnew : float
    hhead : float
    relperm : float
    idbg : int
    ilog : int
    upstream : bool
    fully_saturated : bool
    variably_saturated : bool
    njamxc : int
    nmax : int
    tortuosity_corr : float
    half_cells : bool
    sonew : float
    oil_saturation : bool
    
    """
    _min3p.f90wrap_infcrt_a(nvx=nvx, nvy=nvy, nvz=nvz, ia=ia, ja=ja, isymm=isymm, \
        cinfvs_a=cinfvs_a, cinfrt_va=cinfrt_va, cinfrt_da=cinfrt_da, d=d, \
        mprop=mprop, nzn=nzn, diffu=diffu, disx=disx, disy=disy, disz=disz, \
        pornew=pornew, sanew=sanew, uvsnew=uvsnew, hhead=hhead, relperm=relperm, \
        idbg=idbg, ilog=ilog, upstream=upstream, fully_saturated=fully_saturated, \
        variably_saturated=variably_saturated, njamxc=njamxc, nmax=nmax, \
        tortuosity_corr=tortuosity_corr, half_cells=half_cells, sonew=sonew, \
        oil_saturation=oil_saturation)

def infcrt_g(nx, ny, nz, ia, ja, isymm, cinfrt_dg, d, diffu, pornew, sgnew, \
    idbg, ilog, njamxc, nmax, tortuosity_corr, half_cells, deltaij, tauij, \
    gas_tortuosity, gporij, gsatij, tau_man, sonew, oil_saturation):
    """
    infcrt_g(nx, ny, nz, ia, ja, isymm, cinfrt_dg, d, diffu, pornew, sgnew, idbg, \
        ilog, njamxc, nmax, tortuosity_corr, half_cells, deltaij, tauij, \
        gas_tortuosity, gporij, gsatij, tau_man, sonew, oil_saturation)
    
    
    Defined at ../src/infcrt_g.f lines 77-335
    
    Parameters
    ----------
    nx : int
    ny : int
    nz : int
    ia : int array
    ja : int array
    isymm : int array
    cinfrt_dg : float
    d : float
    diffu : float
    pornew : float
    sgnew : float
    idbg : int
    ilog : int
    njamxc : int
    nmax : int
    tortuosity_corr : float
    half_cells : bool
    deltaij : float
    tauij : float
    gas_tortuosity : float
    gporij : float
    gsatij : float
    tau_man : float
    sonew : float
    oil_saturation : bool
    
    """
    _min3p.f90wrap_infcrt_g(nx=nx, ny=ny, nz=nz, ia=ia, ja=ja, isymm=isymm, \
        cinfrt_dg=cinfrt_dg, d=d, diffu=diffu, pornew=pornew, sgnew=sgnew, \
        idbg=idbg, ilog=ilog, njamxc=njamxc, nmax=nmax, \
        tortuosity_corr=tortuosity_corr, half_cells=half_cells, deltaij=deltaij, \
        tauij=tauij, gas_tortuosity=gas_tortuosity, gporij=gporij, gsatij=gsatij, \
        tau_man=tau_man, sonew=sonew, oil_saturation=oil_saturation)

def infcvs():
    """
    infcvs()
    
    
    Defined at ../src/infcvs.f lines 149-477
    
    
    """
    _min3p.f90wrap_infcvs()

def infcvs_cp():
    """
    infcvs_cp()
    
    
    Defined at ../src/infcvs_cp.f lines 46-66
    
    
    """
    _min3p.f90wrap_infcvs_cp()

def initbcrt():
    """
    initbcrt()
    
    
    Defined at ../src/initbcrt.f lines 289-1263
    
    
    """
    _min3p.f90wrap_initbcrt()

def initbcvs():
    """
    initbcvs()
    
    
    Defined at ../src/initbcvs.f lines 159-664
    
    
    """
    _min3p.f90wrap_initbcvs()

def initcpgs():
    """
    initcpgs()
    
    
    Defined at ../src/initcpgs.f lines 96-332
    
    
    """
    _min3p.f90wrap_initcpgs()

def initcplc():
    """
    initcplc()
    
    
    Defined at ../src/initcplc.f lines 98-283
    
    
    """
    _min3p.f90wrap_initcplc()

def initcprt():
    """
    initcprt()
    
    
    Defined at ../src/initcprt.f lines 162-669
    
    
    -----added by FG, 12 nov 08 to write info in gen file
    """
    _min3p.f90wrap_initcprt()

def initcpvs():
    """
    initcpvs()
    
    
    Defined at ../src/initcpvs.f lines 93-383
    
    
    """
    _min3p.f90wrap_initcpvs()

def initcsys():
    """
    initcsys()
    
    
    Defined at ../src/initcsys.f lines 255-1532
    
    
    """
    _min3p.f90wrap_initcsys()

def initgeom(im, idbg):
    """
    initgeom(im, idbg)
    
    
    Defined at ../src/initgeom.f lines 69-240
    
    Parameters
    ----------
    im : int
    idbg : int
    
    """
    _min3p.f90wrap_initgeom(im=im, idbg=idbg)

def initicrt():
    """
    initicrt()
    
    
    Defined at ../src/initicrt.f lines 158-768
    
    
    """
    _min3p.f90wrap_initicrt()

def initicvs():
    """
    initicvs()
    
    
    Defined at ../src/initicvs.f lines 107-376
    
    
    """
    _min3p.f90wrap_initicvs()

def initopgs():
    """
    initopgs()
    
    
    Defined at ../src/initopgs.f lines 153-579
    
    
    -----added by FG, 12 nov 08 to write info in gen file
    """
    _min3p.f90wrap_initopgs()

def initplant():
    """
    initplant()
    
    
    Defined at ../src/initplant.f lines 168-658
    
    
    """
    _min3p.f90wrap_initplant()

def initpppm():
    """
    initpppm()
    
    
    Defined at ../src/initpppm.f lines 107-403
    
    
    """
    _min3p.f90wrap_initpppm()

def initpprt():
    """
    initpprt()
    
    
    Defined at ../src/initpprt.f lines 125-753
    
    
    """
    _min3p.f90wrap_initpprt()

def initppvs():
    """
    initppvs()
    
    
    Defined at ../src/initppvs.f lines 190-771
    
    
    """
    _min3p.f90wrap_initppvs()

def initprob():
    """
    initprob()
    
    
    Defined at ../src/initprob.f lines 71-270
    
    
    """
    _min3p.f90wrap_initprob()

def initsatw():
    """
    initsatw()
    
    
    Defined at ../src/initsatw.f lines 64-104
    
    
    """
    _min3p.f90wrap_initsatw()

def inittemp():
    """
    inittemp()
    
    
    Defined at ../src/inittemp.f lines 126-289
    
    
    """
    _min3p.f90wrap_inittemp()

def inittsgs():
    """
    inittsgs()
    
    
    Defined at ../src/inittsgs.f lines 73-189
    
    
    """
    _min3p.f90wrap_inittsgs()

def initweed():
    """
    initweed()
    
    
    Defined at ../src/initweed.f lines 51-70
    
    
    """
    _min3p.f90wrap_initweed()

def intpolt():
    """
    intpolt()
    
    
    Defined at ../src/intpolt.f lines 69-133
    
    
    """
    _min3p.f90wrap_intpolt()

def ionstr(c, cx, strion, chargec, chargex, nc, nx, namec, component_type):
    """
    ionstr(c, cx, strion, chargec, chargex, nc, nx, namec, component_type)
    
    
    Defined at ../src/ionstr.f lines 47-79
    
    Parameters
    ----------
    c : float
    cx : float
    strion : float
    chargec : float
    chargex : float
    nc : int
    nx : int
    namec : int
    component_type : float
    
    """
    _min3p.f90wrap_ionstr(c=c, cx=cx, strion=strion, chargec=chargec, \
        chargex=chargex, nc=nc, nx=nx, namec=namec, component_type=component_type)

def jacbrt():
    """
    jacbrt()
    
    
    Defined at ../src/jacbrt.f lines 326-1417
    
    
    """
    _min3p.f90wrap_jacbrt()

def jacbvs():
    """
    jacbvs()
    
    
    Defined at ../src/jacbvs.f lines 66-120
    
    
    """
    _min3p.f90wrap_jacbvs()

def jacfs():
    """
    jacfs()
    
    
    Defined at ../src/jacfs.f lines 82-205
    
    
    """
    _min3p.f90wrap_jacfs()

def jaclc(cnew, cx, gammac, gammax, sw, sa, por):
    """
    jaclc(cnew, cx, gammac, gammax, sw, sa, por)
    
    
    Defined at ../src/jaclc.f lines 275-852
    
    Parameters
    ----------
    cnew : float
    cx : float
    gammac : float
    gammax : float
    sw : float
    sa : float
    por : float
    
    """
    _min3p.f90wrap_jaclc(cnew=cnew, cx=cx, gammac=gammac, gammax=gammax, sw=sw, \
        sa=sa, por=por)

def compte():
    """
    compte()
    
    
    Defined at ../src/jaclc.f lines 856-860
    
    
    """
    _min3p.f90wrap_compte()

def compte4():
    """
    compte4()
    
    
    Defined at ../src/jaclc.f lines 862-866
    
    
    """
    _min3p.f90wrap_compte4()

def compte5():
    """
    compte5()
    
    
    Defined at ../src/jaclc.f lines 868-872
    
    
    """
    _min3p.f90wrap_compte5()

def compte6():
    """
    compte6()
    
    
    Defined at ../src/jaclc.f lines 874-876
    
    
    """
    _min3p.f90wrap_compte6()

def jacrt():
    """
    jacrt()
    
    
    Defined at ../src/jacrt.f lines 557-2105
    
    
    """
    _min3p.f90wrap_jacrt()

def jacsurf(cnew, gammac, sw, por):
    """
    jacsurf(cnew, gammac, sw, por)
    
    
    Defined at ../src/jacsurf.f lines 115-285
    
    Parameters
    ----------
    cnew : float
    gammac : float
    sw : float
    por : float
    
    """
    _min3p.f90wrap_jacsurf(cnew=cnew, gammac=gammac, sw=sw, por=por)

def jacvs():
    """
    jacvs()
    
    
    Defined at ../src/jacvs.f lines 140-388
    
    
    """
    _min3p.f90wrap_jacvs()

def lennard_jones(sigma, epsil, visc_comp_g, diff_bin_g):
    """
    lennard_jones(sigma, epsil, visc_comp_g, diff_bin_g)
    
    
    Defined at ../src/lennard_jones.f lines 41-113
    
    Parameters
    ----------
    sigma : float
    epsil : float
    visc_comp_g : float
    diff_bin_g : float
    
    """
    _min3p.f90wrap_lennard_jones(sigma=sigma, epsil=epsil, visc_comp_g=visc_comp_g, \
        diff_bin_g=diff_bin_g)

def madd(na, nb, nc, m, n, a, b, c):
    """
    madd(na, nb, nc, m, n, a, b, c)
    
    
    Defined at ../src/madd.f lines 1-53
    
    Parameters
    ----------
    na : int
    nb : int
    nc : int
    m : int
    n : int
    a : unknown array
    b : unknown array
    c : unknown array
    
    """
    _min3p.f90wrap_madd(na=na, nb=nb, nc=nc, m=m, n=n, a=a, b=b, c=c)

def mbalrt():
    """
    mbalrt()
    
    
    Defined at ../src/mbalrt.f lines 499-1924
    
    
    """
    _min3p.f90wrap_mbalrt()

def mbalvs():
    """
    mbalvs()
    
    
    Defined at ../src/mbalvs.f lines 121-324
    
    
    """
    _min3p.f90wrap_mbalvs()

def mem_etr():
    """
    mem_etr()
    
    
    Defined at ../src/mem_etr.f lines 46-144
    
    
    """
    _min3p.f90wrap_mem_etr()

def mem_mat():
    """
    mem_mat()
    
    
    Defined at ../src/mem_mat.f lines 75-220
    
    
    """
    _min3p.f90wrap_mem_mat()

def mem_naq():
    """
    mem_naq()
    
    
    Defined at ../src/mem_naq.f lines 198-449
    
    
    """
    _min3p.f90wrap_mem_naq()

def mem_nc():
    """
    mem_nc()
    
    
    Defined at ../src/mem_nc.f lines 193-381
    
    
    """
    _min3p.f90wrap_mem_nc()

def mem_ncsb():
    """
    mem_ncsb()
    
    
    Defined at ../src/mem_ncsb.f lines 94-169
    
    
    """
    _min3p.f90wrap_mem_ncsb()

def mem_ng():
    """
    mem_ng()
    
    
    Defined at ../src/mem_ng.f lines 71-140
    
    
    """
    _min3p.f90wrap_mem_ng()

def mem_njart():
    """
    mem_njart()
    
    
    Defined at ../src/mem_njart.f lines 38-92
    
    
    """
    _min3p.f90wrap_mem_njart()

def mem_njavs():
    """
    mem_njavs()
    
    
    Defined at ../src/mem_njavs.f lines 67-178
    
    
    """
    _min3p.f90wrap_mem_njavs()

def mem_nm():
    """
    mem_nm()
    
    
    Defined at ../src/mem_nm.f lines 255-605
    
    
    """
    _min3p.f90wrap_mem_nm()

def mem_nmx():
    """
    mem_nmx()
    
    
    Defined at ../src/mem_nmx.f lines 65-109
    
    
    """
    _min3p.f90wrap_mem_nmx()

def mem_nr():
    """
    mem_nr()
    
    
    Defined at ../src/mem_nr.f lines 127-252
    
    
    """
    _min3p.f90wrap_mem_nr()

def mem_nsb():
    """
    mem_nsb()
    
    
    Defined at ../src/mem_nsb.f lines 100-219
    
    
    """
    _min3p.f90wrap_mem_nsb()

def mem_ntmp():
    """
    mem_ntmp()
    
    
    Defined at ../src/mem_ntmp.f lines 42-57
    
    
    """
    _min3p.f90wrap_mem_ntmp()

def mem_nx():
    """
    mem_nx()
    
    
    Defined at ../src/mem_nx.f lines 86-170
    
    
    """
    _min3p.f90wrap_mem_nx()

def mem_rt():
    """
    mem_rt()
    
    
    Defined at ../src/mem_rt.f lines 260-711
    
    
    """
    _min3p.f90wrap_mem_rt()

def mem_vs():
    """
    mem_vs()
    
    
    Defined at ../src/mem_vs.f lines 74-203
    
    
    """
    _min3p.f90wrap_mem_vs()

def minmaxwd(cx, totc):
    """
    minmaxwd(cx, totc)
    
    
    Defined at ../src/minmaxwd.f lines 49-72
    
    Parameters
    ----------
    cx : float
    totc : float
    
    """
    _min3p.f90wrap_minmaxwd(cx=cx, totc=totc)

def mmul(na, nb, nc, l, m, n, a, b, c):
    """
    mmul(na, nb, nc, l, m, n, a, b, c)
    
    
    Defined at ../src/mmul.f lines 1-65
    
    Parameters
    ----------
    na : int
    nb : int
    nc : int
    l : int
    m : int
    n : int
    a : unknown array
    b : unknown array
    c : unknown array
    
    """
    _min3p.f90wrap_mmul(na=na, nb=nb, nc=nc, l=l, m=m, n=n, a=a, b=b, c=c)

def modrate(ratem, cmnewm, delt, im):
    """
    modrate(ratem, cmnewm, delt, im)
    
    
    Defined at ../src/modrate.f lines 80-145
    
    Parameters
    ----------
    ratem : float
    cmnewm : float
    delt : float
    im : int
    
    """
    _min3p.f90wrap_modrate(ratem=ratem, cmnewm=cmnewm, delt=delt, im=im)

def molconc(phim):
    """
    molconc(phim)
    
    
    Defined at ../src/molconc.f lines 56-84
    
    Parameters
    ----------
    phim : float
    
    """
    _min3p.f90wrap_molconc(phim=phim)

def ms_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, \
    tauijx, gporx, delta_ijx, small, factor, ipvt, equimolar, ludecomp, fmatx, \
    ms_gflux, ms_dgflux):
    """
    ms_dfluxdg(c_i, c_j, dc_i, dmolfrac_i, zgi, zgj, dens, gpij, tempkel, tauijx, \
        gporx, delta_ijx, small, factor, ipvt, equimolar, ludecomp, fmatx, ms_gflux, \
        ms_dgflux)
    
    
    Defined at ../src/ms_dfluxdg.f lines 147-379
    
    Parameters
    ----------
    c_i : float
    c_j : float
    dc_i : float
    dmolfrac_i : float
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    factor : float
    ipvt : int
    equimolar : bool
    ludecomp : int
    fmatx : float
    ms_gflux : int
    ms_dgflux : int
    
    """
    _min3p.f90wrap_ms_dfluxdg(c_i=c_i, c_j=c_j, dc_i=dc_i, dmolfrac_i=dmolfrac_i, \
        zgi=zgi, zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, tauijx=tauijx, \
        gporx=gporx, delta_ijx=delta_ijx, small=small, factor=factor, ipvt=ipvt, \
        equimolar=equimolar, ludecomp=ludecomp, fmatx=fmatx, ms_gflux=ms_gflux, \
        ms_dgflux=ms_dgflux)

def ms_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, \
    gporx, delta_ijx, small, ludecomp, fmat, ipvt, equimolar, ms_gflux, \
    ms_neflux):
    """
    ms_fluxdg(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, gporx, \
        delta_ijx, small, ludecomp, fmat, ipvt, equimolar, ms_gflux, ms_neflux)
    
    
    Defined at ../src/ms_fluxdg.f lines 139-342
    
    Parameters
    ----------
    c_i : float
    c_j : float
    c_ij : float
    molfrac : int
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    ludecomp : int
    fmat : float
    ipvt : int
    equimolar : bool
    ms_gflux : int
    ms_neflux : int
    
    """
    _min3p.f90wrap_ms_fluxdg(c_i=c_i, c_j=c_j, c_ij=c_ij, molfrac=molfrac, zgi=zgi, \
        zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, tauijx=tauijx, gporx=gporx, \
        delta_ijx=delta_ijx, small=small, ludecomp=ludecomp, fmat=fmat, ipvt=ipvt, \
        equimolar=equimolar, ms_gflux=ms_gflux, ms_neflux=ms_neflux)

def ms_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, \
    gporx, delta_ijx, small, ludecomp, ipvt, equimolar, fmat, ms_neflux_s):
    """
    ms_fluxdg_s(c_i, c_j, c_ij, molfrac, zgi, zgj, dens, gpij, tempkel, tauijx, \
        gporx, delta_ijx, small, ludecomp, ipvt, equimolar, fmat, ms_neflux_s)
    
    
    Defined at ../src/ms_fluxdg_s.f lines 137-314
    
    Parameters
    ----------
    c_i : float
    c_j : float
    c_ij : float
    molfrac : int
    zgi : float
    zgj : float
    dens : float
    gpij : float
    tempkel : float
    tauijx : float
    gporx : float
    delta_ijx : float
    small : float
    ludecomp : int
    ipvt : int
    equimolar : bool
    fmat : float
    ms_neflux_s : int
    
    """
    _min3p.f90wrap_ms_fluxdg_s(c_i=c_i, c_j=c_j, c_ij=c_ij, molfrac=molfrac, \
        zgi=zgi, zgj=zgj, dens=dens, gpij=gpij, tempkel=tempkel, tauijx=tauijx, \
        gporx=gporx, delta_ijx=delta_ijx, small=small, ludecomp=ludecomp, ipvt=ipvt, \
        equimolar=equimolar, fmat=fmat, ms_neflux_s=ms_neflux_s)

def msub(na, nb, nc, m, n, a, b, c):
    """
    msub(na, nb, nc, m, n, a, b, c)
    
    
    Defined at ../src/msub.f lines 1-53
    
    Parameters
    ----------
    na : int
    nb : int
    nc : int
    m : int
    n : int
    a : unknown array
    b : unknown array
    c : unknown array
    
    """
    _min3p.f90wrap_msub(na=na, nb=nb, nc=nc, m=m, n=n, a=a, b=b, c=c)

def msysrt():
    """
    msysrt()
    
    
    Defined at ../src/msysrt.f lines 205-599
    
    
    """
    _min3p.f90wrap_msysrt()

def msysvs():
    """
    msysvs()
    
    
    Defined at ../src/msysvs.f lines 74-137
    
    
    """
    _min3p.f90wrap_msysvs()

def nexttime():
    """
    nexttime()
    
    
    Defined at ../src/nexttime.f lines 208-479
    
    
    """
    _min3p.f90wrap_nexttime()

def opndbfls(redox_master, search_database):
    """
    opndbfls(redox_master, search_database)
    
    
    Defined at ../src/opndbfls_pc.f lines 63-178
    
    Parameters
    ----------
    redox_master : float
    search_database : bool
    
    """
    _min3p.f90wrap_opndbfls(redox_master=redox_master, \
        search_database=search_database)

def opngfls():
    """
    opngfls()
    
    
    Defined at ../src/opngfls.f lines 54-172
    
    
    """
    _min3p.f90wrap_opngfls()

def opnmbfls():
    """
    opnmbfls()
    
    
    Defined at ../src/opnmbfls.f lines 114-939
    
    
    """
    _min3p.f90wrap_opnmbfls()

def opnpgfls():
    """
    opnpgfls()
    
    
    Defined at ../src/opnpgfls.f lines 262-1045
    
    
    """
    _min3p.f90wrap_opnpgfls()

def opnplfls(ilb):
    """
    opnplfls(ilb)
    
    
    Defined at ../src/opnplfls.f lines 156-748
    
    Parameters
    ----------
    ilb : int
    
    """
    _min3p.f90wrap_opnplfls(ilb=ilb)

def opntemp():
    """
    opntemp()
    
    
    Defined at ../src/opntemp.f lines 50-87
    
    
    """
    _min3p.f90wrap_opntemp()

def outputlc(c, cx, gammac, gammax, g, igen, ilog, section_header):
    """
    outputlc(c, cx, gammac, gammax, g, igen, ilog, section_header)
    
    
    Defined at ../src/outputlc.f lines 183-531
    
    Parameters
    ----------
    c : float
    cx : float
    gammac : float
    gammax : float
    g : float
    igen : int
    ilog : int
    section_header : float
    
    """
    _min3p.f90wrap_outputlc(c=c, cx=cx, gammac=gammac, gammax=gammax, g=g, \
        igen=igen, ilog=ilog, section_header=section_header)

def outputrt():
    """
    outputrt()
    
    
    Defined at ../src/outputrt.f lines 425-2598
    
    
    """
    _min3p.f90wrap_outputrt()

def outputvs():
    """
    outputvs()
    
    
    Defined at ../src/outputvs.f lines 140-566
    
    
    """
    _min3p.f90wrap_outputvs()

def phcorr(cnew, cold, tempkel, ilog):
    """
    phcorr(cnew, cold, tempkel, ilog)
    
    
    Defined at ../src/phcorr.f lines 77-131
    
    Parameters
    ----------
    cnew : float
    cold : float
    tempkel : float
    ilog : int
    
    """
    _min3p.f90wrap_phcorr(cnew=cnew, cold=cold, tempkel=tempkel, ilog=ilog)

def phpe(c, gammac, ph, pe, eh, tempkel):
    """
    phpe(c, gammac, ph, pe, eh, tempkel)
    
    
    Defined at ../src/phpe.f lines 54-102
    
    Parameters
    ----------
    c : float
    gammac : float
    ph : float
    pe : float
    eh : float
    tempkel : float
    
    """
    _min3p.f90wrap_phpe(c=c, gammac=gammac, ph=ph, pe=pe, eh=eh, tempkel=tempkel)

def raoult(c, gammac, ratem, phim, phimold, aream, im):
    """
    raoult(c, gammac, ratem, phim, phimold, aream, im)
    
    
    Defined at ../src/raoult.f lines 99-155
    
    Parameters
    ----------
    c : float
    gammac : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    im : int
    
    """
    _min3p.f90wrap_raoult(c=c, gammac=gammac, ratem=ratem, phim=phim, \
        phimold=phimold, aream=aream, im=im)

def rategas(g, tkel, hhead, zg):
    """
    rategas(g, tkel, hhead, zg)
    
    
    Defined at ../src/rategas.f lines 57-121
    
    Parameters
    ----------
    g : float
    tkel : float
    hhead : float
    zg : float
    
    """
    _min3p.f90wrap_rategas(g=g, tkel=tkel, hhead=hhead, zg=zg)

def rateh2o():
    """
    rateh2o()
    
    
    Defined at ../src/rateh2o.f lines 100-229
    
    
    """
    _min3p.f90wrap_rateh2o()

def rateint(rate, totc, c, gammac, phim, iaq):
    """
    rateint(rate, totc, c, gammac, phim, iaq)
    
    
    Defined at ../src/rateint.f lines 92-212
    
    Parameters
    ----------
    rate : float
    totc : float
    c : float
    gammac : float
    phim : float
    iaq : int
    
    """
    _min3p.f90wrap_rateint(rate=rate, totc=totc, c=c, gammac=gammac, phim=phim, \
        iaq=iaq)

def rateint_new(rate, totc, c, cx, gammac, gammax, phim, iaq, sw, por, rootdens, \
    wrf):
    """
    rateint_new(rate, totc, c, cx, gammac, gammax, phim, iaq, sw, por, rootdens, \
        wrf)
    
    
    Defined at ../src/rateint_new.f lines 223-532
    
    Parameters
    ----------
    rate : float
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    phim : float
    iaq : int
    sw : float
    por : float
    rootdens : float
    wrf : float
    
    """
    _min3p.f90wrap_rateint_new(rate=rate, totc=totc, c=c, cx=cx, gammac=gammac, \
        gammax=gammax, phim=phim, iaq=iaq, sw=sw, por=por, rootdens=rootdens, \
        wrf=wrf)

def ratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im):
    """
    ratemin(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im)
    
    
    Defined at ../src/ratemin.f lines 161-492
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    im : int
    
    """
    _min3p.f90wrap_ratemin(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        ratem=ratem, phim=phim, phimold=phimold, aream=aream, im=im)

def ratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, \
    sw, por, rootdens):
    """
    ratemin_new(totc, c, cx, gammac, gammax, ratem, phim, phimold, aream, im, sw, \
        por, rootdens)
    
    
    Defined at ../src/ratemin_new.f lines 220-677
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    ratem : float
    phim : float
    phimold : float
    aream : float
    im : int
    sw : float
    por : float
    rootdens : float
    
    """
    _min3p.f90wrap_ratemin_new(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        ratem=ratem, phim=phim, phimold=phimold, aream=aream, im=im, sw=sw, por=por, \
        rootdens=rootdens)

def rateredx(c, cx, gammac, gammax, rate, totc, ir):
    """
    rateredx(c, cx, gammac, gammax, rate, totc, ir)
    
    
    Defined at ../src/rateredx.f lines 144-322
    
    Parameters
    ----------
    c : float
    cx : float
    gammac : float
    gammax : float
    rate : float
    totc : float
    ir : int
    
    """
    _min3p.f90wrap_rateredx(c=c, cx=cx, gammac=gammac, gammax=gammax, rate=rate, \
        totc=totc, ir=ir)

def reactran():
    """
    reactran()
    
    
    Defined at ../src/reactran.f lines 273-608
    
    
    """
    _min3p.f90wrap_reactran()

def read_tau():
    """
    read_tau()
    
    
    Defined at ../src/read_tau.f lines 1-44
    
    
    """
    _min3p.f90wrap_read_tau()

def readbcvs():
    """
    readbcvs()
    
    
    Defined at ../src/readbcvs.f lines 61-89
    
    
    """
    _min3p.f90wrap_readbcvs()

def readbloc(nin, nout, section_header, found):
    """
    readbloc(nin, nout, section_header, found)
    
    
    Defined at ../src/readbloc.f lines 44-81
    
    Parameters
    ----------
    nin : int
    nout : int
    section_header : float
    found : bool
    
    """
    _min3p.f90wrap_readbloc(nin=nin, nout=nout, section_header=section_header, \
        found=found)

def readcomp(icdbs, ilog, idbg):
    """
    readcomp(icdbs, ilog, idbg)
    
    
    Defined at ../src/readcomp.f lines 69-161
    
    Parameters
    ----------
    icdbs : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readcomp(icdbs=icdbs, ilog=ilog, idbg=idbg)

def readgses(igdbs, ipsp, ilog, idbg):
    """
    readgses(igdbs, ipsp, ilog, idbg)
    
    
    Defined at ../src/readgses.f lines 101-304
    
    Parameters
    ----------
    igdbs : int
    ipsp : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readgses(igdbs=igdbs, ipsp=ipsp, ilog=ilog, idbg=idbg)

def readint(irdbs, ilog, idbg):
    """
    readint(irdbs, ilog, idbg)
    
    
    Defined at ../src/readint.f lines 150-617
    
    Parameters
    ----------
    irdbs : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readint(irdbs=irdbs, ilog=ilog, idbg=idbg)

def readint_new(irdbs, ilog, idbg):
    """
    readint_new(irdbs, ilog, idbg)
    
    
    Defined at ../src/readint_new.f lines 245-1648
    
    Parameters
    ----------
    irdbs : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readint_new(irdbs=irdbs, ilog=ilog, idbg=idbg)

def readmin(imdbs, ilog, idbg, icnv):
    """
    readmin(imdbs, ilog, idbg, icnv)
    
    
    Defined at ../src/readmin.f lines 214-834
    
    Parameters
    ----------
    imdbs : int
    ilog : int
    idbg : int
    icnv : int
    
    """
    _min3p.f90wrap_readmin(imdbs=imdbs, ilog=ilog, idbg=idbg, icnv=icnv)

def readmin_new(imdbs, ilog, idbg, icnv):
    """
    readmin_new(imdbs, ilog, idbg, icnv)
    
    
    Defined at ../src/readmin_new.f lines 298-2048
    
    Parameters
    ----------
    imdbs : int
    ilog : int
    idbg : int
    icnv : int
    
    -------------------------------------------------
    """
    _min3p.f90wrap_readmin_new(imdbs=imdbs, ilog=ilog, idbg=idbg, icnv=icnv)

def readminx(imdbs, ipsp, ilog, idbg):
    """
    readminx(imdbs, ipsp, ilog, idbg)
    
    
    Defined at ../src/readminx.f lines 107-423
    
    Parameters
    ----------
    imdbs : int
    ipsp : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readminx(imdbs=imdbs, ipsp=ipsp, ilog=ilog, idbg=idbg)

def readminx_new(imdbs, ipsp, ilog, idbg):
    """
    readminx_new(imdbs, ipsp, ilog, idbg)
    
    
    Defined at ../src/readminx_new.f lines 107-418
    
    Parameters
    ----------
    imdbs : int
    ipsp : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readminx_new(imdbs=imdbs, ipsp=ipsp, ilog=ilog, idbg=idbg)

def readredx(irdbs, ilog, idbg):
    """
    readredx(irdbs, ilog, idbg)
    
    
    Defined at ../src/readredx.f lines 183-619
    
    Parameters
    ----------
    irdbs : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readredx(irdbs=irdbs, ilog=ilog, idbg=idbg)

def readredx_new(irdbs, ilog, idbg):
    """
    readredx_new(irdbs, ilog, idbg)
    
    
    Defined at ../src/readredx_new.f lines 99-327
    
    Parameters
    ----------
    irdbs : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readredx_new(irdbs=irdbs, ilog=ilog, idbg=idbg)

def readsorb(isdbs, ipsp, ilog, idbg):
    """
    readsorb(isdbs, ipsp, ilog, idbg)
    
    
    Defined at ../src/readsorb.f lines 111-311
    
    Parameters
    ----------
    isdbs : int
    ipsp : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readsorb(isdbs=isdbs, ipsp=ipsp, ilog=ilog, idbg=idbg)

def readsspc(ixdbs, ipsp, ilog, idbg):
    """
    readsspc(ixdbs, ipsp, ilog, idbg)
    
    
    Defined at ../src/readsspc.f lines 127-351
    
    Parameters
    ----------
    ixdbs : int
    ipsp : int
    ilog : int
    idbg : int
    
    """
    _min3p.f90wrap_readsspc(ixdbs=ixdbs, ipsp=ipsp, ilog=ilog, idbg=idbg)

def readtemp():
    """
    readtemp()
    
    
    Defined at ../src/readtemp.f lines 57-95
    
    
    """
    _min3p.f90wrap_readtemp()

def readtime(nin, nout, ilog, itsrc, found):
    """
    readtime(nin, nout, ilog, itsrc, found)
    
    
    Defined at ../src/readtime.f lines 50-98
    
    Parameters
    ----------
    nin : int
    nout : int
    ilog : int
    itsrc : int
    found : bool
    
    """
    _min3p.f90wrap_readtime(nin=nin, nout=nout, ilog=ilog, itsrc=itsrc, found=found)

def readzone(nin, nout, ilog, zone_name, found):
    """
    readzone(nin, nout, ilog, zone_name, found)
    
    
    Defined at ../src/readzone.f lines 49-97
    
    Parameters
    ----------
    nin : int
    nout : int
    ilog : int
    zone_name : float
    found : bool
    
    """
    _min3p.f90wrap_readzone(nin=nin, nout=nout, ilog=ilog, zone_name=zone_name, \
        found=found)

def restart_r():
    """
    restart_r()
    
    
    Defined at ../src/restart_r.f lines 207-510
    
    
    """
    _min3p.f90wrap_restart_r()

def restart_w():
    """
    restart_w()
    
    
    Defined at ../src/restart_w.f lines 204-329
    
    
    """
    _min3p.f90wrap_restart_w()

def rhsrt(naq, ng, nm, nr, nsb, astor, cstor, gstor, totaq, totsb, totor, totdp, \
    totcflux, totgflux, totrateg, redox_equil, noncompetitive_sorption, \
    component_type, b):
    """
    rhsrt(naq, ng, nm, nr, nsb, astor, cstor, gstor, totaq, totsb, totor, totdp, \
        totcflux, totgflux, totrateg, redox_equil, noncompetitive_sorption, \
        component_type, b)
    
    
    Defined at ../src/rhsrt.f lines 78-135
    
    Parameters
    ----------
    naq : int
    ng : int
    nm : int
    nr : int
    nsb : int
    astor : float
    cstor : float
    gstor : float
    totaq : float
    totsb : float
    totor : float
    totdp : float
    totcflux : float
    totgflux : float
    totrateg : float
    redox_equil : bool
    noncompetitive_sorption : bool
    component_type : float
    b : float
    
    """
    _min3p.f90wrap_rhsrt(naq=naq, ng=ng, nm=nm, nr=nr, nsb=nsb, astor=astor, \
        cstor=cstor, gstor=gstor, totaq=totaq, totsb=totsb, totor=totor, \
        totdp=totdp, totcflux=totcflux, totgflux=totgflux, totrateg=totrateg, \
        redox_equil=redox_equil, noncompetitive_sorption=noncompetitive_sorption, \
        component_type=component_type, b=b)

def rhsvs(vsstor, totvsflux, b):
    """
    rhsvs(vsstor, totvsflux, b)
    
    
    Defined at ../src/rhsvs.f lines 28-33
    
    Parameters
    ----------
    vsstor : float
    totvsflux : float
    b : float
    
    """
    _min3p.f90wrap_rhsvs(vsstor=vsstor, totvsflux=totvsflux, b=b)

def rsort(rlist, n):
    """
    rsort(rlist, n)
    
    
    Defined at ../src/rsort.f lines 36-61
    
    Parameters
    ----------
    rlist : float
    n : int
    
    """
    _min3p.f90wrap_rsort(rlist=rlist, n=n)

def rstatgs(idev):
    """
    rstatgs(idev)
    
    
    Defined at ../src/rstatgs.f lines 66-149
    
    Parameters
    ----------
    idev : int
    
    """
    _min3p.f90wrap_rstatgs(idev=idev)

def rstatlc(idev):
    """
    rstatlc(idev)
    
    
    Defined at ../src/rstatlc.f lines 32-49
    
    Parameters
    ----------
    idev : int
    
    """
    _min3p.f90wrap_rstatlc(idev=idev)

def rtrvpprm(swc, sac, porc, section_header):
    """
    rtrvpprm(swc, sac, porc, section_header)
    
    
    Defined at ../src/rtrvpprm.f lines 44-86
    
    Parameters
    ----------
    swc : float
    sac : float
    porc : float
    section_header : float
    
    """
    _min3p.f90wrap_rtrvpprm(swc=swc, sac=sac, porc=porc, \
        section_header=section_header)

def secspec(c, c2, eqc2, gammac1, gammac2, xnuc2, ia, ja, n, i2):
    """
    secspec(c, c2, eqc2, gammac1, gammac2, xnuc2, ia, ja, n, i2)
    
    
    Defined at ../src/secspec.f lines 58-75
    
    Parameters
    ----------
    c : float
    c2 : float
    eqc2 : float
    gammac1 : float
    gammac2 : float
    xnuc2 : float
    ia : int
    ja : int
    n : int
    i2 : int
    
    """
    _min3p.f90wrap_secspec(c=c, c2=c2, eqc2=eqc2, gammac1=gammac1, gammac2=gammac2, \
        xnuc2=xnuc2, ia=ia, ja=ja, n=n, i2=i2)

def seepface():
    """
    seepface()
    
    
    Defined at ../src/seepface.f lines 80-172
    
    
    """
    _min3p.f90wrap_seepface()

def setsize(redox_equil_s):
    """
    setsize(redox_equil_s)
    
    
    Defined at ../src/setsize.f lines 37-58
    
    Parameters
    ----------
    redox_equil_s : bool
    
    """
    _min3p.f90wrap_setsize(redox_equil_s=redox_equil_s)

def simq(z, y, n, nxdim):
    """
    simq(z, y, n, nxdim)
    
    
    Defined at ../src/simq.f lines 1-73
    
    Parameters
    ----------
    z : float
    y : float
    n : int
    nxdim : int
    
    """
    _min3p.f90wrap_simq(z=z, y=y, n=n, nxdim=nxdim)

def soilparm(uvsnew, sanew, relperm, relpermg, sonew, mpropvs, nn):
    """
    soilparm(uvsnew, sanew, relperm, relpermg, sonew, mpropvs, nn)
    
    
    Defined at ../src/soilparm.f lines 66-117
    
    Parameters
    ----------
    uvsnew : float
    sanew : float
    relperm : float
    relpermg : float
    sonew : float
    mpropvs : int
    nn : int
    
    """
    _min3p.f90wrap_soilparm(uvsnew=uvsnew, sanew=sanew, relperm=relperm, \
        relpermg=relpermg, sonew=sonew, mpropvs=mpropvs, nn=nn)

def sorbconc(tota, totc, distcoff, sw, por, ilog):
    """
    sorbconc(tota, totc, distcoff, sw, por, ilog)
    
    
    Defined at ../src/sorbconc.f lines 68-110
    
    Parameters
    ----------
    tota : float
    totc : float
    distcoff : float
    sw : float
    por : float
    ilog : int
    
    """
    _min3p.f90wrap_sorbconc(tota=tota, totc=totc, distcoff=distcoff, sw=sw, por=por, \
        ilog=ilog)

def sorbspc(csb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, \
    sorption_type, sorption_group, component_type, nc, chargesb, namesb, totco, \
    nelec):
    """
    sorbspc(csb, cec, eqsb, gammac, c, xnusb, iasb, jasb, nsb, isb, sorption_type, \
        sorption_group, component_type, nc, chargesb, namesb, totco, nelec)
    
    
    Defined at ../src/sorbspc.f lines 85-262
    
    Parameters
    ----------
    csb : float
    cec : float
    eqsb : float
    gammac : float
    c : float
    xnusb : float
    iasb : int
    jasb : int
    nsb : int
    isb : int
    sorption_type : float
    sorption_group : float
    component_type : float
    nc : int
    chargesb : float
    namesb : int
    totco : float
    nelec : int
    
    """
    _min3p.f90wrap_sorbspc(csb=csb, cec=cec, eqsb=eqsb, gammac=gammac, c=c, \
        xnusb=xnusb, iasb=iasb, jasb=jasb, nsb=nsb, isb=isb, \
        sorption_type=sorption_type, sorption_group=sorption_group, \
        component_type=component_type, nc=nc, chargesb=chargesb, namesb=namesb, \
        totco=totco, nelec=nelec)

def sortcomp(idbg, ilog):
    """
    sortcomp(idbg, ilog)
    
    
    Defined at ../src/sortcomp.f lines 75-226
    
    Parameters
    ----------
    idbg : int
    ilog : int
    
    """
    _min3p.f90wrap_sortcomp(idbg=idbg, ilog=ilog)

def sptldisc():
    """
    sptldisc()
    
    
    Defined at ../src/sptldisc.f lines 107-309
    
    
    """
    _min3p.f90wrap_sptldisc()

def stedflow():
    """
    stedflow()
    
    
    Defined at ../src/stedflow.f lines 67-133
    
    
    """
    _min3p.f90wrap_stedflow()

def surfcomp(cnew, gammac, sw, por, ilog):
    """
    surfcomp(cnew, gammac, sw, por, ilog)
    
    
    Defined at ../src/surfcomp.f lines 101-182
    
    Parameters
    ----------
    cnew : float
    gammac : float
    sw : float
    por : float
    ilog : int
    
    """
    _min3p.f90wrap_surfcomp(cnew=cnew, gammac=gammac, sw=sw, por=por, ilog=ilog)

def tcorr(tempkel):
    """
    tcorr(tempkel)
    
    
    Defined at ../src/tcorr.f lines 130-233
    
    Parameters
    ----------
    tempkel : float
    
    """
    _min3p.f90wrap_tcorr(tempkel=tempkel)

def timeloop():
    """
    timeloop()
    
    
    Defined at ../src/timeloop.f lines 270-739
    
    
    """
    _min3p.f90wrap_timeloop()

def totcona(tota, totc, distcoff, sw, por):
    """
    totcona(tota, totc, distcoff, sw, por)
    
    
    Defined at ../src/totcona.f lines 68-98
    
    Parameters
    ----------
    tota : float
    totc : float
    distcoff : float
    sw : float
    por : float
    
    """
    _min3p.f90wrap_totcona(tota=tota, totc=totc, distcoff=distcoff, sw=sw, por=por)

def totconc(c, cx, totc):
    """
    totconc(c, cx, totc)
    
    
    Defined at ../src/totconc.f lines 60-109
    
    Parameters
    ----------
    c : float
    cx : float
    totc : float
    
    """
    _min3p.f90wrap_totconc(c=c, cx=cx, totc=totc)

def totconcg(g, totg):
    """
    totconcg(g, totg)
    
    
    Defined at ../src/totconcg.f lines 59-91
    
    Parameters
    ----------
    g : float
    totg : float
    
    """
    _min3p.f90wrap_totconcg(g=g, totg=totg)

def totconcsb(tota, totc, distcoff, expfr, langmuir, pol, sw, por):
    """
    totconcsb(tota, totc, distcoff, expfr, langmuir, pol, sw, por)
    
    
    Defined at ../src/totconcsb.f lines 96-187
    
    Parameters
    ----------
    tota : float
    totc : float
    distcoff : float
    expfr : float
    langmuir : int
    pol : float
    sw : float
    por : float
    
    """
    _min3p.f90wrap_totconcsb(tota=tota, totc=totc, distcoff=distcoff, expfr=expfr, \
        langmuir=langmuir, pol=pol, sw=sw, por=por)

def totint(totintaq, idbg):
    """
    totint(totintaq, idbg)
    
    
    Defined at ../src/totint.f lines 72-116
    
    Parameters
    ----------
    totintaq : float
    idbg : int
    
    """
    _min3p.f90wrap_totint(totintaq=totintaq, idbg=idbg)

def totint_w(totintaq_w, idbg):
    """
    totint_w(totintaq_w, idbg)
    
    
    Defined at ../src/totint_w.f lines 70-110
    
    Parameters
    ----------
    totintaq_w : float
    idbg : int
    
    """
    _min3p.f90wrap_totint_w(totintaq_w=totintaq_w, idbg=idbg)

def totmin(ratem, totm):
    """
    totmin(ratem, totm)
    
    
    Defined at ../src/totmin.f lines 60-88
    
    Parameters
    ----------
    ratem : float
    totm : float
    
    """
    _min3p.f90wrap_totmin(ratem=ratem, totm=totm)

def totmin_w(ratem, totm_w):
    """
    totmin_w(ratem, totm_w)
    
    
    Defined at ../src/totmin_w.f lines 59-85
    
    Parameters
    ----------
    ratem : float
    totm_w : float
    
    """
    _min3p.f90wrap_totmin_w(ratem=ratem, totm_w=totm_w)

def totredx(totoxrd, idbg):
    """
    totredx(totoxrd, idbg)
    
    
    Defined at ../src/totredx.f lines 68-117
    
    Parameters
    ----------
    totoxrd : float
    idbg : int
    
    """
    _min3p.f90wrap_totredx(totoxrd=totoxrd, idbg=idbg)

def totredx_w(totoxrd_w, idbg):
    """
    totredx_w(totoxrd_w, idbg)
    
    
    Defined at ../src/totredx_w.f lines 67-112
    
    Parameters
    ----------
    totoxrd_w : float
    idbg : int
    
    """
    _min3p.f90wrap_totredx_w(totoxrd_w=totoxrd_w, idbg=idbg)

def totsorb(csb, chargesb, rhobulk, totcsb, xnusb, iasb, jasb, nc, nsb, namec, \
    sorption_group, component_type):
    """
    totsorb(csb, chargesb, rhobulk, totcsb, xnusb, iasb, jasb, nc, nsb, namec, \
        sorption_group, component_type)
    
    
    Defined at ../src/totsorb.f lines 68-136
    
    Parameters
    ----------
    csb : float
    chargesb : float
    rhobulk : float
    totcsb : float
    xnusb : float
    iasb : int
    jasb : int
    nc : int
    nsb : int
    namec : int
    sorption_group : float
    component_type : float
    
    """
    _min3p.f90wrap_totsorb(csb=csb, chargesb=chargesb, rhobulk=rhobulk, \
        totcsb=totcsb, xnusb=xnusb, iasb=iasb, jasb=jasb, nc=nc, nsb=nsb, \
        namec=namec, sorption_group=sorption_group, component_type=component_type)

def tprfrtlc(totc, c, cx, gammac, gammax, cm, g, cec_l, distcoff, aream, phim, \
    phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, \
    iunit2, iunit3, iunit4, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, \
    iunit10, prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, \
    update_porosity):
    """
    tprfrtlc(totc, c, cx, gammac, gammax, cm, g, cec_l, distcoff, aream, phim, \
        phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, \
        iunit2, iunit3, iunit4, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, \
        iunit10, prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, \
        update_porosity)
    
    
    Defined at ../src/tprfrtlc.f lines 338-1408
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    cm : float
    g : float
    cec_l : float
    distcoff : float
    aream : float
    phim : float
    phimold : float
    strion : float
    tempkel : float
    hhead : float
    zg : float
    time : float
    deltat : float
    sw : float
    porvol : float
    iunit1 : int
    iunit2 : int
    iunit3 : int
    iunit4 : int
    iunit11 : int
    iunit5 : int
    iunit6 : int
    iunit7 : int
    iunit8 : int
    iunit9 : int
    iunit10 : int
    prefix : float
    l_prfx : int
    tec_header : bool
    ivolume : int
    ntstp : int
    zone_name : float
    l_zone_name : int
    update_porosity : bool
    
    """
    _min3p.f90wrap_tprfrtlc(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        cm=cm, g=g, cec_l=cec_l, distcoff=distcoff, aream=aream, phim=phim, \
        phimold=phimold, strion=strion, tempkel=tempkel, hhead=hhead, zg=zg, \
        time=time, deltat=deltat, sw=sw, porvol=porvol, iunit1=iunit1, \
        iunit2=iunit2, iunit3=iunit3, iunit4=iunit4, iunit11=iunit11, iunit5=iunit5, \
        iunit6=iunit6, iunit7=iunit7, iunit8=iunit8, iunit9=iunit9, iunit10=iunit10, \
        prefix=prefix, l_prfx=l_prfx, tec_header=tec_header, ivolume=ivolume, \
        ntstp=ntstp, zone_name=zone_name, l_zone_name=l_zone_name, \
        update_porosity=update_porosity)

def tprfrtlcg0(totc, c, cx, gammac, gammax, cm, cec_l, distcoff, aream, phim, \
    phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, \
    iunit2, iunit3, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, iunit10, \
    prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, \
    update_porosity):
    """
    tprfrtlcg0(totc, c, cx, gammac, gammax, cm, cec_l, distcoff, aream, phim, \
        phimold, strion, tempkel, hhead, zg, time, deltat, sw, porvol, iunit1, \
        iunit2, iunit3, iunit11, iunit5, iunit6, iunit7, iunit8, iunit9, iunit10, \
        prefix, l_prfx, tec_header, ivolume, ntstp, zone_name, l_zone_name, \
        update_porosity)
    
    
    Defined at ../src/tprfrtlcg0.f lines 330-1391
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    cm : float
    cec_l : float
    distcoff : float
    aream : float
    phim : float
    phimold : float
    strion : float
    tempkel : float
    hhead : float
    zg : float
    time : float
    deltat : float
    sw : float
    porvol : float
    iunit1 : int
    iunit2 : int
    iunit3 : int
    iunit11 : int
    iunit5 : int
    iunit6 : int
    iunit7 : int
    iunit8 : int
    iunit9 : int
    iunit10 : int
    prefix : float
    l_prfx : int
    tec_header : bool
    ivolume : int
    ntstp : int
    zone_name : float
    l_zone_name : int
    update_porosity : bool
    
    """
    _min3p.f90wrap_tprfrtlcg0(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        cm=cm, cec_l=cec_l, distcoff=distcoff, aream=aream, phim=phim, \
        phimold=phimold, strion=strion, tempkel=tempkel, hhead=hhead, zg=zg, \
        time=time, deltat=deltat, sw=sw, porvol=porvol, iunit1=iunit1, \
        iunit2=iunit2, iunit3=iunit3, iunit11=iunit11, iunit5=iunit5, iunit6=iunit6, \
        iunit7=iunit7, iunit8=iunit8, iunit9=iunit9, iunit10=iunit10, prefix=prefix, \
        l_prfx=l_prfx, tec_header=tec_header, ivolume=ivolume, ntstp=ntstp, \
        zone_name=zone_name, l_zone_name=l_zone_name, \
        update_porosity=update_porosity)

def tprfrtlcm0(totc, c, cx, gammac, gammax, g, cec_l, distcoff, strion, tempkel, \
    hhead, zg, time, deltat, sw, porvol, iunit1, iunit2, iunit3, iunit4, \
    iunit11, iunit5, iunit6, iunit10, prefix, l_prfx, tec_header, ivolume, \
    ntstp, zone_name, l_zone_name, update_porosity):
    """
    tprfrtlcm0(totc, c, cx, gammac, gammax, g, cec_l, distcoff, strion, tempkel, \
        hhead, zg, time, deltat, sw, porvol, iunit1, iunit2, iunit3, iunit4, \
        iunit11, iunit5, iunit6, iunit10, prefix, l_prfx, tec_header, ivolume, \
        ntstp, zone_name, l_zone_name, update_porosity)
    
    
    Defined at ../src/tprfrtlcm0.f lines 330-1391
    
    Parameters
    ----------
    totc : float
    c : float
    cx : float
    gammac : float
    gammax : float
    g : float
    cec_l : float
    distcoff : float
    strion : float
    tempkel : float
    hhead : float
    zg : float
    time : float
    deltat : float
    sw : float
    porvol : float
    iunit1 : int
    iunit2 : int
    iunit3 : int
    iunit4 : int
    iunit11 : int
    iunit5 : int
    iunit6 : int
    iunit10 : int
    prefix : float
    l_prfx : int
    tec_header : bool
    ivolume : int
    ntstp : int
    zone_name : float
    l_zone_name : int
    update_porosity : bool
    
    """
    _min3p.f90wrap_tprfrtlcm0(totc=totc, c=c, cx=cx, gammac=gammac, gammax=gammax, \
        g=g, cec_l=cec_l, distcoff=distcoff, strion=strion, tempkel=tempkel, \
        hhead=hhead, zg=zg, time=time, deltat=deltat, sw=sw, porvol=porvol, \
        iunit1=iunit1, iunit2=iunit2, iunit3=iunit3, iunit4=iunit4, iunit11=iunit11, \
        iunit5=iunit5, iunit6=iunit6, iunit10=iunit10, prefix=prefix, l_prfx=l_prfx, \
        tec_header=tec_header, ivolume=ivolume, ntstp=ntstp, zone_name=zone_name, \
        l_zone_name=l_zone_name, update_porosity=update_porosity)

def tprfvs(ivol):
    """
    tprfvs(ivol)
    
    
    Defined at ../src/tprfvs.f lines 68-141
    
    Parameters
    ----------
    ivol : int
    
    """
    _min3p.f90wrap_tprfvs(ivol=ivol)

def tranbcrt():
    """
    tranbcrt()
    
    
    Defined at ../src/tranbcrt.f lines 240-628
    
    
    """
    _min3p.f90wrap_tranbcrt()

def tranflow():
    """
    tranflow()
    
    
    Defined at ../src/tranflow.f lines 40-69
    
    
    """
    _min3p.f90wrap_tranflow()

def tranunit(igb):
    """
    tranunit(igb)
    
    
    Defined at ../src/tranunit.f lines 100-149
    
    Parameters
    ----------
    igb : int
    
    """
    _min3p.f90wrap_tranunit(igb=igb)

def tsteplc(cnew, cold, ulc):
    """
    tsteplc(cnew, cold, ulc)
    
    
    Defined at ../src/tsteplc.f lines 50-83
    
    Parameters
    ----------
    cnew : float
    cold : float
    ulc : float
    
    """
    _min3p.f90wrap_tsteplc(cnew=cnew, cold=cold, ulc=ulc)

def tsteprt():
    """
    tsteprt()
    
    
    Defined at ../src/tsteprt.f lines 89-179
    
    
    """
    _min3p.f90wrap_tsteprt()

def tstepvs():
    """
    tstepvs()
    
    
    Defined at ../src/tstepvs.f lines 52-75
    
    
    """
    _min3p.f90wrap_tstepvs()

def update_tau(im, tivol):
    """
    update_tau(im, tivol)
    
    
    Defined at ../src/update_tau.f lines 16-55
    
    Parameters
    ----------
    im : int
    tivol : float
    
    """
    _min3p.f90wrap_update_tau(im=im, tivol=tivol)

def updatelc(c, ulc, ilog, not_converged, zone_name):
    """
    updatelc(c, ulc, ilog, not_converged, zone_name)
    
    
    Defined at ../src/updatelc.f lines 86-201
    
    Parameters
    ----------
    c : float
    ulc : float
    ilog : int
    not_converged : bool
    zone_name : float
    
    """
    _min3p.f90wrap_updatelc(c=c, ulc=ulc, ilog=ilog, not_converged=not_converged, \
        zone_name=zone_name)

def updatert():
    """
    updatert()
    
    
    Defined at ../src/updatert.f lines 95-321
    
    
    """
    _min3p.f90wrap_updatert()

def updatevs():
    """
    updatevs()
    
    
    Defined at ../src/updatevs.f lines 80-183
    
    
    """
    _min3p.f90wrap_updatevs()

def updtbcvs():
    """
    updtbcvs()
    
    
    Defined at ../src/updtbcvs.f lines 140-469
    
    
    """
    _min3p.f90wrap_updtbcvs()

def updtetp():
    """
    updtetp()
    
    
    Defined at ../src/updtetp.f lines 56-104
    
    
    """
    _min3p.f90wrap_updtetp()

def updtrootdensity():
    """
    updtrootdensity()
    
    
    Defined at ../src/updtrootdensity.f90 lines 55-320
    
    
    ------------------------ COUPLAGE 1D -----------------------
    """
    _min3p.f90wrap_updtrootdensity()

def updtsurf(c, ulc, ilog, not_converged):
    """
    updtsurf(c, ulc, ilog, not_converged)
    
    
    Defined at ../src/updtsurf.f lines 86-198
    
    Parameters
    ----------
    c : float
    ulc : float
    ilog : int
    not_converged : bool
    
    """
    _min3p.f90wrap_updtsurf(c=c, ulc=ulc, ilog=ilog, not_converged=not_converged)

def updtsvap(c, cx, gammac, gammax, strion):
    """
    updtsvap(c, cx, gammac, gammax, strion)
    
    
    Defined at ../src/updtsvap.f lines 131-208
    
    Parameters
    ----------
    c : float
    cx : float
    gammac : float
    gammax : float
    strion : float
    
    """
    _min3p.f90wrap_updtsvap(c=c, cx=cx, gammac=gammac, gammax=gammax, strion=strion)

def updtsvgp(c, gammac, g, totcg, tempkel):
    """
    updtsvgp(c, gammac, g, totcg, tempkel)
    
    
    Defined at ../src/updtsvgp.f lines 42-62
    
    Parameters
    ----------
    c : float
    gammac : float
    g : float
    totcg : float
    tempkel : float
    
    """
    _min3p.f90wrap_updtsvgp(c=c, gammac=gammac, g=g, totcg=totcg, tempkel=tempkel)

def updtsvmp(cmnewm, cmoldm, phim, aream, ratem, delt):
    """
    updtsvmp(cmnewm, cmoldm, phim, aream, ratem, delt)
    
    
    Defined at ../src/updtsvmp.f lines 98-220
    
    Parameters
    ----------
    cmnewm : float
    cmoldm : float
    phim : float
    aream : float
    ratem : float
    delt : float
    
    """
    _min3p.f90wrap_updtsvmp(cmnewm=cmnewm, cmoldm=cmoldm, phim=phim, aream=aream, \
        ratem=ratem, delt=delt)

def velocity(nvx, nvy, nvz, iavs, javs, cinfvs_a, dimcv, xg, yg, zg, uvsnew, \
    hhead, relperm, idbg, ilog, ivel, upstream, fully_saturated, njavs, nn, \
    half_cells):
    """
    velocity(nvx, nvy, nvz, iavs, javs, cinfvs_a, dimcv, xg, yg, zg, uvsnew, hhead, \
        relperm, idbg, ilog, ivel, upstream, fully_saturated, njavs, nn, half_cells)
    
    
    Defined at ../src/velocity.f lines 107-256
    
    Parameters
    ----------
    nvx : int
    nvy : int
    nvz : int
    iavs : int array
    javs : int array
    cinfvs_a : float
    dimcv : float
    xg : float
    yg : float
    zg : float
    uvsnew : float
    hhead : float
    relperm : float
    idbg : int
    ilog : int
    ivel : int
    upstream : bool
    fully_saturated : bool
    njavs : int
    nn : int
    half_cells : bool
    
    """
    _min3p.f90wrap_velocity(nvx=nvx, nvy=nvy, nvz=nvz, iavs=iavs, javs=javs, \
        cinfvs_a=cinfvs_a, dimcv=dimcv, xg=xg, yg=yg, zg=zg, uvsnew=uvsnew, \
        hhead=hhead, relperm=relperm, idbg=idbg, ilog=ilog, ivel=ivel, \
        upstream=upstream, fully_saturated=fully_saturated, njavs=njavs, nn=nn, \
        half_cells=half_cells)

def velocityg(l_sufx, suffix):
    """
    velocityg(l_sufx, suffix)
    
    
    Defined at ../src/velocityg.f lines 213-1002
    
    Parameters
    ----------
    l_sufx : int
    suffix : float
    
    """
    _min3p.f90wrap_velocityg(l_sufx=l_sufx, suffix=suffix)

def vsflow():
    """
    vsflow()
    
    
    Defined at ../src/vsflow.f lines 126-348
    
    
    """
    _min3p.f90wrap_vsflow()

def weed():
    """
    weed()
    
    
    Defined at ../src/weed.f lines 79-122
    
    
    """
    _min3p.f90wrap_weed()

def welcome():
    """
    welcome()
    
    
    Defined at ../src/welcome_pc.f lines 37-84
    
    
    """
    _min3p.f90wrap_welcome()

def wgprop(totg_i, totg_j, totg, g_i, g_j, g, molfrac_i, molfrac_j, molfracg, \
    relpermg_i, relpermg_j, relpg, dens_i, dens_j, densg, visc_i, visc_j, viscg, \
    gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, nc, ng, gacc):
    """
    wgprop(totg_i, totg_j, totg, g_i, g_j, g, molfrac_i, molfrac_j, molfracg, \
        relpermg_i, relpermg_j, relpg, dens_i, dens_j, densg, visc_i, visc_j, viscg, \
        gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, nc, ng, gacc)
    
    
    Defined at ../src/wgprop.f lines 76-195
    
    Parameters
    ----------
    totg_i : float
    totg_j : float
    totg : float
    g_i : float
    g_j : float
    g : float
    molfrac_i : int
    molfrac_j : int
    molfracg : int
    relpermg_i : float
    relpermg_j : float
    relpg : float
    dens_i : float
    dens_j : float
    densg : float
    visc_i : float
    visc_j : float
    viscg : float
    gpi : float
    gpj : float
    gpij : float
    zgi : float
    zgj : float
    spt_weight : float
    iupsgx : int
    nc : int
    ng : int
    gacc : float
    
    """
    _min3p.f90wrap_wgprop(totg_i=totg_i, totg_j=totg_j, totg=totg, g_i=g_i, g_j=g_j, \
        g=g, molfrac_i=molfrac_i, molfrac_j=molfrac_j, molfracg=molfracg, \
        relpermg_i=relpermg_i, relpermg_j=relpermg_j, relpg=relpg, dens_i=dens_i, \
        dens_j=dens_j, densg=densg, visc_i=visc_i, visc_j=visc_j, viscg=viscg, \
        gpi=gpi, gpj=gpj, gpij=gpij, zgi=zgi, zgj=zgj, spt_weight=spt_weight, \
        iupsgx=iupsgx, nc=nc, ng=ng, gacc=gacc)

def wgpropd(totg_i, totg_j, totg, relpermg_i, relpermg_j, relpg, dens_i, dens_j, \
    densg, visc_i, visc_j, viscg, gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, \
    factor, nc, ng, gacc):
    """
    wgpropd(totg_i, totg_j, totg, relpermg_i, relpermg_j, relpg, dens_i, dens_j, \
        densg, visc_i, visc_j, viscg, gpi, gpj, gpij, zgi, zgj, spt_weight, iupsgx, \
        factor, nc, ng, gacc)
    
    
    Defined at ../src/wgpropd.f lines 63-175
    
    Parameters
    ----------
    totg_i : float
    totg_j : float
    totg : float
    relpermg_i : float
    relpermg_j : float
    relpg : float
    dens_i : float
    dens_j : float
    densg : float
    visc_i : float
    visc_j : float
    viscg : float
    gpi : float
    gpj : float
    gpij : float
    zgi : float
    zgj : float
    spt_weight : float
    iupsgx : int
    factor : float
    nc : int
    ng : int
    gacc : float
    
    """
    _min3p.f90wrap_wgpropd(totg_i=totg_i, totg_j=totg_j, totg=totg, \
        relpermg_i=relpermg_i, relpermg_j=relpermg_j, relpg=relpg, dens_i=dens_i, \
        dens_j=dens_j, densg=densg, visc_i=visc_i, visc_j=visc_j, viscg=viscg, \
        gpi=gpi, gpj=gpj, gpij=gpij, zgi=zgi, zgj=zgj, spt_weight=spt_weight, \
        iupsgx=iupsgx, factor=factor, nc=nc, ng=ng, gacc=gacc)

def ws209(lfile, nn, nitmax, numit, idetail, ia, ja, iaf, iafd, jaf, lorder, a, \
    af, x, b, res, work, restol, deltol, nja, njaf, over_flow, rnorm, rmupdate):
    """
    ws209(lfile, nn, nitmax, numit, idetail, ia, ja, iaf, iafd, jaf, lorder, a, af, \
        x, b, res, work, restol, deltol, nja, njaf, over_flow, rnorm, rmupdate)
    
    
    Defined at ../src/ws209.f lines 74-223
    
    Parameters
    ----------
    lfile : int
    nn : int
    nitmax : int
    numit : int
    idetail : int
    ia : int array
    ja : int array
    iaf : int array
    iafd : int array
    jaf : int array
    lorder : int array
    a : float
    af : float
    x : float
    b : float
    res : float
    work : float
    restol : float
    deltol : float
    nja : int
    njaf : int
    over_flow : bool
    rnorm : float
    rmupdate : float
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_ws209(lfile=lfile, nn=nn, nitmax=nitmax, numit=numit, \
        idetail=idetail, ia=ia, ja=ja, iaf=iaf, iafd=iafd, jaf=jaf, lorder=lorder, \
        a=a, af=af, x=x, b=b, res=res, work=work, restol=restol, deltol=deltol, \
        nja=nja, njaf=njaf, over_flow=over_flow, rnorm=rnorm, rmupdate=rmupdate)

def bicgstab(lfile, nn, idetail, nitmax, numit, ia, ja, iaf, iafd, jaf, \
    converged, a, af, x, res, restol, rnorm, rmupdate, deltol, res0, pvec, vbar, \
    avbar, svec, zvec, tvec, temp, lorder, nja, njaf):
    """
    bicgstab(lfile, nn, idetail, nitmax, numit, ia, ja, iaf, iafd, jaf, converged, \
        a, af, x, res, restol, rnorm, rmupdate, deltol, res0, pvec, vbar, avbar, \
        svec, zvec, tvec, temp, lorder, nja, njaf)
    
    
    Defined at ../src/ws209.f lines 231-406
    
    Parameters
    ----------
    lfile : int
    nn : int
    idetail : int
    nitmax : int
    numit : int
    ia : int array
    ja : int array
    iaf : int array
    iafd : int array
    jaf : int array
    converged : bool
    a : float
    af : float
    x : float
    res : float
    restol : float
    rnorm : float
    rmupdate : float
    deltol : float
    res0 : float
    pvec : float
    vbar : float
    avbar : float
    svec : float
    zvec : float
    tvec : float
    temp : float
    lorder : int array
    nja : int
    njaf : int
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_bicgstab(lfile=lfile, nn=nn, idetail=idetail, nitmax=nitmax, \
        numit=numit, ia=ia, ja=ja, iaf=iaf, iafd=iafd, jaf=jaf, converged=converged, \
        a=a, af=af, x=x, res=res, restol=restol, rnorm=rnorm, rmupdate=rmupdate, \
        deltol=deltol, res0=res0, pvec=pvec, vbar=vbar, avbar=avbar, svec=svec, \
        zvec=zvec, tvec=tvec, temp=temp, lorder=lorder, nja=nja, njaf=njaf)

def loweruppersolve(nn, njaf, x, b, af, temp, iaf, iafd, jaf, lorder):
    """
    loweruppersolve(nn, njaf, x, b, af, temp, iaf, iafd, jaf, lorder)
    
    
    Defined at ../src/ws209.f lines 416-492
    
    Parameters
    ----------
    nn : int
    njaf : int
    x : float
    b : float
    af : float
    temp : float
    iaf : int array
    iafd : int array
    jaf : int array
    lorder : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_loweruppersolve(nn=nn, njaf=njaf, x=x, b=b, af=af, temp=temp, \
        iaf=iaf, iafd=iafd, jaf=jaf, lorder=lorder)

def matrixvectormultiply(nn, nja, x, b, a, ia, ja):
    """
    matrixvectormultiply(nn, nja, x, b, a, ia, ja)
    
    
    Defined at ../src/ws209.f lines 497-541
    
    Parameters
    ----------
    nn : int
    nja : int
    x : float
    b : float
    a : float
    ia : int array
    ja : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_matrixvectormultiply(nn=nn, nja=nja, x=x, b=b, a=a, ia=ia, ja=ja)

def idamax(n, dx):
    """
    idamax = idamax(n, dx)
    
    
    Defined at ../src/ws209.f lines 582-612
    
    Parameters
    ----------
    n : int
    dx : float
    
    Returns
    -------
    idamax : int
    
    -----------------------------------------------------------------------
    """
    idamax = _min3p.f90wrap_idamax(n=n, dx=dx)
    return idamax

def incompletefactorization(nn, nja, njaf, b, a, af, row, ia, ja, iaf, iafd, \
    jaf, list, lorder, invord):
    """
    incompletefactorization(nn, nja, njaf, b, a, af, row, ia, ja, iaf, iafd, jaf, \
        list, lorder, invord)
    
    
    Defined at ../src/ws209.f lines 622-759
    
    Parameters
    ----------
    nn : int
    nja : int
    njaf : int
    b : float
    a : float
    af : float
    row : float
    ia : int array
    ja : int array
    iaf : int array
    iafd : int array
    jaf : int array
    list : int array
    lorder : int array
    invord : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_incompletefactorization(nn=nn, nja=nja, njaf=njaf, b=b, a=a, \
        af=af, row=row, ia=ia, ja=ja, iaf=iaf, iafd=iafd, jaf=jaf, list=list, \
        lorder=lorder, invord=invord)

def symbolicfactorization(lfile, nn, nja, njaf, mnjaf, level, list, ia, ja, row, \
    levptr, iaf, iafd, jaf, lorder, invord):
    """
    symbolicfactorization(lfile, nn, nja, njaf, mnjaf, level, list, ia, ja, row, \
        levptr, iaf, iafd, jaf, lorder, invord)
    
    
    Defined at ../src/ws209.f lines 765-951
    
    Parameters
    ----------
    lfile : int
    nn : int
    nja : int
    njaf : int
    mnjaf : int
    level : int
    list : int array
    ia : int array
    ja : int array
    row : int array
    levptr : int array
    iaf : int array
    iafd : int array
    jaf : int array
    lorder : int array
    invord : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_symbolicfactorization(lfile=lfile, nn=nn, nja=nja, njaf=njaf, \
        mnjaf=mnjaf, level=level, list=list, ia=ia, ja=ja, row=row, levptr=levptr, \
        iaf=iaf, iafd=iafd, jaf=jaf, lorder=lorder, invord=invord)

def naturalordering(nn, lorder, invord):
    """
    naturalordering(nn, lorder, invord)
    
    
    Defined at ../src/ws209.f lines 963-991
    
    Parameters
    ----------
    nn : int
    lorder : int array
    invord : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_naturalordering(nn=nn, lorder=lorder, invord=invord)

def rcmordering(nn, nja, ia, ja, lorder, invord, mask, xls):
    """
    rcmordering(nn, nja, ia, ja, lorder, invord, mask, xls)
    
    
    Defined at ../src/ws209.f lines 996-1073
    
    Parameters
    ----------
    nn : int
    nja : int
    ia : int array
    ja : int array
    lorder : int array
    invord : int array
    mask : bool array
    xls : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_rcmordering(nn=nn, nja=nja, ia=ia, ja=ja, lorder=lorder, \
        invord=invord, mask=mask, xls=xls)

def findperipheralnode(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls):
    """
    findperipheralnode(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls)
    
    
    Defined at ../src/ws209.f lines 1079-1171
    
    Parameters
    ----------
    nn : int
    nja : int
    rnode : int
    ia : int array
    ja : int array
    mask : bool array
    nlvl : int
    xls : int array
    ls : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_findperipheralnode(nn=nn, nja=nja, rnode=rnode, ia=ia, ja=ja, \
        mask=mask, nlvl=nlvl, xls=xls, ls=ls)

def rootedlevelstructure(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls):
    """
    rootedlevelstructure(nn, nja, rnode, ia, ja, mask, nlvl, xls, ls)
    
    
    Defined at ../src/ws209.f lines 1177-1271
    
    Parameters
    ----------
    nn : int
    nja : int
    rnode : int
    ia : int array
    ja : int array
    mask : bool array
    nlvl : int
    xls : int array
    ls : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_rootedlevelstructure(nn=nn, nja=nja, rnode=rnode, ia=ia, ja=ja, \
        mask=mask, nlvl=nlvl, xls=xls, ls=ls)

def reversecuthillmckee(nn, nja, rnode, ia, ja, mask, lorder, ccsize, deg):
    """
    reversecuthillmckee(nn, nja, rnode, ia, ja, mask, lorder, ccsize, deg)
    
    
    Defined at ../src/ws209.f lines 1277-1405
    
    Parameters
    ----------
    nn : int
    nja : int
    rnode : int
    ia : int array
    ja : int array
    mask : bool array
    lorder : int array
    ccsize : int
    deg : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_reversecuthillmckee(nn=nn, nja=nja, rnode=rnode, ia=ia, ja=ja, \
        mask=mask, lorder=lorder, ccsize=ccsize, deg=deg)

def degree(nn, nja, rnode, ia, ja, mask, deg, ccsize, ls):
    """
    degree(nn, nja, rnode, ia, ja, mask, deg, ccsize, ls)
    
    
    Defined at ../src/ws209.f lines 1410-1513
    
    Parameters
    ----------
    nn : int
    nja : int
    rnode : int
    ia : int array
    ja : int array
    mask : bool array
    deg : int array
    ccsize : int
    ls : int array
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_degree(nn=nn, nja=nja, rnode=rnode, ia=ia, ja=ja, mask=mask, \
        deg=deg, ccsize=ccsize, ls=ls)

def bubblesort(list, n):
    """
    bubblesort(list, n)
    
    
    Defined at ../src/ws209.f lines 1522-1564
    
    Parameters
    ----------
    list : int array
    n : int
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_bubblesort(list=list, n=n)

def binaryfind(nn, nja, ia, ja, jband, nj, ni):
    """
    binaryfind(nn, nja, ia, ja, jband, nj, ni)
    
    
    Defined at ../src/ws209.f lines 1569-1654
    
    Parameters
    ----------
    nn : int
    nja : int
    ia : int array
    ja : int array
    jband : int
    nj : int
    ni : int
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_binaryfind(nn=nn, nja=nja, ia=ia, ja=ja, jband=jband, nj=nj, \
        ni=ni)

def check(number, maximum, lfile):
    """
    check(number, maximum, lfile)
    
    
    Defined at ../src/ws209.f lines 1659-1687
    
    Parameters
    ----------
    number : int
    maximum : int
    lfile : int
    
    -----------------------------------------------------------------------
    """
    _min3p.f90wrap_check(number=number, maximum=maximum, lfile=lfile)

def xyzcoord():
    """
    xyzcoord()
    
    
    Defined at ../src/xyzcoord.f lines 146-487
    
    
    """
    _min3p.f90wrap_xyzcoord()

def zero_i4(i4, n1, n2, n3):
    """
    zero_i4(i4, n1, n2, n3)
    
    
    Defined at ../src/zero_i4.f lines 34-45
    
    Parameters
    ----------
    i4 : int
    n1 : int
    n2 : int
    n3 : int
    
    """
    _min3p.f90wrap_zero_i4(i4=i4, n1=n1, n2=n2, n3=n3)

def zero_r4(r4, n1, n2, n3):
    """
    zero_r4(r4, n1, n2, n3)
    
    
    Defined at ../src/zero_r4.f lines 40-51
    
    Parameters
    ----------
    r4 : float
    n1 : int
    n2 : int
    n3 : int
    
    """
    _min3p.f90wrap_zero_r4(r4=r4, n1=n1, n2=n2, n3=n3)

def zero_r8(r8, n1, n2, n3):
    """
    zero_r8(r8, n1, n2, n3)
    
    
    Defined at ../src/zero_r8.f lines 40-51
    
    Parameters
    ----------
    r8 : float
    n1 : int
    n2 : int
    n3 : int
    
    """
    _min3p.f90wrap_zero_r8(r8=r8, n1=n1, n2=n2, n3=n3)

