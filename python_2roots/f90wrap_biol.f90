! Module biol defined in file ../src/biol.f

subroutine f90wrap_biol__get__root_uptake(f90wrap_root_uptake)
    use biol, only: biol_root_uptake => root_uptake
    implicit none
    logical, intent(out) :: f90wrap_root_uptake
    
    f90wrap_root_uptake = biol_root_uptake
end subroutine f90wrap_biol__get__root_uptake

subroutine f90wrap_biol__set__root_uptake(f90wrap_root_uptake)
    use biol, only: biol_root_uptake => root_uptake
    implicit none
    logical, intent(in) :: f90wrap_root_uptake
    
    biol_root_uptake = f90wrap_root_uptake
end subroutine f90wrap_biol__set__root_uptake

subroutine f90wrap_biol__get__vegetation_growth(f90wrap_vegetation_growth)
    use biol, only: biol_vegetation_growth => vegetation_growth
    implicit none
    logical, intent(out) :: f90wrap_vegetation_growth
    
    f90wrap_vegetation_growth = biol_vegetation_growth
end subroutine f90wrap_biol__get__vegetation_growth

subroutine f90wrap_biol__set__vegetation_growth(f90wrap_vegetation_growth)
    use biol, only: biol_vegetation_growth => vegetation_growth
    implicit none
    logical, intent(in) :: f90wrap_vegetation_growth
    
    biol_vegetation_growth = f90wrap_vegetation_growth
end subroutine f90wrap_biol__set__vegetation_growth

subroutine f90wrap_biol__get__passive_uptake(f90wrap_passive_uptake)
    use biol, only: biol_passive_uptake => passive_uptake
    implicit none
    logical, intent(out) :: f90wrap_passive_uptake
    
    f90wrap_passive_uptake = biol_passive_uptake
end subroutine f90wrap_biol__get__passive_uptake

subroutine f90wrap_biol__set__passive_uptake(f90wrap_passive_uptake)
    use biol, only: biol_passive_uptake => passive_uptake
    implicit none
    logical, intent(in) :: f90wrap_passive_uptake
    
    biol_passive_uptake = f90wrap_passive_uptake
end subroutine f90wrap_biol__set__passive_uptake

subroutine f90wrap_biol__get__two_plants(f90wrap_two_plants)
    use biol, only: biol_two_plants => two_plants
    implicit none
    logical, intent(out) :: f90wrap_two_plants
    
    f90wrap_two_plants = biol_two_plants
end subroutine f90wrap_biol__get__two_plants

subroutine f90wrap_biol__set__two_plants(f90wrap_two_plants)
    use biol, only: biol_two_plants => two_plants
    implicit none
    logical, intent(in) :: f90wrap_two_plants
    
    biol_two_plants = f90wrap_two_plants
end subroutine f90wrap_biol__set__two_plants

subroutine f90wrap_biol__get__update_root_rld(f90wrap_update_root_rld)
    use biol, only: biol_update_root_rld => update_root_rld
    implicit none
    logical, intent(out) :: f90wrap_update_root_rld
    
    f90wrap_update_root_rld = biol_update_root_rld
end subroutine f90wrap_biol__get__update_root_rld

subroutine f90wrap_biol__set__update_root_rld(f90wrap_update_root_rld)
    use biol, only: biol_update_root_rld => update_root_rld
    implicit none
    logical, intent(in) :: f90wrap_update_root_rld
    
    biol_update_root_rld = f90wrap_update_root_rld
end subroutine f90wrap_biol__set__update_root_rld

subroutine f90wrap_biol__get__inside_rld(f90wrap_inside_rld)
    use biol, only: biol_inside_rld => inside_rld
    implicit none
    logical, intent(out) :: f90wrap_inside_rld
    
    f90wrap_inside_rld = biol_inside_rld
end subroutine f90wrap_biol__get__inside_rld

subroutine f90wrap_biol__set__inside_rld(f90wrap_inside_rld)
    use biol, only: biol_inside_rld => inside_rld
    implicit none
    logical, intent(in) :: f90wrap_inside_rld
    
    biol_inside_rld = f90wrap_inside_rld
