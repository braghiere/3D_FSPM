! Module phys defined in file ../src/phys.f

subroutine f90wrap_phys__get__por(f90wrap_por)
    use phys, only: phys_por => por
    implicit none
    real(8), intent(out) :: f90wrap_por
    
    f90wrap_por = phys_por
end subroutine f90wrap_phys__get__por

subroutine f90wrap_phys__set__por(f90wrap_por)
    use phys, only: phys_por => por
    implicit none
    real(8), intent(in) :: f90wrap_por
    
    phys_por = f90wrap_por
end subroutine f90wrap_phys__set__por

subroutine f90wrap_phys__array__pvol(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_pvol => pvol
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_pvol)) then
        dshape(1:1) = shape(phys_pvol)
        dloc = loc(phys_pvol)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__pvol

subroutine f90wrap_phys__array__condxx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_condxx => condxx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_condxx)) then
        dshape(1:1) = shape(phys_condxx)
        dloc = loc(phys_condxx)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__condxx

subroutine f90wrap_phys__array__condyy(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_condyy => condyy
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_condyy)) then
        dshape(1:1) = shape(phys_condyy)
        dloc = loc(phys_condyy)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__condyy

subroutine f90wrap_phys__array__condzz(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_condzz => condzz
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_condzz)) then
        dshape(1:1) = shape(phys_condzz)
        dloc = loc(phys_condzz)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__condzz

subroutine f90wrap_phys__array__permx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_permx => permx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_permx)) then
        dshape(1:1) = shape(phys_permx)
        dloc = loc(phys_permx)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__permx

subroutine f90wrap_phys__array__permy(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_permy => permy
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_permy)) then
        dshape(1:1) = shape(phys_permy)
        dloc = loc(phys_permy)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__permy

subroutine f90wrap_phys__array__permz(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_permz => permz
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_permz)) then
        dshape(1:1) = shape(phys_permz)
        dloc = loc(phys_permz)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__permz

subroutine f90wrap_phys__array__spstor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_spstor => spstor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_spstor)) then
        dshape(1:1) = shape(phys_spstor)
        dloc = loc(phys_spstor)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__spstor

subroutine f90wrap_phys__array__swr(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_swr => swr
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_swr)) then
        dshape(1:1) = shape(phys_swr)
        dloc = loc(phys_swr)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__swr

subroutine f90wrap_phys__array__spalpha(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_spalpha => spalpha
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_spalpha)) then
        dshape(1:1) = shape(phys_spalpha)
        dloc = loc(phys_spalpha)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__spalpha

subroutine f90wrap_phys__array__spbeta(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_spbeta => spbeta
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_spbeta)) then
        dshape(1:1) = shape(phys_spbeta)
        dloc = loc(phys_spbeta)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__spbeta

subroutine f90wrap_phys__array__spgamma(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_spgamma => spgamma
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_spgamma)) then
        dshape(1:1) = shape(phys_spgamma)
        dloc = loc(phys_spgamma)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__spgamma

subroutine f90wrap_phys__array__expn(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_expn => expn
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_expn)) then
        dshape(1:1) = shape(phys_expn)
        dloc = loc(phys_expn)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__expn

subroutine f90wrap_phys__array__aentry(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_aentry => aentry
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_aentry)) then
        dshape(1:1) = shape(phys_aentry)
        dloc = loc(phys_aentry)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__aentry

subroutine f90wrap_phys__array__satwdry(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_satwdry => satwdry
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_satwdry)) then
        dshape(1:1) = shape(phys_satwdry)
        dloc = loc(phys_satwdry)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__satwdry

subroutine f90wrap_phys__array__h1dry(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_h1dry => h1dry
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_h1dry)) then
        dshape(1:1) = shape(phys_h1dry)
        dloc = loc(phys_h1dry)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__h1dry

subroutine f90wrap_phys__get__nzn(f90wrap_nzn)
    use phys, only: phys_nzn => nzn
    implicit none
    integer(4), intent(out) :: f90wrap_nzn
    
    f90wrap_nzn = phys_nzn
end subroutine f90wrap_phys__get__nzn