end subroutine f90wrap_biol__set__inside_rld

subroutine f90wrap_biol__get__coupled_archi_rld(f90wrap_coupled_archi_rld)
    use biol, only: biol_coupled_archi_rld => coupled_archi_rld
    implicit none
    logical, intent(out) :: f90wrap_coupled_archi_rld
    
    f90wrap_coupled_archi_rld = biol_coupled_archi_rld
end subroutine f90wrap_biol__get__coupled_archi_rld

subroutine f90wrap_biol__set__coupled_archi_rld(f90wrap_coupled_archi_rld)
    use biol, only: biol_coupled_archi_rld => coupled_archi_rld
    implicit none
    logical, intent(in) :: f90wrap_coupled_archi_rld
    
    biol_coupled_archi_rld = f90wrap_coupled_archi_rld
end subroutine f90wrap_biol__set__coupled_archi_rld

subroutine f90wrap_biol__get__maillage_rld_coupled(f90wrap_maillage_rld_coupled)
    use biol, only: biol_maillage_rld_coupled => maillage_rld_coupled
    implicit none
    logical, intent(out) :: f90wrap_maillage_rld_coupled
    
    f90wrap_maillage_rld_coupled = biol_maillage_rld_coupled
end subroutine f90wrap_biol__get__maillage_rld_coupled

subroutine f90wrap_biol__set__maillage_rld_coupled(f90wrap_maillage_rld_coupled)
    use biol, only: biol_maillage_rld_coupled => maillage_rld_coupled
    implicit none
    logical, intent(in) :: f90wrap_maillage_rld_coupled
    
    biol_maillage_rld_coupled = f90wrap_maillage_rld_coupled
end subroutine f90wrap_biol__set__maillage_rld_coupled

subroutine f90wrap_biol__get__file_rlddata(f90wrap_file_rlddata)
    use biol, only: biol_file_rlddata => file_rlddata
    implicit none
    logical, intent(out) :: f90wrap_file_rlddata
    
    f90wrap_file_rlddata = biol_file_rlddata
end subroutine f90wrap_biol__get__file_rlddata

subroutine f90wrap_biol__set__file_rlddata(f90wrap_file_rlddata)
    use biol, only: biol_file_rlddata => file_rlddata
    implicit none
    logical, intent(in) :: f90wrap_file_rlddata
    
    biol_file_rlddata = f90wrap_file_rlddata
end subroutine f90wrap_biol__set__file_rlddata

subroutine f90wrap_biol__get__rootdensitynill(f90wrap_rootdensitynill)
    use biol, only: biol_rootdensitynill => rootdensitynill
    implicit none
    logical, intent(out) :: f90wrap_rootdensitynill
    
    f90wrap_rootdensitynill = biol_rootdensitynill
end subroutine f90wrap_biol__get__rootdensitynill

subroutine f90wrap_biol__set__rootdensitynill(f90wrap_rootdensitynill)
    use biol, only: biol_rootdensitynill => rootdensitynill
    implicit none
    logical, intent(in) :: f90wrap_rootdensitynill
    
    biol_rootdensitynill = f90wrap_rootdensitynill
end subroutine f90wrap_biol__set__rootdensitynill

subroutine f90wrap_biol__get__pet(f90wrap_pet)
    use biol, only: biol_pet => pet
    implicit none
    real(8), intent(out) :: f90wrap_pet
    
    f90wrap_pet = biol_pet
end subroutine f90wrap_biol__get__pet

subroutine f90wrap_biol__set__pet(f90wrap_pet)
    use biol, only: biol_pet => pet
    implicit none
    real(8), intent(in) :: f90wrap_pet
    
    biol_pet = f90wrap_pet
end subroutine f90wrap_biol__set__pet

subroutine f90wrap_biol__get__pe_soil(f90wrap_pe_soil)
    use biol, only: biol_pe_soil => pe_soil
    implicit none
    real(8), intent(out) :: f90wrap_pe_soil
    
    f90wrap_pe_soil = biol_pe_soil
end subroutine f90wrap_biol__get__pe_soil

subroutine f90wrap_biol__set__pe_soil(f90wrap_pe_soil)
    use biol, only: biol_pe_soil => pe_soil
    implicit none
    real(8), intent(in) :: f90wrap_pe_soil
    
    biol_pe_soil = f90wrap_pe_soil
end subroutine f90wrap_biol__set__pe_soil

subroutine f90wrap_biol__get__scale_aboveground(f90wrap_scale_aboveground)
    use biol, only: biol_scale_aboveground => scale_aboveground
    implicit none
    real(8), intent(out) :: f90wrap_scale_aboveground
    
    f90wrap_scale_aboveground = biol_scale_aboveground
end subroutine f90wrap_biol__get__scale_aboveground

subroutine f90wrap_biol__set__scale_aboveground(f90wrap_scale_aboveground)
    use biol, only: biol_scale_aboveground => scale_aboveground
    implicit none
    real(8), intent(in) :: f90wrap_scale_aboveground
    
    biol_scale_aboveground = f90wrap_scale_aboveground
end subroutine f90wrap_biol__set__scale_aboveground

subroutine f90wrap_biol__get__transp_pot_sharing(f90wrap_transp_pot_sharing)
    use biol, only: biol_transp_pot_sharing => transp_pot_sharing
    implicit none
    real(8), intent(out) :: f90wrap_transp_pot_sharing
    
    f90wrap_transp_pot_sharing = biol_transp_pot_sharing
end subroutine f90wrap_biol__get__transp_pot_sharing

subroutine f90wrap_biol__set__transp_pot_sharing(f90wrap_transp_pot_sharing)
    use biol, only: biol_transp_pot_sharing => transp_pot_sharing
    implicit none
    real(8), intent(in) :: f90wrap_transp_pot_sharing
    
    biol_transp_pot_sharing = f90wrap_transp_pot_sharing
end subroutine f90wrap_biol__set__transp_pot_sharing

subroutine f90wrap_biol__get__canopy_int(f90wrap_canopy_int)
    use biol, only: biol_canopy_int => canopy_int
    implicit none
    real(8), intent(out) :: f90wrap_canopy_int
    
    f90wrap_canopy_int = biol_canopy_int
end subroutine f90wrap_biol__get__canopy_int

subroutine f90wrap_biol__set__canopy_int(f90wrap_canopy_int)
    use biol, only: biol_canopy_int => canopy_int
    implicit none
    real(8), intent(in) :: f90wrap_canopy_int
    
    biol_canopy_int = f90wrap_canopy_int
end subroutine f90wrap_biol__set__canopy_int

subroutine f90wrap_biol__get__time_soi(f90wrap_time_soi)
    use biol, only: biol_time_soi => time_soi
    implicit none
    real(8), intent(out) :: f90wrap_time_soi
    
    f90wrap_time_soi = biol_time_soi
end subroutine f90wrap_biol__get__time_soi

subroutine f90wrap_biol__set__time_soi(f90wrap_time_soi)
    use biol, only: biol_time_soi => time_soi
    implicit none
    real(8), intent(in) :: f90wrap_time_soi
    
    biol_time_soi = f90wrap_time_soi
end subroutine f90wrap_biol__set__time_soi

subroutine f90wrap_biol__get__time_rld(f90wrap_time_rld)
    use biol, only: biol_time_rld => time_rld
    implicit none
    real(8), intent(out) :: f90wrap_time_rld
    
    f90wrap_time_rld = biol_time_rld
end subroutine f90wrap_biol__get__time_rld

subroutine f90wrap_biol__set__time_rld(f90wrap_time_rld)
    use biol, only: biol_time_rld => time_rld
    implicit none
    real(8), intent(in) :: f90wrap_time_rld
    
    biol_time_rld = f90wrap_time_rld
end subroutine f90wrap_biol__set__time_rld

subroutine f90wrap_biol__get__isoi(f90wrap_isoi)
    use biol, only: biol_isoi => isoi
    implicit none
    integer(4), intent(out) :: f90wrap_isoi
    
    f90wrap_isoi = biol_isoi
end subroutine f90wrap_biol__get__isoi