subroutine f90wrap_phys__set__nzn(f90wrap_nzn)
    use phys, only: phys_nzn => nzn
    implicit none
    integer(4), intent(in) :: f90wrap_nzn
    
    phys_nzn = f90wrap_nzn
end subroutine f90wrap_phys__set__nzn

subroutine f90wrap_phys__get__permeability_field(f90wrap_permeability_field)
    use phys, only: phys_permeability_field => permeability_field
    implicit none
    logical, intent(out) :: f90wrap_permeability_field
    
    f90wrap_permeability_field = phys_permeability_field
end subroutine f90wrap_phys__get__permeability_field

subroutine f90wrap_phys__set__permeability_field(f90wrap_permeability_field)
    use phys, only: phys_permeability_field => permeability_field
    implicit none
    logical, intent(in) :: f90wrap_permeability_field
    
    phys_permeability_field = f90wrap_permeability_field
end subroutine f90wrap_phys__set__permeability_field

subroutine f90wrap_phys__get__randomdistrib_K(f90wrap_randomdistrib_K)
    use phys, only: phys_randomdistrib_K => randomdistrib_K
    implicit none
    logical, intent(out) :: f90wrap_randomdistrib_K
    
    f90wrap_randomdistrib_K = phys_randomdistrib_K
end subroutine f90wrap_phys__get__randomdistrib_K

subroutine f90wrap_phys__set__randomdistrib_K(f90wrap_randomdistrib_K)
    use phys, only: phys_randomdistrib_K => randomdistrib_K
    implicit none
    logical, intent(in) :: f90wrap_randomdistrib_K
    
    phys_randomdistrib_K = f90wrap_randomdistrib_K
end subroutine f90wrap_phys__set__randomdistrib_K

subroutine f90wrap_phys__get__pure_evaporation(f90wrap_pure_evaporation)
    use phys, only: phys_pure_evaporation => pure_evaporation
    implicit none
    logical, intent(out) :: f90wrap_pure_evaporation
    
    f90wrap_pure_evaporation = phys_pure_evaporation
end subroutine f90wrap_phys__get__pure_evaporation

subroutine f90wrap_phys__set__pure_evaporation(f90wrap_pure_evaporation)
    use phys, only: phys_pure_evaporation => pure_evaporation
    implicit none
    logical, intent(in) :: f90wrap_pure_evaporation
    
    phys_pure_evaporation = f90wrap_pure_evaporation
end subroutine f90wrap_phys__set__pure_evaporation

subroutine f90wrap_phys__get__oil_saturation(f90wrap_oil_saturation)
    use phys, only: phys_oil_saturation => oil_saturation
    implicit none
    logical, intent(out) :: f90wrap_oil_saturation
    
    f90wrap_oil_saturation = phys_oil_saturation
end subroutine f90wrap_phys__get__oil_saturation

subroutine f90wrap_phys__set__oil_saturation(f90wrap_oil_saturation)
    use phys, only: phys_oil_saturation => oil_saturation
    implicit none
    logical, intent(in) :: f90wrap_oil_saturation
    
    phys_oil_saturation = f90wrap_oil_saturation
end subroutine f90wrap_phys__set__oil_saturation

subroutine f90wrap_phys__array__disx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_disx => disx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_disx)) then
        dshape(1:1) = shape(phys_disx)
        dloc = loc(phys_disx)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__disx

subroutine f90wrap_phys__array__disy(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_disy => disy
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_disy)) then
        dshape(1:1) = shape(phys_disy)
        dloc = loc(phys_disy)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__disy

subroutine f90wrap_phys__array__disz(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_disz => disz
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_disz)) then
        dshape(1:1) = shape(phys_disz)
        dloc = loc(phys_disz)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__disz

subroutine f90wrap_phys__get__diff_a(f90wrap_diff_a)
    use phys, only: phys_diff_a => diff_a
    implicit none
    real(8), intent(out) :: f90wrap_diff_a
    
    f90wrap_diff_a = phys_diff_a
end subroutine f90wrap_phys__get__diff_a

subroutine f90wrap_phys__set__diff_a(f90wrap_diff_a)
    use phys, only: phys_diff_a => diff_a
    implicit none
    real(8), intent(in) :: f90wrap_diff_a
    
    phys_diff_a = f90wrap_diff_a
end subroutine f90wrap_phys__set__diff_a

subroutine f90wrap_phys__get__diff_g(f90wrap_diff_g)
    use phys, only: phys_diff_g => diff_g
    implicit none
    real(8), intent(out) :: f90wrap_diff_g
    
    f90wrap_diff_g = phys_diff_g
end subroutine f90wrap_phys__get__diff_g

subroutine f90wrap_phys__set__diff_g(f90wrap_diff_g)
    use phys, only: phys_diff_g => diff_g
    implicit none
    real(8), intent(in) :: f90wrap_diff_g
    
    phys_diff_g = f90wrap_diff_g
end subroutine f90wrap_phys__set__diff_g

subroutine f90wrap_phys__get__dens_h2o(f90wrap_dens_h2o)
    use phys, only: phys_dens_h2o => dens_h2o
    implicit none
    real(8), intent(out) :: f90wrap_dens_h2o
    
    f90wrap_dens_h2o = phys_dens_h2o
end subroutine f90wrap_phys__get__dens_h2o

subroutine f90wrap_phys__set__dens_h2o(f90wrap_dens_h2o)
    use phys, only: phys_dens_h2o => dens_h2o
    implicit none
    real(8), intent(in) :: f90wrap_dens_h2o
    
    phys_dens_h2o = f90wrap_dens_h2o
end subroutine f90wrap_phys__set__dens_h2o

subroutine f90wrap_phys__get__visc_h2o(f90wrap_visc_h2o)
    use phys, only: phys_visc_h2o => visc_h2o
    implicit none
    real(8), intent(out) :: f90wrap_visc_h2o
    
    f90wrap_visc_h2o = phys_visc_h2o
end subroutine f90wrap_phys__get__visc_h2o

subroutine f90wrap_phys__set__visc_h2o(f90wrap_visc_h2o)
    use phys, only: phys_visc_h2o => visc_h2o
    implicit none
    real(8), intent(in) :: f90wrap_visc_h2o
    
    phys_visc_h2o = f90wrap_visc_h2o
end subroutine f90wrap_phys__set__visc_h2o

subroutine f90wrap_phys__get__dens_gcnst(f90wrap_dens_gcnst)
    use phys, only: phys_dens_gcnst => dens_gcnst
    implicit none
    real(8), intent(out) :: f90wrap_dens_gcnst
    
    f90wrap_dens_gcnst = phys_dens_gcnst
end subroutine f90wrap_phys__get__dens_gcnst

subroutine f90wrap_phys__set__dens_gcnst(f90wrap_dens_gcnst)
    use phys, only: phys_dens_gcnst => dens_gcnst
    implicit none
    real(8), intent(in) :: f90wrap_dens_gcnst
    
    phys_dens_gcnst = f90wrap_dens_gcnst
end subroutine f90wrap_phys__set__dens_gcnst

subroutine f90wrap_phys__get__visc_gcnst(f90wrap_visc_gcnst)
    use phys, only: phys_visc_gcnst => visc_gcnst
    implicit none
    real(8), intent(out) :: f90wrap_visc_gcnst
    
    f90wrap_visc_gcnst = phys_visc_gcnst
end subroutine f90wrap_phys__get__visc_gcnst

subroutine f90wrap_phys__set__visc_gcnst(f90wrap_visc_gcnst)
    use phys, only: phys_visc_gcnst => visc_gcnst
    implicit none
    real(8), intent(in) :: f90wrap_visc_gcnst
    
    phys_visc_gcnst = f90wrap_visc_gcnst
end subroutine f90wrap_phys__set__visc_gcnst

subroutine f90wrap_phys__get__theta_diff(f90wrap_theta_diff)
    use phys, only: phys_theta_diff => theta_diff
    implicit none
    real(8), intent(out) :: f90wrap_theta_diff
    
    f90wrap_theta_diff = phys_theta_diff
end subroutine f90wrap_phys__get__theta_diff

subroutine f90wrap_phys__set__theta_diff(f90wrap_theta_diff)
    use phys, only: phys_theta_diff => theta_diff
    implicit none
    real(8), intent(in) :: f90wrap_theta_diff
    
    phys_theta_diff = f90wrap_theta_diff