subroutine f90wrap_biol__set__isoi(f90wrap_isoi)
    use biol, only: biol_isoi => isoi
    implicit none
    integer(4), intent(in) :: f90wrap_isoi
    
    biol_isoi = f90wrap_isoi
end subroutine f90wrap_biol__set__isoi

subroutine f90wrap_biol__get__irld(f90wrap_irld)
    use biol, only: biol_irld => irld
    implicit none
    integer(4), intent(out) :: f90wrap_irld
    
    f90wrap_irld = biol_irld
end subroutine f90wrap_biol__get__irld

subroutine f90wrap_biol__set__irld(f90wrap_irld)
    use biol, only: biol_irld => irld
    implicit none
    integer(4), intent(in) :: f90wrap_irld
    
    biol_irld = f90wrap_irld
end subroutine f90wrap_biol__set__irld

subroutine f90wrap_biol__array__h1lim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_h1lim => h1lim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_h1lim)) then
        dshape(1:1) = shape(biol_h1lim)
        dloc = loc(biol_h1lim)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__h1lim

subroutine f90wrap_biol__array__h1field(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_h1field => h1field
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_h1field)) then
        dshape(1:1) = shape(biol_h1field)
        dloc = loc(biol_h1field)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__h1field

subroutine f90wrap_biol__array__h1opt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_h1opt => h1opt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_h1opt)) then
        dshape(1:1) = shape(biol_h1opt)
        dloc = loc(biol_h1opt)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__h1opt

subroutine f90wrap_biol__array__satwlim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_satwlim => satwlim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_satwlim)) then
        dshape(1:1) = shape(biol_satwlim)
        dloc = loc(biol_satwlim)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__satwlim

subroutine f90wrap_biol__array__satwfield(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_satwfield => satwfield
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_satwfield)) then
        dshape(1:1) = shape(biol_satwfield)
        dloc = loc(biol_satwfield)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__satwfield

subroutine f90wrap_biol__array__satwopt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_satwopt => satwopt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_satwopt)) then
        dshape(1:1) = shape(biol_satwopt)
        dloc = loc(biol_satwopt)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__satwopt

subroutine f90wrap_biol__array__satwh1(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_satwh1 => satwh1
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_satwh1)) then
        dshape(1:1) = shape(biol_satwh1)
        dloc = loc(biol_satwh1)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__satwh1

subroutine f90wrap_biol__array__rootdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_rootdiff => rootdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rootdiff)) then
        dshape(1:1) = shape(biol_rootdiff)
        dloc = loc(biol_rootdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rootdiff

subroutine f90wrap_biol__array__totrootdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_totrootdiff => totrootdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_totrootdiff)) then
        dshape(1:1) = shape(biol_totrootdiff)
        dloc = loc(biol_totrootdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__totrootdiff

subroutine f90wrap_biol__array__rootdiff2(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_rootdiff2 => rootdiff2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rootdiff2)) then
        dshape(1:1) = shape(biol_rootdiff2)
        dloc = loc(biol_rootdiff2)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rootdiff2

subroutine f90wrap_biol__array__totrootdiff2(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use biol, only: biol_totrootdiff2 => totrootdiff2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_totrootdiff2)) then
        dshape(1:1) = shape(biol_totrootdiff2)
        dloc = loc(biol_totrootdiff2)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__totrootdiff2

subroutine f90wrap_biol__array__rootlengthdens(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use biol, only: biol_rootlengthdens => rootlengthdens
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rootlengthdens)) then
        dshape(1:1) = shape(biol_rootlengthdens)
        dloc = loc(biol_rootlengthdens)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rootlengthdens

subroutine f90wrap_biol__array__rootlengthdens2(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use biol, only: biol_rootlengthdens2 => rootlengthdens2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rootlengthdens2)) then
        dshape(1:1) = shape(biol_rootlengthdens2)
        dloc = loc(biol_rootlengthdens2)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rootlengthdens2

subroutine f90wrap_biol__array__rld(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_rld => rld
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rld)) then
        dshape(1:1) = shape(biol_rld)
        dloc = loc(biol_rld)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rld

subroutine f90wrap_biol__array__rld2(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_rld2 => rld2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_rld2)) then
        dshape(1:1) = shape(biol_rld2)
        dloc = loc(biol_rld2)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__rld2

subroutine f90wrap_biol__array__water_red_factor(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use biol, only: biol_water_red_factor => water_red_factor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_water_red_factor)) then
        dshape(1:1) = shape(biol_water_red_factor)
        dloc = loc(biol_water_red_factor)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__water_red_factor

subroutine f90wrap_biol__array__time_demand(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_time_demand => time_demand
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_time_demand)) then
        dshape(1:1) = shape(biol_time_demand)
        dloc = loc(biol_time_demand)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__time_demand

subroutine f90wrap_biol__array__demand_rate(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_demand_rate => demand_rate
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_demand_rate)) then
        dshape(1:1) = shape(biol_demand_rate)
        dloc = loc(biol_demand_rate)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__demand_rate

subroutine f90wrap_biol__array__var_factor_dem_rate(dummy_this, nd, dtype, &
    dshape, dloc)
    use parm
    use biol, only: biol_var_factor_dem_rate => var_factor_dem_rate
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_var_factor_dem_rate)) then
        dshape(1:1) = shape(biol_var_factor_dem_rate)
        dloc = loc(biol_var_factor_dem_rate)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__var_factor_dem_rate

subroutine f90wrap_biol__array__uptakefactor(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use biol, only: biol_uptakefactor => uptakefactor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_uptakefactor)) then
        dshape(1:1) = shape(biol_uptakefactor)
        dloc = loc(biol_uptakefactor)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__uptakefactor

subroutine f90wrap_biol__array__puf(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use biol, only: biol_puf => puf
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(biol_puf)) then
        dshape(1:1) = shape(biol_puf)
        dloc = loc(biol_puf)
    else
        dloc = 0
    end if
end subroutine f90wrap_biol__array__puf

subroutine f90wrap_biol__get__canopy_evap_factor(f90wrap_canopy_evap_factor)
    use biol, only: biol_canopy_evap_factor => canopy_evap_factor
    implicit none
    real(8), intent(out) :: f90wrap_canopy_evap_factor
    
    f90wrap_canopy_evap_factor = biol_canopy_evap_factor
end subroutine f90wrap_biol__get__canopy_evap_factor

subroutine f90wrap_biol__set__canopy_evap_factor(f90wrap_canopy_evap_factor)
    use biol, only: biol_canopy_evap_factor => canopy_evap_factor
    implicit none
    real(8), intent(in) :: f90wrap_canopy_evap_factor
    
    biol_canopy_evap_factor = f90wrap_canopy_evap_factor
end subroutine f90wrap_biol__set__canopy_evap_factor

subroutine f90wrap_biol__get__rew0(f90wrap_rew0)
    use biol, only: biol_rew0 => rew0
    implicit none
    real(8), intent(out) :: f90wrap_rew0
    
    f90wrap_rew0 = biol_rew0
end subroutine f90wrap_biol__get__rew0

subroutine f90wrap_biol__set__rew0(f90wrap_rew0)
    use biol, only: biol_rew0 => rew0
    implicit none
    real(8), intent(in) :: f90wrap_rew0
    
    biol_rew0 = f90wrap_rew0
end subroutine f90wrap_biol__set__rew0

subroutine f90wrap_biol__get__p1(f90wrap_p1)
    use biol, only: biol_p1 => p1
    implicit none
    real(8), intent(out) :: f90wrap_p1
    
    f90wrap_p1 = biol_p1
end subroutine f90wrap_biol__get__p1

subroutine f90wrap_biol__set__p1(f90wrap_p1)
    use biol, only: biol_p1 => p1
    implicit none
    real(8), intent(in) :: f90wrap_p1
    
    biol_p1 = f90wrap_p1
end subroutine f90wrap_biol__set__p1

subroutine f90wrap_biol__get__rewm(f90wrap_rewm)
    use biol, only: biol_rewm => rewm
    implicit none
    real(8), intent(out) :: f90wrap_rewm
    
    f90wrap_rewm = biol_rewm