end subroutine f90wrap_phys__set__theta_diff

subroutine f90wrap_phys__array__dens_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_dens_g => dens_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_dens_g)) then
        dshape(1:1) = shape(phys_dens_g)
        dloc = loc(phys_dens_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__dens_g

subroutine f90wrap_phys__array__visc_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_visc_g => visc_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_visc_g)) then
        dshape(1:1) = shape(phys_visc_g)
        dloc = loc(phys_visc_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__visc_g

subroutine f90wrap_phys__array__mdens_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_mdens_g => mdens_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_mdens_g)) then
        dshape(1:1) = shape(phys_mdens_g)
        dloc = loc(phys_mdens_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__mdens_g

subroutine f90wrap_phys__get__update_dens_g(f90wrap_update_dens_g)
    use phys, only: phys_update_dens_g => update_dens_g
    implicit none
    logical, intent(out) :: f90wrap_update_dens_g
    
    f90wrap_update_dens_g = phys_update_dens_g
end subroutine f90wrap_phys__get__update_dens_g

subroutine f90wrap_phys__set__update_dens_g(f90wrap_update_dens_g)
    use phys, only: phys_update_dens_g => update_dens_g
    implicit none
    logical, intent(in) :: f90wrap_update_dens_g
    
    phys_update_dens_g = f90wrap_update_dens_g
end subroutine f90wrap_phys__set__update_dens_g

subroutine f90wrap_phys__get__blanc_diff_g(f90wrap_blanc_diff_g)
    use phys, only: phys_blanc_diff_g => blanc_diff_g
    implicit none
    logical, intent(out) :: f90wrap_blanc_diff_g
    
    f90wrap_blanc_diff_g = phys_blanc_diff_g
end subroutine f90wrap_phys__get__blanc_diff_g

subroutine f90wrap_phys__set__blanc_diff_g(f90wrap_blanc_diff_g)
    use phys, only: phys_blanc_diff_g => blanc_diff_g
    implicit none
    logical, intent(in) :: f90wrap_blanc_diff_g
    
    phys_blanc_diff_g = f90wrap_blanc_diff_g
end subroutine f90wrap_phys__set__blanc_diff_g

subroutine f90wrap_phys__get__diff_press(f90wrap_diff_press)
    use phys, only: phys_diff_press => diff_press
    implicit none
    logical, intent(out) :: f90wrap_diff_press
    
    f90wrap_diff_press = phys_diff_press
end subroutine f90wrap_phys__get__diff_press

subroutine f90wrap_phys__set__diff_press(f90wrap_diff_press)
    use phys, only: phys_diff_press => diff_press
    implicit none
    logical, intent(in) :: f90wrap_diff_press
    
    phys_diff_press = f90wrap_diff_press
end subroutine f90wrap_phys__set__diff_press

subroutine f90wrap_phys__get__diff_temp(f90wrap_diff_temp)
    use phys, only: phys_diff_temp => diff_temp
    implicit none
    logical, intent(out) :: f90wrap_diff_temp
    
    f90wrap_diff_temp = phys_diff_temp
end subroutine f90wrap_phys__get__diff_temp

subroutine f90wrap_phys__set__diff_temp(f90wrap_diff_temp)
    use phys, only: phys_diff_temp => diff_temp
    implicit none
    logical, intent(in) :: f90wrap_diff_temp
    
    phys_diff_temp = f90wrap_diff_temp
end subroutine f90wrap_phys__set__diff_temp

subroutine f90wrap_phys__array__visc_comp_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_visc_comp_g => visc_comp_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(phys_visc_comp_g)) then
        dshape(1:1) = shape(phys_visc_comp_g)
        dloc = loc(phys_visc_comp_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__visc_comp_g

subroutine f90wrap_phys__array__diff_bin_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use phys, only: phys_diff_bin_g => diff_bin_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(phys_diff_bin_g)) then
        dshape(1:2) = shape(phys_diff_bin_g)
        dloc = loc(phys_diff_bin_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_phys__array__diff_bin_g

! End of module phys defined in file ../src/phys.f