end subroutine f90wrap_biol__get__rewm

subroutine f90wrap_biol__set__rewm(f90wrap_rewm)
    use biol, only: biol_rewm => rewm
    implicit none
    real(8), intent(in) :: f90wrap_rewm
    
    biol_rewm = f90wrap_rewm
end subroutine f90wrap_biol__set__rewm

subroutine f90wrap_biol__get__v_prop(f90wrap_v_prop)
    use biol, only: biol_v_prop => v_prop
    implicit none
    real(8), intent(out) :: f90wrap_v_prop
    
    f90wrap_v_prop = biol_v_prop
end subroutine f90wrap_biol__get__v_prop

subroutine f90wrap_biol__set__v_prop(f90wrap_v_prop)
    use biol, only: biol_v_prop => v_prop
    implicit none
    real(8), intent(in) :: f90wrap_v_prop
    
    biol_v_prop = f90wrap_v_prop
end subroutine f90wrap_biol__set__v_prop

subroutine f90wrap_biol__get__cmws(f90wrap_cmws)
    use biol, only: biol_cmws => cmws
    implicit none
    integer(4), intent(out) :: f90wrap_cmws
    
    f90wrap_cmws = biol_cmws
end subroutine f90wrap_biol__get__cmws

subroutine f90wrap_biol__set__cmws(f90wrap_cmws)
    use biol, only: biol_cmws => cmws
    implicit none
    integer(4), intent(in) :: f90wrap_cmws
    
    biol_cmws = f90wrap_cmws
end subroutine f90wrap_biol__set__cmws

subroutine f90wrap_biol__get__compt_rld_coupled(f90wrap_compt_rld_coupled)
    use biol, only: biol_compt_rld_coupled => compt_rld_coupled
    implicit none
    integer(4), intent(out) :: f90wrap_compt_rld_coupled
    
    f90wrap_compt_rld_coupled = biol_compt_rld_coupled
end subroutine f90wrap_biol__get__compt_rld_coupled

subroutine f90wrap_biol__set__compt_rld_coupled(f90wrap_compt_rld_coupled)
    use biol, only: biol_compt_rld_coupled => compt_rld_coupled
    implicit none
    integer(4), intent(in) :: f90wrap_compt_rld_coupled
    
    biol_compt_rld_coupled = f90wrap_compt_rld_coupled
end subroutine f90wrap_biol__set__compt_rld_coupled

subroutine f90wrap_biol__get__rootlengthdens_field(f90wrap_rootlengthdens_field)
    use biol, only: biol_rootlengthdens_field => rootlengthdens_field
    implicit none
    logical, intent(out) :: f90wrap_rootlengthdens_field
    
    f90wrap_rootlengthdens_field = biol_rootlengthdens_field
end subroutine f90wrap_biol__get__rootlengthdens_field

subroutine f90wrap_biol__set__rootlengthdens_field(f90wrap_rootlengthdens_field)
    use biol, only: biol_rootlengthdens_field => rootlengthdens_field
    implicit none
    logical, intent(in) :: f90wrap_rootlengthdens_field
    
    biol_rootlengthdens_field = f90wrap_rootlengthdens_field
end subroutine f90wrap_biol__set__rootlengthdens_field

subroutine f90wrap_biol__get__randomdistrib_root(f90wrap_randomdistrib_root)
    use biol, only: biol_randomdistrib_root => randomdistrib_root
    implicit none
    logical, intent(out) :: f90wrap_randomdistrib_root
    
    f90wrap_randomdistrib_root = biol_randomdistrib_root
end subroutine f90wrap_biol__get__randomdistrib_root

subroutine f90wrap_biol__set__randomdistrib_root(f90wrap_randomdistrib_root)
    use biol, only: biol_randomdistrib_root => randomdistrib_root
    implicit none
    logical, intent(in) :: f90wrap_randomdistrib_root
    
    biol_randomdistrib_root = f90wrap_randomdistrib_root
end subroutine f90wrap_biol__set__randomdistrib_root

! End of module biol defined in file ../src/biol.f

