! Module chem defined in file ../src/chem.f

subroutine f90wrap_chem__get__acth2omin(f90wrap_acth2omin)
    use chem, only: chem_acth2omin => acth2omin
    implicit none
    real(8), intent(out) :: f90wrap_acth2omin
    
    f90wrap_acth2omin = chem_acth2omin
end subroutine f90wrap_chem__get__acth2omin

subroutine f90wrap_chem__set__acth2omin(f90wrap_acth2omin)
    use chem, only: chem_acth2omin => acth2omin
    implicit none
    real(8), intent(in) :: f90wrap_acth2omin
    
    chem_acth2omin = f90wrap_acth2omin
end subroutine f90wrap_chem__set__acth2omin

subroutine f90wrap_chem__get__dinc_lc(f90wrap_dinc_lc)
    use chem, only: chem_dinc_lc => dinc_lc
    implicit none
    real(8), intent(out) :: f90wrap_dinc_lc
    
    f90wrap_dinc_lc = chem_dinc_lc
end subroutine f90wrap_chem__get__dinc_lc

subroutine f90wrap_chem__set__dinc_lc(f90wrap_dinc_lc)
    use chem, only: chem_dinc_lc => dinc_lc
    implicit none
    real(8), intent(in) :: f90wrap_dinc_lc
    
    chem_dinc_lc = f90wrap_dinc_lc
end subroutine f90wrap_chem__set__dinc_lc

subroutine f90wrap_chem__get__ph_fixed(f90wrap_ph_fixed)
    use chem, only: chem_ph_fixed => ph_fixed
    implicit none
    real(8), intent(out) :: f90wrap_ph_fixed
    
    f90wrap_ph_fixed = chem_ph_fixed
end subroutine f90wrap_chem__get__ph_fixed

subroutine f90wrap_chem__set__ph_fixed(f90wrap_ph_fixed)
    use chem, only: chem_ph_fixed => ph_fixed
    implicit none
    real(8), intent(in) :: f90wrap_ph_fixed
    
    chem_ph_fixed = f90wrap_ph_fixed
end subroutine f90wrap_chem__set__ph_fixed

subroutine f90wrap_chem__get__ph_inc(f90wrap_ph_inc)
    use chem, only: chem_ph_inc => ph_inc
    implicit none
    real(8), intent(out) :: f90wrap_ph_inc
    
    f90wrap_ph_inc = chem_ph_inc
end subroutine f90wrap_chem__get__ph_inc

subroutine f90wrap_chem__set__ph_inc(f90wrap_ph_inc)
    use chem, only: chem_ph_inc => ph_inc
    implicit none
    real(8), intent(in) :: f90wrap_ph_inc
    
    chem_ph_inc = f90wrap_ph_inc
end subroutine f90wrap_chem__set__ph_inc

subroutine f90wrap_chem__get__ph_start(f90wrap_ph_start)
    use chem, only: chem_ph_start => ph_start
    implicit none
    real(8), intent(out) :: f90wrap_ph_start
    
    f90wrap_ph_start = chem_ph_start
end subroutine f90wrap_chem__get__ph_start

subroutine f90wrap_chem__set__ph_start(f90wrap_ph_start)
    use chem, only: chem_ph_start => ph_start
    implicit none
    real(8), intent(in) :: f90wrap_ph_start
    
    chem_ph_start = f90wrap_ph_start
end subroutine f90wrap_chem__set__ph_start

subroutine f90wrap_chem__get__ph_stop(f90wrap_ph_stop)
    use chem, only: chem_ph_stop => ph_stop
    implicit none
    real(8), intent(out) :: f90wrap_ph_stop
    
    f90wrap_ph_stop = chem_ph_stop
end subroutine f90wrap_chem__get__ph_stop

subroutine f90wrap_chem__set__ph_stop(f90wrap_ph_stop)
    use chem, only: chem_ph_stop => ph_stop
    implicit none
    real(8), intent(in) :: f90wrap_ph_stop
    
    chem_ph_stop = f90wrap_ph_stop
end subroutine f90wrap_chem__set__ph_stop

subroutine f90wrap_chem__get__sionmax(f90wrap_sionmax)
    use chem, only: chem_sionmax => sionmax
    implicit none
    real(8), intent(out) :: f90wrap_sionmax
    
    f90wrap_sionmax = chem_sionmax
end subroutine f90wrap_chem__get__sionmax

subroutine f90wrap_chem__set__sionmax(f90wrap_sionmax)
    use chem, only: chem_sionmax => sionmax
    implicit none
    real(8), intent(in) :: f90wrap_sionmax
    
    chem_sionmax = f90wrap_sionmax
end subroutine f90wrap_chem__set__sionmax

subroutine f90wrap_chem__get__srelfac_lc(f90wrap_srelfac_lc)
    use chem, only: chem_srelfac_lc => srelfac_lc
    implicit none
    real(8), intent(out) :: f90wrap_srelfac_lc
    
    f90wrap_srelfac_lc = chem_srelfac_lc
end subroutine f90wrap_chem__get__srelfac_lc

subroutine f90wrap_chem__set__srelfac_lc(f90wrap_srelfac_lc)
    use chem, only: chem_srelfac_lc => srelfac_lc
    implicit none
    real(8), intent(in) :: f90wrap_srelfac_lc
    
    chem_srelfac_lc = f90wrap_srelfac_lc
end subroutine f90wrap_chem__set__srelfac_lc

subroutine f90wrap_chem__get__tempc(f90wrap_tempc)
    use chem, only: chem_tempc => tempc
    implicit none
    real(8), intent(out) :: f90wrap_tempc
    
    f90wrap_tempc = chem_tempc
end subroutine f90wrap_chem__get__tempc

subroutine f90wrap_chem__set__tempc(f90wrap_tempc)
    use chem, only: chem_tempc => tempc
    implicit none
    real(8), intent(in) :: f90wrap_tempc
    
    chem_tempc = f90wrap_tempc
end subroutine f90wrap_chem__set__tempc

subroutine f90wrap_chem__get__tempk(f90wrap_tempk)
    use chem, only: chem_tempk => tempk
    implicit none
    real(8), intent(out) :: f90wrap_tempk
    
    f90wrap_tempk = chem_tempk
end subroutine f90wrap_chem__get__tempk

subroutine f90wrap_chem__set__tempk(f90wrap_tempk)
    use chem, only: chem_tempk => tempk
    implicit none
    real(8), intent(in) :: f90wrap_tempk
    
    chem_tempk = f90wrap_tempk
end subroutine f90wrap_chem__set__tempk

subroutine f90wrap_chem__get__tfinal_lc(f90wrap_tfinal_lc)
    use chem, only: chem_tfinal_lc => tfinal_lc
    implicit none
    real(8), intent(out) :: f90wrap_tfinal_lc
    
    f90wrap_tfinal_lc = chem_tfinal_lc
end subroutine f90wrap_chem__get__tfinal_lc

subroutine f90wrap_chem__set__tfinal_lc(f90wrap_tfinal_lc)
    use chem, only: chem_tfinal_lc => tfinal_lc
    implicit none
    real(8), intent(in) :: f90wrap_tfinal_lc
    
    chem_tfinal_lc = f90wrap_tfinal_lc
end subroutine f90wrap_chem__set__tfinal_lc

subroutine f90wrap_chem__get__tinyrate(f90wrap_tinyrate)
    use chem, only: chem_tinyrate => tinyrate
    implicit none
    real(8), intent(out) :: f90wrap_tinyrate
    
    f90wrap_tinyrate = chem_tinyrate
end subroutine f90wrap_chem__get__tinyrate

subroutine f90wrap_chem__set__tinyrate(f90wrap_tinyrate)
    use chem, only: chem_tinyrate => tinyrate
    implicit none
    real(8), intent(in) :: f90wrap_tinyrate
    
    chem_tinyrate = f90wrap_tinyrate
end subroutine f90wrap_chem__set__tinyrate

subroutine f90wrap_chem__get__time_factor_lc(f90wrap_time_factor_lc)
    use chem, only: chem_time_factor_lc => time_factor_lc
    implicit none
    real(8), intent(out) :: f90wrap_time_factor_lc
    
    f90wrap_time_factor_lc = chem_time_factor_lc
end subroutine f90wrap_chem__get__time_factor_lc

subroutine f90wrap_chem__set__time_factor_lc(f90wrap_time_factor_lc)
    use chem, only: chem_time_factor_lc => time_factor_lc
    implicit none
    real(8), intent(in) :: f90wrap_time_factor_lc
    
    chem_time_factor_lc = f90wrap_time_factor_lc
end subroutine f90wrap_chem__set__time_factor_lc

subroutine f90wrap_chem__get__tol_lc(f90wrap_tol_lc)
    use chem, only: chem_tol_lc => tol_lc
    implicit none
    real(8), intent(out) :: f90wrap_tol_lc
    
    f90wrap_tol_lc = chem_tol_lc
end subroutine f90wrap_chem__get__tol_lc

subroutine f90wrap_chem__set__tol_lc(f90wrap_tol_lc)
    use chem, only: chem_tol_lc => tol_lc
    implicit none
    real(8), intent(in) :: f90wrap_tol_lc
    
    chem_tol_lc = f90wrap_tol_lc
end subroutine f90wrap_chem__set__tol_lc

subroutine f90wrap_chem__array__ncorder(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ncorder => ncorder
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_ncorder)) then
        dshape(1:1) = shape(chem_ncorder)
        dloc = loc(chem_ncorder)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ncorder

subroutine f90wrap_chem__get__iph_steps(f90wrap_iph_steps)
    use chem, only: chem_iph_steps => iph_steps
    implicit none
    integer(4), intent(out) :: f90wrap_iph_steps
    
    f90wrap_iph_steps = chem_iph_steps
end subroutine f90wrap_chem__get__iph_steps

subroutine f90wrap_chem__set__iph_steps(f90wrap_iph_steps)
    use chem, only: chem_iph_steps => iph_steps
    implicit none
    integer(4), intent(in) :: f90wrap_iph_steps
    
    chem_iph_steps = f90wrap_iph_steps
end subroutine f90wrap_chem__set__iph_steps

subroutine f90wrap_chem__get__maxit_lc(f90wrap_maxit_lc)
    use chem, only: chem_maxit_lc => maxit_lc
    implicit none
    integer(4), intent(out) :: f90wrap_maxit_lc
    
    f90wrap_maxit_lc = chem_maxit_lc
end subroutine f90wrap_chem__get__maxit_lc

subroutine f90wrap_chem__set__maxit_lc(f90wrap_maxit_lc)
    use chem, only: chem_maxit_lc => maxit_lc
    implicit none
    integer(4), intent(in) :: f90wrap_maxit_lc
    
    chem_maxit_lc = f90wrap_maxit_lc
end subroutine f90wrap_chem__set__maxit_lc

subroutine f90wrap_chem__get__idetail_lc(f90wrap_idetail_lc)
    use chem, only: chem_idetail_lc => idetail_lc
    implicit none
    integer(4), intent(out) :: f90wrap_idetail_lc
    
    f90wrap_idetail_lc = chem_idetail_lc
end subroutine f90wrap_chem__get__idetail_lc

subroutine f90wrap_chem__set__idetail_lc(f90wrap_idetail_lc)
    use chem, only: chem_idetail_lc => idetail_lc
    implicit none
    integer(4), intent(in) :: f90wrap_idetail_lc
    
    chem_idetail_lc = f90wrap_idetail_lc
end subroutine f90wrap_chem__set__idetail_lc

subroutine f90wrap_chem__get__ittot_lc(f90wrap_ittot_lc)
    use chem, only: chem_ittot_lc => ittot_lc
    implicit none
    integer(4), intent(out) :: f90wrap_ittot_lc
    
    f90wrap_ittot_lc = chem_ittot_lc
end subroutine f90wrap_chem__get__ittot_lc

subroutine f90wrap_chem__set__ittot_lc(f90wrap_ittot_lc)
    use chem, only: chem_ittot_lc => ittot_lc
    implicit none
    integer(4), intent(in) :: f90wrap_ittot_lc
    
    chem_ittot_lc = f90wrap_ittot_lc
end subroutine f90wrap_chem__set__ittot_lc

subroutine f90wrap_chem__get__iter_lc(f90wrap_iter_lc)
    use chem, only: chem_iter_lc => iter_lc
    implicit none
    integer(4), intent(out) :: f90wrap_iter_lc
    
    f90wrap_iter_lc = chem_iter_lc
end subroutine f90wrap_chem__get__iter_lc

subroutine f90wrap_chem__set__iter_lc(f90wrap_iter_lc)
    use chem, only: chem_iter_lc => iter_lc
    implicit none
    integer(4), intent(in) :: f90wrap_iter_lc
    
    chem_iter_lc = f90wrap_iter_lc
end subroutine f90wrap_chem__set__iter_lc

subroutine f90wrap_chem__get__naq(f90wrap_naq)
    use chem, only: chem_naq => naq
    implicit none
    integer(4), intent(out) :: f90wrap_naq
    
    f90wrap_naq = chem_naq
end subroutine f90wrap_chem__get__naq

subroutine f90wrap_chem__set__naq(f90wrap_naq)
    use chem, only: chem_naq => naq
    implicit none
    integer(4), intent(in) :: f90wrap_naq
    
    chem_naq = f90wrap_naq
end subroutine f90wrap_chem__set__naq

subroutine f90wrap_chem__get__nc(f90wrap_nc)
    use chem, only: chem_nc => nc
    implicit none
    integer(4), intent(out) :: f90wrap_nc
    
    f90wrap_nc = chem_nc
end subroutine f90wrap_chem__get__nc

subroutine f90wrap_chem__set__nc(f90wrap_nc)
    use chem, only: chem_nc => nc
    implicit none
    integer(4), intent(in) :: f90wrap_nc
    
    chem_nc = f90wrap_nc
end subroutine f90wrap_chem__set__nc

subroutine f90wrap_chem__get__nx(f90wrap_nx)
    use chem, only: chem_nx => nx
    implicit none
    integer(4), intent(out) :: f90wrap_nx
    
    f90wrap_nx = chem_nx
end subroutine f90wrap_chem__get__nx

subroutine f90wrap_chem__set__nx(f90wrap_nx)
    use chem, only: chem_nx => nx
    implicit none
    integer(4), intent(in) :: f90wrap_nx
    
    chem_nx = f90wrap_nx
end subroutine f90wrap_chem__set__nx

subroutine f90wrap_chem__get__nm(f90wrap_nm)
    use chem, only: chem_nm => nm
    implicit none
    integer(4), intent(out) :: f90wrap_nm
    
    f90wrap_nm = chem_nm
end subroutine f90wrap_chem__get__nm

subroutine f90wrap_chem__set__nm(f90wrap_nm)
    use chem, only: chem_nm => nm
    implicit none
    integer(4), intent(in) :: f90wrap_nm
    
    chem_nm = f90wrap_nm
end subroutine f90wrap_chem__set__nm

subroutine f90wrap_chem__get__nmx(f90wrap_nmx)
    use chem, only: chem_nmx => nmx
    implicit none
    integer(4), intent(out) :: f90wrap_nmx
    
    f90wrap_nmx = chem_nmx
end subroutine f90wrap_chem__get__nmx

subroutine f90wrap_chem__set__nmx(f90wrap_nmx)
    use chem, only: chem_nmx => nmx
    implicit none
    integer(4), intent(in) :: f90wrap_nmx
    
    chem_nmx = f90wrap_nmx
end subroutine f90wrap_chem__set__nmx

subroutine f90wrap_chem__get__nopu(f90wrap_nopu)
    use chem, only: chem_nopu => nopu
    implicit none
    integer(4), intent(out) :: f90wrap_nopu
    
    f90wrap_nopu = chem_nopu
end subroutine f90wrap_chem__get__nopu

subroutine f90wrap_chem__set__nopu(f90wrap_nopu)
    use chem, only: chem_nopu => nopu
    implicit none
    integer(4), intent(in) :: f90wrap_nopu
    
    chem_nopu = f90wrap_nopu
end subroutine f90wrap_chem__set__nopu

subroutine f90wrap_chem__get__ng(f90wrap_ng)
    use chem, only: chem_ng => ng
    implicit none
    integer(4), intent(out) :: f90wrap_ng
    
    f90wrap_ng = chem_ng
end subroutine f90wrap_chem__get__ng

subroutine f90wrap_chem__set__ng(f90wrap_ng)
    use chem, only: chem_ng => ng
    implicit none
    integer(4), intent(in) :: f90wrap_ng
    
    chem_ng = f90wrap_ng
end subroutine f90wrap_chem__set__ng

subroutine f90wrap_chem__get__nr(f90wrap_nr)
    use chem, only: chem_nr => nr
    implicit none
    integer(4), intent(out) :: f90wrap_nr
    
    f90wrap_nr = chem_nr
end subroutine f90wrap_chem__get__nr

subroutine f90wrap_chem__set__nr(f90wrap_nr)
    use chem, only: chem_nr => nr
    implicit none
    integer(4), intent(in) :: f90wrap_nr
    
    chem_nr = f90wrap_nr
end subroutine f90wrap_chem__set__nr

subroutine f90wrap_chem__get__nph_steps(f90wrap_nph_steps)
    use chem, only: chem_nph_steps => nph_steps
    implicit none
    integer(4), intent(out) :: f90wrap_nph_steps
    
    f90wrap_nph_steps = chem_nph_steps
end subroutine f90wrap_chem__get__nph_steps

subroutine f90wrap_chem__set__nph_steps(f90wrap_nph_steps)
    use chem, only: chem_nph_steps => nph_steps
    implicit none
    integer(4), intent(in) :: f90wrap_nph_steps
    
    chem_nph_steps = f90wrap_nph_steps
end subroutine f90wrap_chem__set__nph_steps

subroutine f90wrap_chem__get__ivolindice(f90wrap_ivolindice)
    use chem, only: chem_ivolindice => ivolindice
    implicit none
    integer(4), intent(out) :: f90wrap_ivolindice
    
    f90wrap_ivolindice = chem_ivolindice
end subroutine f90wrap_chem__get__ivolindice

subroutine f90wrap_chem__set__ivolindice(f90wrap_ivolindice)
    use chem, only: chem_ivolindice => ivolindice
    implicit none
    integer(4), intent(in) :: f90wrap_ivolindice
    
    chem_ivolindice = f90wrap_ivolindice
end subroutine f90wrap_chem__set__ivolindice

subroutine f90wrap_chem__array__minequil(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_minequil => minequil
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_minequil)) then
        dshape(1:1) = shape(chem_minequil)
        dloc = loc(chem_minequil)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__minequil

subroutine f90wrap_chem__get__compute_alkalinity(f90wrap_compute_alkalinity)
    use chem, only: chem_compute_alkalinity => compute_alkalinity
    implicit none
    logical, intent(out) :: f90wrap_compute_alkalinity
    
    f90wrap_compute_alkalinity = chem_compute_alkalinity
end subroutine f90wrap_chem__get__compute_alkalinity

subroutine f90wrap_chem__set__compute_alkalinity(f90wrap_compute_alkalinity)
    use chem, only: chem_compute_alkalinity => compute_alkalinity
    implicit none
    logical, intent(in) :: f90wrap_compute_alkalinity
    
    chem_compute_alkalinity = f90wrap_compute_alkalinity
end subroutine f90wrap_chem__set__compute_alkalinity

subroutine f90wrap_chem__get__explicit_surface(f90wrap_explicit_surface)
    use chem, only: chem_explicit_surface => explicit_surface
    implicit none
    logical, intent(out) :: f90wrap_explicit_surface
    
    f90wrap_explicit_surface = chem_explicit_surface
end subroutine f90wrap_chem__get__explicit_surface

subroutine f90wrap_chem__set__explicit_surface(f90wrap_explicit_surface)
    use chem, only: chem_explicit_surface => explicit_surface
    implicit none
    logical, intent(in) :: f90wrap_explicit_surface
    
    chem_explicit_surface = f90wrap_explicit_surface
end subroutine f90wrap_chem__set__explicit_surface

subroutine f90wrap_chem__get__finite_minerals(f90wrap_finite_minerals)
    use chem, only: chem_finite_minerals => finite_minerals
    implicit none
    logical, intent(out) :: f90wrap_finite_minerals
    
    f90wrap_finite_minerals = chem_finite_minerals
end subroutine f90wrap_chem__get__finite_minerals

subroutine f90wrap_chem__set__finite_minerals(f90wrap_finite_minerals)
    use chem, only: chem_finite_minerals => finite_minerals
    implicit none
    logical, intent(in) :: f90wrap_finite_minerals
    
    chem_finite_minerals = f90wrap_finite_minerals
end subroutine f90wrap_chem__set__finite_minerals

subroutine f90wrap_chem__get__implicit_surface(f90wrap_implicit_surface)
    use chem, only: chem_implicit_surface => implicit_surface
    implicit none
    logical, intent(out) :: f90wrap_implicit_surface
    
    f90wrap_implicit_surface = chem_implicit_surface
end subroutine f90wrap_chem__get__implicit_surface

subroutine f90wrap_chem__set__implicit_surface(f90wrap_implicit_surface)
    use chem, only: chem_implicit_surface => implicit_surface
    implicit none
    logical, intent(in) :: f90wrap_implicit_surface
    
    chem_implicit_surface = f90wrap_implicit_surface
end subroutine f90wrap_chem__set__implicit_surface

subroutine f90wrap_chem__get__new_database(f90wrap_new_database)
    use chem, only: chem_new_database => new_database
    implicit none
    logical, intent(out) :: f90wrap_new_database
    
    f90wrap_new_database = chem_new_database
end subroutine f90wrap_chem__get__new_database

subroutine f90wrap_chem__set__new_database(f90wrap_new_database)
    use chem, only: chem_new_database => new_database
    implicit none
    logical, intent(in) :: f90wrap_new_database
    
    chem_new_database = f90wrap_new_database
end subroutine f90wrap_chem__set__new_database

subroutine f90wrap_chem__get__ph_sweep(f90wrap_ph_sweep)
    use chem, only: chem_ph_sweep => ph_sweep
    implicit none
    logical, intent(out) :: f90wrap_ph_sweep
    
    f90wrap_ph_sweep = chem_ph_sweep
end subroutine f90wrap_chem__get__ph_sweep

subroutine f90wrap_chem__set__ph_sweep(f90wrap_ph_sweep)
    use chem, only: chem_ph_sweep => ph_sweep
    implicit none
    logical, intent(in) :: f90wrap_ph_sweep
    
    chem_ph_sweep = f90wrap_ph_sweep
end subroutine f90wrap_chem__set__ph_sweep

subroutine f90wrap_chem__get__reactive_minerals(f90wrap_reactive_minerals)
    use chem, only: chem_reactive_minerals => reactive_minerals
    implicit none
    logical, intent(out) :: f90wrap_reactive_minerals
    
    f90wrap_reactive_minerals = chem_reactive_minerals
end subroutine f90wrap_chem__get__reactive_minerals

subroutine f90wrap_chem__set__reactive_minerals(f90wrap_reactive_minerals)
    use chem, only: chem_reactive_minerals => reactive_minerals
    implicit none
    logical, intent(in) :: f90wrap_reactive_minerals
    
    chem_reactive_minerals = f90wrap_reactive_minerals
end subroutine f90wrap_chem__set__reactive_minerals

subroutine f90wrap_chem__get__redox_equil_lc(f90wrap_redox_equil_lc)
    use chem, only: chem_redox_equil_lc => redox_equil_lc
    implicit none
    logical, intent(out) :: f90wrap_redox_equil_lc
    
    f90wrap_redox_equil_lc = chem_redox_equil_lc
end subroutine f90wrap_chem__get__redox_equil_lc

subroutine f90wrap_chem__set__redox_equil_lc(f90wrap_redox_equil_lc)
    use chem, only: chem_redox_equil_lc => redox_equil_lc
    implicit none
    logical, intent(in) :: f90wrap_redox_equil_lc
    
    chem_redox_equil_lc = f90wrap_redox_equil_lc
end subroutine f90wrap_chem__set__redox_equil_lc

subroutine f90wrap_chem__get__search_database(f90wrap_search_database)
    use chem, only: chem_search_database => search_database
    implicit none
    logical, intent(out) :: f90wrap_search_database
    
    f90wrap_search_database = chem_search_database
end subroutine f90wrap_chem__get__search_database

subroutine f90wrap_chem__set__search_database(f90wrap_search_database)
    use chem, only: chem_search_database => search_database
    implicit none
    logical, intent(in) :: f90wrap_search_database
    
    chem_search_database = f90wrap_search_database
end subroutine f90wrap_chem__set__search_database

subroutine f90wrap_chem__get__specified_ph(f90wrap_specified_ph)
    use chem, only: chem_specified_ph => specified_ph
    implicit none
    logical, intent(out) :: f90wrap_specified_ph
    
    f90wrap_specified_ph = chem_specified_ph
end subroutine f90wrap_chem__get__specified_ph

subroutine f90wrap_chem__set__specified_ph(f90wrap_specified_ph)
    use chem, only: chem_specified_ph => specified_ph
    implicit none
    logical, intent(in) :: f90wrap_specified_ph
    
    chem_specified_ph = f90wrap_specified_ph
end subroutine f90wrap_chem__set__specified_ph

subroutine f90wrap_chem__get__temp_corr(f90wrap_temp_corr)
    use chem, only: chem_temp_corr => temp_corr
    implicit none
    logical, intent(out) :: f90wrap_temp_corr
    
    f90wrap_temp_corr = chem_temp_corr
end subroutine f90wrap_chem__get__temp_corr

subroutine f90wrap_chem__set__temp_corr(f90wrap_temp_corr)
    use chem, only: chem_temp_corr => temp_corr
    implicit none
    logical, intent(in) :: f90wrap_temp_corr
    
    chem_temp_corr = f90wrap_temp_corr
end subroutine f90wrap_chem__set__temp_corr

subroutine f90wrap_chem__get__temp_field(f90wrap_temp_field)
    use chem, only: chem_temp_field => temp_field
    implicit none
    logical, intent(out) :: f90wrap_temp_field
    
    f90wrap_temp_field = chem_temp_field
end subroutine f90wrap_chem__get__temp_field

subroutine f90wrap_chem__set__temp_field(f90wrap_temp_field)
    use chem, only: chem_temp_field => temp_field
    implicit none
    logical, intent(in) :: f90wrap_temp_field
    
    chem_temp_field = f90wrap_temp_field
end subroutine f90wrap_chem__set__temp_field

subroutine f90wrap_chem__get__tstart_to_equil(f90wrap_tstart_to_equil)
    use chem, only: chem_tstart_to_equil => tstart_to_equil
    implicit none
    logical, intent(out) :: f90wrap_tstart_to_equil
    
    f90wrap_tstart_to_equil = chem_tstart_to_equil
end subroutine f90wrap_chem__get__tstart_to_equil

subroutine f90wrap_chem__set__tstart_to_equil(f90wrap_tstart_to_equil)
    use chem, only: chem_tstart_to_equil => tstart_to_equil
    implicit none
    logical, intent(in) :: f90wrap_tstart_to_equil
    
    chem_tstart_to_equil = f90wrap_tstart_to_equil
end subroutine f90wrap_chem__set__tstart_to_equil

subroutine f90wrap_chem__get__tstart_to_tfinal(f90wrap_tstart_to_tfinal)
    use chem, only: chem_tstart_to_tfinal => tstart_to_tfinal
    implicit none
    logical, intent(out) :: f90wrap_tstart_to_tfinal
    
    f90wrap_tstart_to_tfinal = chem_tstart_to_tfinal
end subroutine f90wrap_chem__get__tstart_to_tfinal

subroutine f90wrap_chem__set__tstart_to_tfinal(f90wrap_tstart_to_tfinal)
    use chem, only: chem_tstart_to_tfinal => tstart_to_tfinal
    implicit none
    logical, intent(in) :: f90wrap_tstart_to_tfinal
    
    chem_tstart_to_tfinal = f90wrap_tstart_to_tfinal
end subroutine f90wrap_chem__set__tstart_to_tfinal

subroutine f90wrap_chem__get__adav(f90wrap_adav)
    use chem, only: chem_adav => adav
    implicit none
    real(8), intent(out) :: f90wrap_adav
    
    f90wrap_adav = chem_adav
end subroutine f90wrap_chem__get__adav

subroutine f90wrap_chem__set__adav(f90wrap_adav)
    use chem, only: chem_adav => adav
    implicit none
    real(8), intent(in) :: f90wrap_adav
    
    chem_adav = f90wrap_adav
end subroutine f90wrap_chem__set__adav

subroutine f90wrap_chem__get__avog_const(f90wrap_avog_const)
    use chem, only: chem_avog_const => avog_const
    implicit none
    real(8), intent(out) :: f90wrap_avog_const
    
    f90wrap_avog_const = chem_avog_const
end subroutine f90wrap_chem__get__avog_const

subroutine f90wrap_chem__set__avog_const(f90wrap_avog_const)
    use chem, only: chem_avog_const => avog_const
    implicit none
    real(8), intent(in) :: f90wrap_avog_const
    
    chem_avog_const = f90wrap_avog_const
end subroutine f90wrap_chem__set__avog_const

subroutine f90wrap_chem__get__bdav(f90wrap_bdav)
    use chem, only: chem_bdav => bdav
    implicit none
    real(8), intent(out) :: f90wrap_bdav
    
    f90wrap_bdav = chem_bdav
end subroutine f90wrap_chem__get__bdav

subroutine f90wrap_chem__set__bdav(f90wrap_bdav)
    use chem, only: chem_bdav => bdav
    implicit none
    real(8), intent(in) :: f90wrap_bdav
    
    chem_bdav = f90wrap_bdav
end subroutine f90wrap_chem__set__bdav

subroutine f90wrap_chem__get__diel_const(f90wrap_diel_const)
    use chem, only: chem_diel_const => diel_const
    implicit none
    real(8), intent(out) :: f90wrap_diel_const
    
    f90wrap_diel_const = chem_diel_const
end subroutine f90wrap_chem__get__diel_const

subroutine f90wrap_chem__set__diel_const(f90wrap_diel_const)
    use chem, only: chem_diel_const => diel_const
    implicit none
    real(8), intent(in) :: f90wrap_diel_const
    
    chem_diel_const = f90wrap_diel_const
end subroutine f90wrap_chem__set__diel_const

subroutine f90wrap_chem__get__dhad(f90wrap_dhad)
    use chem, only: chem_dhad => dhad
    implicit none
    real(8), intent(out) :: f90wrap_dhad
    
    f90wrap_dhad = chem_dhad
end subroutine f90wrap_chem__get__dhad

subroutine f90wrap_chem__set__dhad(f90wrap_dhad)
    use chem, only: chem_dhad => dhad
    implicit none
    real(8), intent(in) :: f90wrap_dhad
    
    chem_dhad = f90wrap_dhad
end subroutine f90wrap_chem__set__dhad

subroutine f90wrap_chem__get__dhbd(f90wrap_dhbd)
    use chem, only: chem_dhbd => dhbd
    implicit none
    real(8), intent(out) :: f90wrap_dhbd
    
    f90wrap_dhbd = chem_dhbd
end subroutine f90wrap_chem__get__dhbd

subroutine f90wrap_chem__set__dhbd(f90wrap_dhbd)
    use chem, only: chem_dhbd => dhbd
    implicit none
    real(8), intent(in) :: f90wrap_dhbd
    
    chem_dhbd = f90wrap_dhbd
end subroutine f90wrap_chem__set__dhbd

subroutine f90wrap_chem__get__ehfac(f90wrap_ehfac)
    use chem, only: chem_ehfac => ehfac
    implicit none
    real(8), intent(out) :: f90wrap_ehfac
    
    f90wrap_ehfac = chem_ehfac
end subroutine f90wrap_chem__get__ehfac

subroutine f90wrap_chem__set__ehfac(f90wrap_ehfac)
    use chem, only: chem_ehfac => ehfac
    implicit none
    real(8), intent(in) :: f90wrap_ehfac
    
    chem_ehfac = f90wrap_ehfac
end subroutine f90wrap_chem__set__ehfac

subroutine f90wrap_chem__get__farad_const(f90wrap_farad_const)
    use chem, only: chem_farad_const => farad_const
    implicit none
    real(8), intent(out) :: f90wrap_farad_const
    
    f90wrap_farad_const = chem_farad_const
end subroutine f90wrap_chem__get__farad_const

subroutine f90wrap_chem__set__farad_const(f90wrap_farad_const)
    use chem, only: chem_farad_const => farad_const
    implicit none
    real(8), intent(in) :: f90wrap_farad_const
    
    chem_farad_const = f90wrap_farad_const
end subroutine f90wrap_chem__set__farad_const

subroutine f90wrap_chem__get__g_acc(f90wrap_g_acc)
    use chem, only: chem_g_acc => g_acc
    implicit none
    real(8), intent(out) :: f90wrap_g_acc
    
    f90wrap_g_acc = chem_g_acc
end subroutine f90wrap_chem__get__g_acc

subroutine f90wrap_chem__set__g_acc(f90wrap_g_acc)
    use chem, only: chem_g_acc => g_acc
    implicit none
    real(8), intent(in) :: f90wrap_g_acc
    
    chem_g_acc = f90wrap_g_acc
end subroutine f90wrap_chem__set__g_acc

subroutine f90wrap_chem__get__pa_atm(f90wrap_pa_atm)
    use chem, only: chem_pa_atm => pa_atm
    implicit none
    real(8), intent(out) :: f90wrap_pa_atm
    
    f90wrap_pa_atm = chem_pa_atm
end subroutine f90wrap_chem__get__pa_atm

subroutine f90wrap_chem__set__pa_atm(f90wrap_pa_atm)
    use chem, only: chem_pa_atm => pa_atm
    implicit none
    real(8), intent(in) :: f90wrap_pa_atm
    
    chem_pa_atm = f90wrap_pa_atm
end subroutine f90wrap_chem__set__pa_atm

subroutine f90wrap_chem__get__permit_const(f90wrap_permit_const)
    use chem, only: chem_permit_const => permit_const
    implicit none
    real(8), intent(out) :: f90wrap_permit_const
    
    f90wrap_permit_const = chem_permit_const
end subroutine f90wrap_chem__get__permit_const

subroutine f90wrap_chem__set__permit_const(f90wrap_permit_const)
    use chem, only: chem_permit_const => permit_const
    implicit none
    real(8), intent(in) :: f90wrap_permit_const
    
    chem_permit_const = f90wrap_permit_const
end subroutine f90wrap_chem__set__permit_const

subroutine f90wrap_chem__get__pres_atm(f90wrap_pres_atm)
    use chem, only: chem_pres_atm => pres_atm
    implicit none
    real(8), intent(out) :: f90wrap_pres_atm
    
    f90wrap_pres_atm = chem_pres_atm
end subroutine f90wrap_chem__get__pres_atm

subroutine f90wrap_chem__set__pres_atm(f90wrap_pres_atm)
    use chem, only: chem_pres_atm => pres_atm
    implicit none
    real(8), intent(in) :: f90wrap_pres_atm
    
    chem_pres_atm = f90wrap_pres_atm
end subroutine f90wrap_chem__set__pres_atm

subroutine f90wrap_chem__get__tempcs(f90wrap_tempcs)
    use chem, only: chem_tempcs => tempcs
    implicit none
    real(8), intent(out) :: f90wrap_tempcs
    
    f90wrap_tempcs = chem_tempcs
end subroutine f90wrap_chem__get__tempcs

subroutine f90wrap_chem__set__tempcs(f90wrap_tempcs)
    use chem, only: chem_tempcs => tempcs
    implicit none
    real(8), intent(in) :: f90wrap_tempcs
    
    chem_tempcs = f90wrap_tempcs
end subroutine f90wrap_chem__set__tempcs

subroutine f90wrap_chem__get__tempks(f90wrap_tempks)
    use chem, only: chem_tempks => tempks
    implicit none
    real(8), intent(out) :: f90wrap_tempks
    
    f90wrap_tempks = chem_tempks
end subroutine f90wrap_chem__get__tempks

subroutine f90wrap_chem__set__tempks(f90wrap_tempks)
    use chem, only: chem_tempks => tempks
    implicit none
    real(8), intent(in) :: f90wrap_tempks
    
    chem_tempks = f90wrap_tempks
end subroutine f90wrap_chem__set__tempks

subroutine f90wrap_chem__get__tconv(f90wrap_tconv)
    use chem, only: chem_tconv => tconv
    implicit none
    real(8), intent(out) :: f90wrap_tconv
    
    f90wrap_tconv = chem_tconv
end subroutine f90wrap_chem__get__tconv

subroutine f90wrap_chem__set__tconv(f90wrap_tconv)
    use chem, only: chem_tconv => tconv
    implicit none
    real(8), intent(in) :: f90wrap_tconv
    
    chem_tconv = f90wrap_tconv
end subroutine f90wrap_chem__set__tconv

subroutine f90wrap_chem__get__rgas(f90wrap_rgas)
    use chem, only: chem_rgas => rgas
    implicit none
    real(8), intent(out) :: f90wrap_rgas
    
    f90wrap_rgas = chem_rgas
end subroutine f90wrap_chem__get__rgas

subroutine f90wrap_chem__set__rgas(f90wrap_rgas)
    use chem, only: chem_rgas => rgas
    implicit none
    real(8), intent(in) :: f90wrap_rgas
    
    chem_rgas = f90wrap_rgas
end subroutine f90wrap_chem__set__rgas

subroutine f90wrap_chem__get__rgascal(f90wrap_rgascal)
    use chem, only: chem_rgascal => rgascal
    implicit none
    real(8), intent(out) :: f90wrap_rgascal
    
    f90wrap_rgascal = chem_rgascal
end subroutine f90wrap_chem__get__rgascal

subroutine f90wrap_chem__set__rgascal(f90wrap_rgascal)
    use chem, only: chem_rgascal => rgascal
    implicit none
    real(8), intent(in) :: f90wrap_rgascal
    
    chem_rgascal = f90wrap_rgascal
end subroutine f90wrap_chem__set__rgascal

subroutine f90wrap_chem__get__rgasjoule(f90wrap_rgasjoule)
    use chem, only: chem_rgasjoule => rgasjoule
    implicit none
    real(8), intent(out) :: f90wrap_rgasjoule
    
    f90wrap_rgasjoule = chem_rgasjoule
end subroutine f90wrap_chem__get__rgasjoule

subroutine f90wrap_chem__set__rgasjoule(f90wrap_rgasjoule)
    use chem, only: chem_rgasjoule => rgasjoule
    implicit none
    real(8), intent(in) :: f90wrap_rgasjoule
    
    chem_rgasjoule = f90wrap_rgasjoule
end subroutine f90wrap_chem__set__rgasjoule

subroutine f90wrap_chem__get__rho_w(f90wrap_rho_w)
    use chem, only: chem_rho_w => rho_w
    implicit none
    real(8), intent(out) :: f90wrap_rho_w
    
    f90wrap_rho_w = chem_rho_w
end subroutine f90wrap_chem__get__rho_w

subroutine f90wrap_chem__set__rho_w(f90wrap_rho_w)
    use chem, only: chem_rho_w => rho_w
    implicit none
    real(8), intent(in) :: f90wrap_rho_w
    
    chem_rho_w = f90wrap_rho_w
end subroutine f90wrap_chem__set__rho_w

subroutine f90wrap_chem__get__delt_lc(f90wrap_delt_lc)
    use chem, only: chem_delt_lc => delt_lc
    implicit none
    real(8), intent(out) :: f90wrap_delt_lc
    
    f90wrap_delt_lc = chem_delt_lc
end subroutine f90wrap_chem__get__delt_lc

subroutine f90wrap_chem__set__delt_lc(f90wrap_delt_lc)
    use chem, only: chem_delt_lc => delt_lc
    implicit none
    real(8), intent(in) :: f90wrap_delt_lc
    
    chem_delt_lc = f90wrap_delt_lc
end subroutine f90wrap_chem__set__delt_lc

subroutine f90wrap_chem__get__delt_max_lc(f90wrap_delt_max_lc)
    use chem, only: chem_delt_max_lc => delt_max_lc
    implicit none
    real(8), intent(out) :: f90wrap_delt_max_lc
    
    f90wrap_delt_max_lc = chem_delt_max_lc
end subroutine f90wrap_chem__get__delt_max_lc

subroutine f90wrap_chem__set__delt_max_lc(f90wrap_delt_max_lc)
    use chem, only: chem_delt_max_lc => delt_max_lc
    implicit none
    real(8), intent(in) :: f90wrap_delt_max_lc
    
    chem_delt_max_lc = f90wrap_delt_max_lc
end subroutine f90wrap_chem__set__delt_max_lc

subroutine f90wrap_chem__get__ntstp_lc(f90wrap_ntstp_lc)
    use chem, only: chem_ntstp_lc => ntstp_lc
    implicit none
    integer(4), intent(out) :: f90wrap_ntstp_lc
    
    f90wrap_ntstp_lc = chem_ntstp_lc
end subroutine f90wrap_chem__get__ntstp_lc

subroutine f90wrap_chem__set__ntstp_lc(f90wrap_ntstp_lc)
    use chem, only: chem_ntstp_lc => ntstp_lc
    implicit none
    integer(4), intent(in) :: f90wrap_ntstp_lc
    
    chem_ntstp_lc = f90wrap_ntstp_lc
end subroutine f90wrap_chem__set__ntstp_lc

subroutine f90wrap_chem__get__ilbb(f90wrap_ilbb)
    use chem, only: chem_ilbb => ilbb
    implicit none
    integer(4), intent(out) :: f90wrap_ilbb
    
    f90wrap_ilbb = chem_ilbb
end subroutine f90wrap_chem__get__ilbb

subroutine f90wrap_chem__set__ilbb(f90wrap_ilbb)
    use chem, only: chem_ilbb => ilbb
    implicit none
    integer(4), intent(in) :: f90wrap_ilbb
    
    chem_ilbb = f90wrap_ilbb
end subroutine f90wrap_chem__set__ilbb

subroutine f90wrap_chem__get__ilbc(f90wrap_ilbc)
    use chem, only: chem_ilbc => ilbc
    implicit none
    integer(4), intent(out) :: f90wrap_ilbc
    
    f90wrap_ilbc = chem_ilbc
end subroutine f90wrap_chem__get__ilbc

subroutine f90wrap_chem__set__ilbc(f90wrap_ilbc)
    use chem, only: chem_ilbc => ilbc
    implicit none
    integer(4), intent(in) :: f90wrap_ilbc
    
    chem_ilbc = f90wrap_ilbc
end subroutine f90wrap_chem__set__ilbc

subroutine f90wrap_chem__get__ilbd(f90wrap_ilbd)
    use chem, only: chem_ilbd => ilbd
    implicit none
    integer(4), intent(out) :: f90wrap_ilbd
    
    f90wrap_ilbd = chem_ilbd
end subroutine f90wrap_chem__get__ilbd

subroutine f90wrap_chem__set__ilbd(f90wrap_ilbd)
    use chem, only: chem_ilbd => ilbd
    implicit none
    integer(4), intent(in) :: f90wrap_ilbd
    
    chem_ilbd = f90wrap_ilbd
end subroutine f90wrap_chem__set__ilbd

subroutine f90wrap_chem__get__ilbg(f90wrap_ilbg)
    use chem, only: chem_ilbg => ilbg
    implicit none
    integer(4), intent(out) :: f90wrap_ilbg
    
    f90wrap_ilbg = chem_ilbg
end subroutine f90wrap_chem__get__ilbg

subroutine f90wrap_chem__set__ilbg(f90wrap_ilbg)
    use chem, only: chem_ilbg => ilbg
    implicit none
    integer(4), intent(in) :: f90wrap_ilbg
    
    chem_ilbg = f90wrap_ilbg
end subroutine f90wrap_chem__set__ilbg

subroutine f90wrap_chem__get__ilbgr(f90wrap_ilbgr)
    use chem, only: chem_ilbgr => ilbgr
    implicit none
    integer(4), intent(out) :: f90wrap_ilbgr
    
    f90wrap_ilbgr = chem_ilbgr
end subroutine f90wrap_chem__get__ilbgr

subroutine f90wrap_chem__set__ilbgr(f90wrap_ilbgr)
    use chem, only: chem_ilbgr => ilbgr
    implicit none
    integer(4), intent(in) :: f90wrap_ilbgr
    
    chem_ilbgr = f90wrap_ilbgr
end subroutine f90wrap_chem__set__ilbgr

subroutine f90wrap_chem__get__ilbm(f90wrap_ilbm)
    use chem, only: chem_ilbm => ilbm
    implicit none
    integer(4), intent(out) :: f90wrap_ilbm
    
    f90wrap_ilbm = chem_ilbm
end subroutine f90wrap_chem__get__ilbm

subroutine f90wrap_chem__set__ilbm(f90wrap_ilbm)
    use chem, only: chem_ilbm => ilbm
    implicit none
    integer(4), intent(in) :: f90wrap_ilbm
    
    chem_ilbm = f90wrap_ilbm
end subroutine f90wrap_chem__set__ilbm

subroutine f90wrap_chem__get__ilbi(f90wrap_ilbi)
    use chem, only: chem_ilbi => ilbi
    implicit none
    integer(4), intent(out) :: f90wrap_ilbi
    
    f90wrap_ilbi = chem_ilbi
end subroutine f90wrap_chem__get__ilbi

subroutine f90wrap_chem__set__ilbi(f90wrap_ilbi)
    use chem, only: chem_ilbi => ilbi
    implicit none
    integer(4), intent(in) :: f90wrap_ilbi
    
    chem_ilbi = f90wrap_ilbi
end subroutine f90wrap_chem__set__ilbi

subroutine f90wrap_chem__get__ilbs(f90wrap_ilbs)
    use chem, only: chem_ilbs => ilbs
    implicit none
    integer(4), intent(out) :: f90wrap_ilbs
    
    f90wrap_ilbs = chem_ilbs
end subroutine f90wrap_chem__get__ilbs

subroutine f90wrap_chem__set__ilbs(f90wrap_ilbs)
    use chem, only: chem_ilbs => ilbs
    implicit none
    integer(4), intent(in) :: f90wrap_ilbs
    
    chem_ilbs = f90wrap_ilbs
end subroutine f90wrap_chem__set__ilbs

subroutine f90wrap_chem__get__ilbt(f90wrap_ilbt)
    use chem, only: chem_ilbt => ilbt
    implicit none
    integer(4), intent(out) :: f90wrap_ilbt
    
    f90wrap_ilbt = chem_ilbt
end subroutine f90wrap_chem__get__ilbt

subroutine f90wrap_chem__set__ilbt(f90wrap_ilbt)
    use chem, only: chem_ilbt => ilbt
    implicit none
    integer(4), intent(in) :: f90wrap_ilbt
    
    chem_ilbt = f90wrap_ilbt
end subroutine f90wrap_chem__set__ilbt

subroutine f90wrap_chem__get__ilbv(f90wrap_ilbv)
    use chem, only: chem_ilbv => ilbv
    implicit none
    integer(4), intent(out) :: f90wrap_ilbv
    
    f90wrap_ilbv = chem_ilbv
end subroutine f90wrap_chem__get__ilbv

subroutine f90wrap_chem__set__ilbv(f90wrap_ilbv)
    use chem, only: chem_ilbv => ilbv
    implicit none
    integer(4), intent(in) :: f90wrap_ilbv
    
    chem_ilbv = f90wrap_ilbv
end subroutine f90wrap_chem__set__ilbv

subroutine f90wrap_chem__get__ilbx(f90wrap_ilbx)
    use chem, only: chem_ilbx => ilbx
    implicit none
    integer(4), intent(out) :: f90wrap_ilbx
    
    f90wrap_ilbx = chem_ilbx
end subroutine f90wrap_chem__get__ilbx

subroutine f90wrap_chem__set__ilbx(f90wrap_ilbx)
    use chem, only: chem_ilbx => ilbx
    implicit none
    integer(4), intent(in) :: f90wrap_ilbx
    
    chem_ilbx = f90wrap_ilbx
end subroutine f90wrap_chem__set__ilbx

subroutine f90wrap_chem__get__lb_output(f90wrap_lb_output)
    use chem, only: chem_lb_output => lb_output
    implicit none
    logical, intent(out) :: f90wrap_lb_output
    
    f90wrap_lb_output = chem_lb_output
end subroutine f90wrap_chem__get__lb_output

subroutine f90wrap_chem__set__lb_output(f90wrap_lb_output)
    use chem, only: chem_lb_output => lb_output
    implicit none
    logical, intent(in) :: f90wrap_lb_output
    
    chem_lb_output = f90wrap_lb_output
end subroutine f90wrap_chem__set__lb_output

subroutine f90wrap_chem__get__pe_output(f90wrap_pe_output)
    use chem, only: chem_pe_output => pe_output
    implicit none
    logical, intent(out) :: f90wrap_pe_output
    
    f90wrap_pe_output = chem_pe_output
end subroutine f90wrap_chem__get__pe_output

subroutine f90wrap_chem__set__pe_output(f90wrap_pe_output)
    use chem, only: chem_pe_output => pe_output
    implicit none
    logical, intent(in) :: f90wrap_pe_output
    
    chem_pe_output = f90wrap_pe_output
end subroutine f90wrap_chem__set__pe_output

subroutine f90wrap_chem__get__ph_output(f90wrap_ph_output)
    use chem, only: chem_ph_output => ph_output
    implicit none
    logical, intent(out) :: f90wrap_ph_output
    
    f90wrap_ph_output = chem_ph_output
end subroutine f90wrap_chem__get__ph_output

subroutine f90wrap_chem__set__ph_output(f90wrap_ph_output)
    use chem, only: chem_ph_output => ph_output
    implicit none
    logical, intent(in) :: f90wrap_ph_output
    
    chem_ph_output = f90wrap_ph_output
end subroutine f90wrap_chem__set__ph_output

subroutine f90wrap_chem__array__actv(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_actv => actv
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_actv)) then
        dshape(1:1) = shape(chem_actv)
        dloc = loc(chem_actv)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__actv

subroutine f90wrap_chem__array__alkfacc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_alkfacc => alkfacc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_alkfacc)) then
        dshape(1:1) = shape(chem_alkfacc)
        dloc = loc(chem_alkfacc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__alkfacc

subroutine f90wrap_chem__array__alkfacx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_alkfacx => alkfacx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_alkfacx)) then
        dshape(1:1) = shape(chem_alkfacx)
        dloc = loc(chem_alkfacx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__alkfacx

subroutine f90wrap_chem__array__totcinit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcinit => totcinit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcinit)) then
        dshape(1:1) = shape(chem_totcinit)
        dloc = loc(chem_totcinit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcinit

subroutine f90wrap_chem__array__totcn(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcn => totcn
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcn)) then
        dshape(1:1) = shape(chem_totcn)
        dloc = loc(chem_totcn)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcn

subroutine f90wrap_chem__array__totcmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcmin => totcmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcmin)) then
        dshape(1:1) = shape(chem_totcmin)
        dloc = loc(chem_totcmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcmin

subroutine f90wrap_chem__array__totco(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totco => totco
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totco)) then
        dshape(1:1) = shape(chem_totco)
        dloc = loc(chem_totco)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totco

subroutine f90wrap_chem__array__ccnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ccnew => ccnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ccnew)) then
        dshape(1:1) = shape(chem_ccnew)
        dloc = loc(chem_ccnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ccnew

subroutine f90wrap_chem__array__ccold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ccold => ccold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ccold)) then
        dshape(1:1) = shape(chem_ccold)
        dloc = loc(chem_ccold)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ccold

subroutine f90wrap_chem__array__gamma_l(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gamma_l => gamma_l
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gamma_l)) then
        dshape(1:1) = shape(chem_gamma_l)
        dloc = loc(chem_gamma_l)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gamma_l

subroutine f90wrap_chem__array__chargec(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chargec => chargec
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chargec)) then
        dshape(1:1) = shape(chem_chargec)
        dloc = loc(chem_chargec)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chargec

subroutine f90wrap_chem__array__gfwc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwc => gfwc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwc)) then
        dshape(1:1) = shape(chem_gfwc)
        dloc = loc(chem_gfwc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwc

subroutine f90wrap_chem__array__distcoff_lc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_distcoff_lc => distcoff_lc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_distcoff_lc)) then
        dshape(1:1) = shape(chem_distcoff_lc)
        dloc = loc(chem_distcoff_lc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__distcoff_lc

subroutine f90wrap_chem__array__nfr(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_nfr => nfr
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_nfr)) then
        dshape(1:1) = shape(chem_nfr)
        dloc = loc(chem_nfr)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__nfr

subroutine f90wrap_chem__array__lang(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_lang => lang
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_lang)) then
        dshape(1:1) = shape(chem_lang)
        dloc = loc(chem_lang)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__lang

subroutine f90wrap_chem__array__pdm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_pdm => pdm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_pdm)) then
        dshape(1:1) = shape(chem_pdm)
        dloc = loc(chem_pdm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__pdm

subroutine f90wrap_chem__array__dhac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhac => dhac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhac)) then
        dshape(1:1) = shape(chem_dhac)
        dloc = loc(chem_dhac)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhac

subroutine f90wrap_chem__array__dhbc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhbc => dhbc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhbc)) then
        dshape(1:1) = shape(chem_dhbc)
        dloc = loc(chem_dhbc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhbc

subroutine f90wrap_chem__array__cxc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cxc => cxc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cxc)) then
        dshape(1:1) = shape(chem_cxc)
        dloc = loc(chem_cxc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cxc

subroutine f90wrap_chem__array__cxmax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cxmax => cxmax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cxmax)) then
        dshape(1:1) = shape(chem_cxmax)
        dloc = loc(chem_cxmax)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cxmax

subroutine f90wrap_chem__array__chargex(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chargex => chargex
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chargex)) then
        dshape(1:1) = shape(chem_chargex)
        dloc = loc(chem_chargex)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chargex

subroutine f90wrap_chem__array__eqx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqx => eqx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqx)) then
        dshape(1:1) = shape(chem_eqx)
        dloc = loc(chem_eqx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqx

subroutine f90wrap_chem__array__eqxs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqxs => eqxs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqxs)) then
        dshape(1:1) = shape(chem_eqxs)
        dloc = loc(chem_eqxs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqxs

subroutine f90wrap_chem__array__gfwx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwx => gfwx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwx)) then
        dshape(1:1) = shape(chem_gfwx)
        dloc = loc(chem_gfwx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwx

subroutine f90wrap_chem__array__dhcx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcx => dhcx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcx)) then
        dshape(1:1) = shape(chem_dhcx)
        dloc = loc(chem_dhcx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcx

subroutine f90wrap_chem__array__dhax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhax => dhax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhax)) then
        dshape(1:1) = shape(chem_dhax)
        dloc = loc(chem_dhax)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhax

subroutine f90wrap_chem__array__dhbx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhbx => dhbx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhbx)) then
        dshape(1:1) = shape(chem_dhbx)
        dloc = loc(chem_dhbx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhbx

subroutine f90wrap_chem__array__xnux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnux => xnux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnux)) then
        dshape(1:1) = shape(chem_xnux)
        dloc = loc(chem_xnux)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnux

subroutine f90wrap_chem__get__sion1(f90wrap_sion1)
    use chem, only: chem_sion1 => sion1
    implicit none
    real(8), intent(out) :: f90wrap_sion1
    
    f90wrap_sion1 = chem_sion1
end subroutine f90wrap_chem__get__sion1

subroutine f90wrap_chem__set__sion1(f90wrap_sion1)
    use chem, only: chem_sion1 => sion1
    implicit none
    real(8), intent(in) :: f90wrap_sion1
    
    chem_sion1 = f90wrap_sion1
end subroutine f90wrap_chem__set__sion1

subroutine f90wrap_chem__get__phguess(f90wrap_phguess)
    use chem, only: chem_phguess => phguess
    implicit none
    real(8), intent(out) :: f90wrap_phguess
    
    f90wrap_phguess = chem_phguess
end subroutine f90wrap_chem__get__phguess

subroutine f90wrap_chem__set__phguess(f90wrap_phguess)
    use chem, only: chem_phguess => phguess
    implicit none
    real(8), intent(in) :: f90wrap_phguess
    
    chem_phguess = f90wrap_phguess
end subroutine f90wrap_chem__set__phguess

subroutine f90wrap_chem__array__iax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iax => iax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iax)) then
        dshape(1:1) = shape(chem_iax)
        dloc = loc(chem_iax)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iax

subroutine f90wrap_chem__array__jax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jax => jax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jax)) then
        dshape(1:1) = shape(chem_jax)
        dloc = loc(chem_jax)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jax

subroutine f90wrap_chem__array__l_namec(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namec => l_namec
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namec)) then
        dshape(1:1) = shape(chem_l_namec)
        dloc = loc(chem_l_namec)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namec

subroutine f90wrap_chem__array__l_namex(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namex => l_namex
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namex)) then
        dshape(1:1) = shape(chem_l_namex)
        dloc = loc(chem_l_namex)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namex

subroutine f90wrap_chem__array__cequil_kin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cequil_kin => cequil_kin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cequil_kin)) then
        dshape(1:1) = shape(chem_cequil_kin)
        dloc = loc(chem_cequil_kin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cequil_kin

subroutine f90wrap_chem__array__clang_kin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_clang_kin => clang_kin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_clang_kin)) then
        dshape(1:1) = shape(chem_clang_kin)
        dloc = loc(chem_clang_kin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__clang_kin

subroutine f90wrap_chem__array__smax_kin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_smax_kin => smax_kin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_smax_kin)) then
        dshape(1:1) = shape(chem_smax_kin)
        dloc = loc(chem_smax_kin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__smax_kin

subroutine f90wrap_chem__array__cfreund_kin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cfreund_kin => cfreund_kin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cfreund_kin)) then
        dshape(1:1) = shape(chem_cfreund_kin)
        dloc = loc(chem_cfreund_kin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cfreund_kin

subroutine f90wrap_chem__array__exponfreund_kin(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use chem, only: chem_exponfreund_kin => exponfreund_kin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_exponfreund_kin)) then
        dshape(1:1) = shape(chem_exponfreund_kin)
        dloc = loc(chem_exponfreund_kin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__exponfreund_kin

subroutine f90wrap_chem__array__eqaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqaq => eqaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqaq)) then
        dshape(1:1) = shape(chem_eqaq)
        dloc = loc(chem_eqaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqaq

subroutine f90wrap_chem__array__eqaqs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqaqs => eqaqs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqaqs)) then
        dshape(1:1) = shape(chem_eqaqs)
        dloc = loc(chem_eqaqs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqaqs

subroutine f90wrap_chem__array__dgaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dgaq => dgaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dgaq)) then
        dshape(1:1) = shape(chem_dgaq)
        dloc = loc(chem_dgaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dgaq

subroutine f90wrap_chem__array__dhaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhaq => dhaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhaq)) then
        dshape(1:1) = shape(chem_dhaq)
        dloc = loc(chem_dhaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhaq

subroutine f90wrap_chem__array__dtotaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotaq => dtotaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotaq)) then
        dshape(1:1) = shape(chem_dtotaq)
        dloc = loc(chem_dtotaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotaq

subroutine f90wrap_chem__array__faqhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqhc => faqhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqhc)) then
        dshape(1:1) = shape(chem_faqhc)
        dloc = loc(chem_faqhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqhc

subroutine f90wrap_chem__array__faqht(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqht => faqht
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqht)) then
        dshape(1:1) = shape(chem_faqht)
        dloc = loc(chem_faqht)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqht

subroutine f90wrap_chem__array__faqhm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqhm => faqhm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqhm)) then
        dshape(1:1) = shape(chem_faqhm)
        dloc = loc(chem_faqhm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqhm

subroutine f90wrap_chem__array__faqi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqi => faqi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqi)) then
        dshape(1:1) = shape(chem_faqi)
        dloc = loc(chem_faqi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqi

subroutine f90wrap_chem__array__faqic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqic => faqic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqic)) then
        dshape(1:1) = shape(chem_faqic)
        dloc = loc(chem_faqic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqic

subroutine f90wrap_chem__array__faqit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqit => faqit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqit)) then
        dshape(1:1) = shape(chem_faqit)
        dloc = loc(chem_faqit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqit

subroutine f90wrap_chem__array__faqim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_faqim => faqim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_faqim)) then
        dshape(1:1) = shape(chem_faqim)
        dloc = loc(chem_faqim)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__faqim

subroutine f90wrap_chem__array__ordaqic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqic => ordaqic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqic)) then
        dshape(1:1) = shape(chem_ordaqic)
        dloc = loc(chem_ordaqic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqic

subroutine f90wrap_chem__array__ordaqit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqit => ordaqit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqit)) then
        dshape(1:1) = shape(chem_ordaqit)
        dloc = loc(chem_ordaqit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqit

subroutine f90wrap_chem__array__ordaqim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqim => ordaqim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqim)) then
        dshape(1:1) = shape(chem_ordaqim)
        dloc = loc(chem_ordaqim)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqim

subroutine f90wrap_chem__array__ordaqhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqhc => ordaqhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqhc)) then
        dshape(1:1) = shape(chem_ordaqhc)
        dloc = loc(chem_ordaqhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqhc

subroutine f90wrap_chem__array__ordaqht(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqht => ordaqht
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqht)) then
        dshape(1:1) = shape(chem_ordaqht)
        dloc = loc(chem_ordaqht)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqht

subroutine f90wrap_chem__array__ordaqhm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqhm => ordaqhm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqhm)) then
        dshape(1:1) = shape(chem_ordaqhm)
        dloc = loc(chem_ordaqhm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqhm

subroutine f90wrap_chem__array__ordaqt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqt => ordaqt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqt)) then
        dshape(1:1) = shape(chem_ordaqt)
        dloc = loc(chem_ordaqt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqt

subroutine f90wrap_chem__array__ordaqc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqc => ordaqc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqc)) then
        dshape(1:1) = shape(chem_ordaqc)
        dloc = loc(chem_ordaqc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqc

subroutine f90wrap_chem__array__ordaqx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqx => ordaqx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqx)) then
        dshape(1:1) = shape(chem_ordaqx)
        dloc = loc(chem_ordaqx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqx

subroutine f90wrap_chem__array__ordaqm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordaqm => ordaqm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordaqm)) then
        dshape(1:1) = shape(chem_ordaqm)
        dloc = loc(chem_ordaqm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordaqm

subroutine f90wrap_chem__array__rateaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rateaq => rateaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rateaq)) then
        dshape(1:1) = shape(chem_rateaq)
        dloc = loc(chem_rateaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rateaq

subroutine f90wrap_chem__array__ratecaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ratecaq => ratecaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ratecaq)) then
        dshape(1:1) = shape(chem_ratecaq)
        dloc = loc(chem_ratecaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ratecaq

subroutine f90wrap_chem__array__ratecaqs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ratecaqs => ratecaqs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ratecaqs)) then
        dshape(1:1) = shape(chem_ratecaqs)
        dloc = loc(chem_ratecaqs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ratecaqs

subroutine f90wrap_chem__array__sataq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_sataq => sataq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_sataq)) then
        dshape(1:1) = shape(chem_sataq)
        dloc = loc(chem_sataq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__sataq

subroutine f90wrap_chem__array__scalfac_aq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_scalfac_aq => scalfac_aq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_scalfac_aq)) then
        dshape(1:1) = shape(chem_scalfac_aq)
        dloc = loc(chem_scalfac_aq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__scalfac_aq

subroutine f90wrap_chem__array__totaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totaq => totaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totaq)) then
        dshape(1:1) = shape(chem_totaq)
        dloc = loc(chem_totaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totaq

subroutine f90wrap_chem__array__xnuaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnuaq => xnuaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnuaq)) then
        dshape(1:1) = shape(chem_xnuaq)
        dloc = loc(chem_xnuaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnuaq

subroutine f90wrap_chem__array__iaaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaq => iaaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaq)) then
        dshape(1:1) = shape(chem_iaaq)
        dloc = loc(chem_iaaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaq

subroutine f90wrap_chem__array__iaaqi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqi => iaaqi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqi)) then
        dshape(1:1) = shape(chem_iaaqi)
        dloc = loc(chem_iaaqi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqi

subroutine f90wrap_chem__array__iaaqic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqic => iaaqic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqic)) then
        dshape(1:1) = shape(chem_iaaqic)
        dloc = loc(chem_iaaqic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqic

subroutine f90wrap_chem__array__iaaqit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqit => iaaqit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqit)) then
        dshape(1:1) = shape(chem_iaaqit)
        dloc = loc(chem_iaaqit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqit

subroutine f90wrap_chem__array__iaaqim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqim => iaaqim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqim)) then
        dshape(1:1) = shape(chem_iaaqim)
        dloc = loc(chem_iaaqim)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqim

subroutine f90wrap_chem__array__iaaqhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqhc => iaaqhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqhc)) then
        dshape(1:1) = shape(chem_iaaqhc)
        dloc = loc(chem_iaaqhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqhc

subroutine f90wrap_chem__array__iaaqht(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqht => iaaqht
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqht)) then
        dshape(1:1) = shape(chem_iaaqht)
        dloc = loc(chem_iaaqht)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqht

subroutine f90wrap_chem__array__iaaqhm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqhm => iaaqhm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqhm)) then
        dshape(1:1) = shape(chem_iaaqhm)
        dloc = loc(chem_iaaqhm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqhm

subroutine f90wrap_chem__array__iaaqt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqt => iaaqt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqt)) then
        dshape(1:1) = shape(chem_iaaqt)
        dloc = loc(chem_iaaqt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqt

subroutine f90wrap_chem__array__iaequil(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaequil => iaequil
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaequil)) then
        dshape(1:1) = shape(chem_iaequil)
        dloc = loc(chem_iaequil)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaequil

subroutine f90wrap_chem__array__iaaqc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqc => iaaqc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqc)) then
        dshape(1:1) = shape(chem_iaaqc)
        dloc = loc(chem_iaaqc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqc

subroutine f90wrap_chem__array__iaaqx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqx => iaaqx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqx)) then
        dshape(1:1) = shape(chem_iaaqx)
        dloc = loc(chem_iaaqx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqx

subroutine f90wrap_chem__array__iaaqm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaaqm => iaaqm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaaqm)) then
        dshape(1:1) = shape(chem_iaaqm)
        dloc = loc(chem_iaaqm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaaqm

subroutine f90wrap_chem__array__jaaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaq => jaaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaq)) then
        dshape(1:1) = shape(chem_jaaq)
        dloc = loc(chem_jaaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaq

subroutine f90wrap_chem__array__jaaqt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqt => jaaqt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqt)) then
        dshape(1:1) = shape(chem_jaaqt)
        dloc = loc(chem_jaaqt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqt

subroutine f90wrap_chem__array__jaequil(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaequil => jaequil
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaequil)) then
        dshape(1:1) = shape(chem_jaequil)
        dloc = loc(chem_jaequil)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaequil

subroutine f90wrap_chem__array__jaaqc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqc => jaaqc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqc)) then
        dshape(1:1) = shape(chem_jaaqc)
        dloc = loc(chem_jaaqc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqc

subroutine f90wrap_chem__array__jaaqx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqx => jaaqx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqx)) then
        dshape(1:1) = shape(chem_jaaqx)
        dloc = loc(chem_jaaqx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqx

subroutine f90wrap_chem__array__jaaqm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqm => jaaqm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqm)) then
        dshape(1:1) = shape(chem_jaaqm)
        dloc = loc(chem_jaaqm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqm

subroutine f90wrap_chem__array__jaaqhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqhc => jaaqhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqhc)) then
        dshape(1:1) = shape(chem_jaaqhc)
        dloc = loc(chem_jaaqhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqhc

subroutine f90wrap_chem__array__jaaqht(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqht => jaaqht
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqht)) then
        dshape(1:1) = shape(chem_jaaqht)
        dloc = loc(chem_jaaqht)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqht

subroutine f90wrap_chem__array__jaaqhm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqhm => jaaqhm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqhm)) then
        dshape(1:1) = shape(chem_jaaqhm)
        dloc = loc(chem_jaaqhm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqhm

subroutine f90wrap_chem__array__jaaqi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqi => jaaqi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqi)) then
        dshape(1:1) = shape(chem_jaaqi)
        dloc = loc(chem_jaaqi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqi

subroutine f90wrap_chem__array__jaaqic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqic => jaaqic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqic)) then
        dshape(1:1) = shape(chem_jaaqic)
        dloc = loc(chem_jaaqic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqic

subroutine f90wrap_chem__array__jaaqit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqit => jaaqit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqit)) then
        dshape(1:1) = shape(chem_jaaqit)
        dloc = loc(chem_jaaqit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqit

subroutine f90wrap_chem__array__jaaqim(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaaqim => jaaqim
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaaqim)) then
        dshape(1:1) = shape(chem_jaaqim)
        dloc = loc(chem_jaaqim)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaaqim

subroutine f90wrap_chem__array__l_nameaq(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_nameaq => l_nameaq
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_nameaq)) then
        dshape(1:1) = shape(chem_l_nameaq)
        dloc = loc(chem_l_nameaq)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_nameaq

subroutine f90wrap_chem__get__ratio(f90wrap_ratio)
    use chem, only: chem_ratio => ratio
    implicit none
    real(8), intent(out) :: f90wrap_ratio
    
    f90wrap_ratio = chem_ratio
end subroutine f90wrap_chem__get__ratio

subroutine f90wrap_chem__set__ratio(f90wrap_ratio)
    use chem, only: chem_ratio => ratio
    implicit none
    real(8), intent(in) :: f90wrap_ratio
    
    chem_ratio = f90wrap_ratio
end subroutine f90wrap_chem__set__ratio

subroutine f90wrap_chem__get__delt_bck(f90wrap_delt_bck)
    use chem, only: chem_delt_bck => delt_bck
    implicit none
    real(8), intent(out) :: f90wrap_delt_bck
    
    f90wrap_delt_bck = chem_delt_bck
end subroutine f90wrap_chem__get__delt_bck

subroutine f90wrap_chem__set__delt_bck(f90wrap_delt_bck)
    use chem, only: chem_delt_bck => delt_bck
    implicit none
    real(8), intent(in) :: f90wrap_delt_bck
    
    chem_delt_bck = f90wrap_delt_bck
end subroutine f90wrap_chem__set__delt_bck

subroutine f90wrap_chem__get__ratio_init(f90wrap_ratio_init)
    use chem, only: chem_ratio_init => ratio_init
    implicit none
    real(8), intent(out) :: f90wrap_ratio_init
    
    f90wrap_ratio_init = chem_ratio_init
end subroutine f90wrap_chem__get__ratio_init

subroutine f90wrap_chem__set__ratio_init(f90wrap_ratio_init)
    use chem, only: chem_ratio_init => ratio_init
    implicit none
    real(8), intent(in) :: f90wrap_ratio_init
    
    chem_ratio_init = f90wrap_ratio_init
end subroutine f90wrap_chem__set__ratio_init

subroutine f90wrap_chem__get__ratio_bck(f90wrap_ratio_bck)
    use chem, only: chem_ratio_bck => ratio_bck
    implicit none
    real(8), intent(out) :: f90wrap_ratio_bck
    
    f90wrap_ratio_bck = chem_ratio_bck
end subroutine f90wrap_chem__get__ratio_bck

subroutine f90wrap_chem__set__ratio_bck(f90wrap_ratio_bck)
    use chem, only: chem_ratio_bck => ratio_bck
    implicit none
    real(8), intent(in) :: f90wrap_ratio_bck
    
    chem_ratio_bck = f90wrap_ratio_bck
end subroutine f90wrap_chem__set__ratio_bck

subroutine f90wrap_chem__get__sfr(f90wrap_sfr)
    use chem, only: chem_sfr => sfr
    implicit none
    real(8), intent(out) :: f90wrap_sfr
    
    f90wrap_sfr = chem_sfr
end subroutine f90wrap_chem__get__sfr

subroutine f90wrap_chem__set__sfr(f90wrap_sfr)
    use chem, only: chem_sfr => sfr
    implicit none
    real(8), intent(in) :: f90wrap_sfr
    
    chem_sfr = f90wrap_sfr
end subroutine f90wrap_chem__set__sfr

subroutine f90wrap_chem__get__ratedemand_corr(f90wrap_ratedemand_corr)
    use chem, only: chem_ratedemand_corr => ratedemand_corr
    implicit none
    real(8), intent(out) :: f90wrap_ratedemand_corr
    
    f90wrap_ratedemand_corr = chem_ratedemand_corr
end subroutine f90wrap_chem__get__ratedemand_corr

subroutine f90wrap_chem__set__ratedemand_corr(f90wrap_ratedemand_corr)
    use chem, only: chem_ratedemand_corr => ratedemand_corr
    implicit none
    real(8), intent(in) :: f90wrap_ratedemand_corr
    
    chem_ratedemand_corr = f90wrap_ratedemand_corr
end subroutine f90wrap_chem__set__ratedemand_corr

subroutine &
    f90wrap_chem__get__cumul_totactiveuptake_mass(f90wrap_cumul_totactiveuptake_mass)
    use chem, only: chem_cumul_totactiveuptake_mass => cumul_totactiveuptake_mass
    implicit none
    real(8), intent(out) :: f90wrap_cumul_totactiveuptake_mass
    
    f90wrap_cumul_totactiveuptake_mass = chem_cumul_totactiveuptake_mass
end subroutine f90wrap_chem__get__cumul_totactiveuptake_mass

subroutine &
    f90wrap_chem__set__cumul_totactiveuptake_mass(f90wrap_cumul_totactiveuptake_mass)
    use chem, only: chem_cumul_totactiveuptake_mass => cumul_totactiveuptake_mass
    implicit none
    real(8), intent(in) :: f90wrap_cumul_totactiveuptake_mass
    
    chem_cumul_totactiveuptake_mass = f90wrap_cumul_totactiveuptake_mass
end subroutine f90wrap_chem__set__cumul_totactiveuptake_mass

subroutine &
    f90wrap_chem__get__cumul_totactiveuptake_mass_2(f90wrap_cumul_totactiveuptake_mass_2)
    use chem, only: chem_cumul_totactiveuptake_mass_2 => &
        cumul_totactiveuptake_mass_2
    implicit none
    real(8), intent(out) :: f90wrap_cumul_totactiveuptake_mass_2
    
    f90wrap_cumul_totactiveuptake_mass_2 = chem_cumul_totactiveuptake_mass_2
end subroutine f90wrap_chem__get__cumul_totactiveuptake_mass_2

subroutine &
    f90wrap_chem__set__cumul_totactiveuptake_mass_2(f90wrap_cumul_totactiveuptake_mass_2)
    use chem, only: chem_cumul_totactiveuptake_mass_2 => &
        cumul_totactiveuptake_mass_2
    implicit none
    real(8), intent(in) :: f90wrap_cumul_totactiveuptake_mass_2
    
    chem_cumul_totactiveuptake_mass_2 = f90wrap_cumul_totactiveuptake_mass_2
end subroutine f90wrap_chem__set__cumul_totactiveuptake_mass_2

subroutine f90wrap_chem__get__nutdemand(f90wrap_nutdemand)
    use chem, only: chem_nutdemand => nutdemand
    implicit none
    logical, intent(out) :: f90wrap_nutdemand
    
    f90wrap_nutdemand = chem_nutdemand
end subroutine f90wrap_chem__get__nutdemand

subroutine f90wrap_chem__set__nutdemand(f90wrap_nutdemand)
    use chem, only: chem_nutdemand => nutdemand
    implicit none
    logical, intent(in) :: f90wrap_nutdemand
    
    chem_nutdemand = f90wrap_nutdemand
end subroutine f90wrap_chem__set__nutdemand

subroutine f90wrap_chem__get__nutdemand_opt(f90wrap_nutdemand_opt)
    use chem, only: chem_nutdemand_opt => nutdemand_opt
    implicit none
    logical, intent(out) :: f90wrap_nutdemand_opt
    
    f90wrap_nutdemand_opt = chem_nutdemand_opt
end subroutine f90wrap_chem__get__nutdemand_opt

subroutine f90wrap_chem__set__nutdemand_opt(f90wrap_nutdemand_opt)
    use chem, only: chem_nutdemand_opt => nutdemand_opt
    implicit none
    logical, intent(in) :: f90wrap_nutdemand_opt
    
    chem_nutdemand_opt = f90wrap_nutdemand_opt
end subroutine f90wrap_chem__set__nutdemand_opt

subroutine f90wrap_chem__get__nutdemand_gen(f90wrap_nutdemand_gen)
    use chem, only: chem_nutdemand_gen => nutdemand_gen
    implicit none
    logical, intent(out) :: f90wrap_nutdemand_gen
    
    f90wrap_nutdemand_gen = chem_nutdemand_gen
end subroutine f90wrap_chem__get__nutdemand_gen

subroutine f90wrap_chem__set__nutdemand_gen(f90wrap_nutdemand_gen)
    use chem, only: chem_nutdemand_gen => nutdemand_gen
    implicit none
    logical, intent(in) :: f90wrap_nutdemand_gen
    
    chem_nutdemand_gen = f90wrap_nutdemand_gen
end subroutine f90wrap_chem__set__nutdemand_gen

subroutine f90wrap_chem__get__optimization_failed(f90wrap_optimization_failed)
    use chem, only: chem_optimization_failed => optimization_failed
    implicit none
    logical, intent(out) :: f90wrap_optimization_failed
    
    f90wrap_optimization_failed = chem_optimization_failed
end subroutine f90wrap_chem__get__optimization_failed

subroutine f90wrap_chem__set__optimization_failed(f90wrap_optimization_failed)
    use chem, only: chem_optimization_failed => optimization_failed
    implicit none
    logical, intent(in) :: f90wrap_optimization_failed
    
    chem_optimization_failed = f90wrap_optimization_failed
end subroutine f90wrap_chem__set__optimization_failed

subroutine f90wrap_chem__get__icountnutuptake(f90wrap_icountnutuptake)
    use chem, only: chem_icountnutuptake => icountnutuptake
    implicit none
    integer(4), intent(out) :: f90wrap_icountnutuptake
    
    f90wrap_icountnutuptake = chem_icountnutuptake
end subroutine f90wrap_chem__get__icountnutuptake

subroutine f90wrap_chem__set__icountnutuptake(f90wrap_icountnutuptake)
    use chem, only: chem_icountnutuptake => icountnutuptake
    implicit none
    integer(4), intent(in) :: f90wrap_icountnutuptake
    
    chem_icountnutuptake = f90wrap_icountnutuptake
end subroutine f90wrap_chem__set__icountnutuptake

subroutine f90wrap_chem__get__iopt_nutuptake(f90wrap_iopt_nutuptake)
    use chem, only: chem_iopt_nutuptake => iopt_nutuptake
    implicit none
    integer(4), intent(out) :: f90wrap_iopt_nutuptake
    
    f90wrap_iopt_nutuptake = chem_iopt_nutuptake
end subroutine f90wrap_chem__get__iopt_nutuptake

subroutine f90wrap_chem__set__iopt_nutuptake(f90wrap_iopt_nutuptake)
    use chem, only: chem_iopt_nutuptake => iopt_nutuptake
    implicit none
    integer(4), intent(in) :: f90wrap_iopt_nutuptake
    
    chem_iopt_nutuptake = f90wrap_iopt_nutuptake
end subroutine f90wrap_chem__set__iopt_nutuptake

subroutine f90wrap_chem__array__bcatfac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_bcatfac => bcatfac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_bcatfac)) then
        dshape(1:1) = shape(chem_bcatfac)
        dloc = loc(chem_bcatfac)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__bcatfac

subroutine f90wrap_chem__array__dhcr(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcr => dhcr
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcr)) then
        dshape(1:1) = shape(chem_dhcr)
        dloc = loc(chem_dhcr)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcr

subroutine f90wrap_chem__array__dtotor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotor => dtotor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotor)) then
        dshape(1:1) = shape(chem_dtotor)
        dloc = loc(chem_dtotor)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotor

subroutine f90wrap_chem__array__eqr(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqr => eqr
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqr)) then
        dshape(1:1) = shape(chem_eqr)
        dloc = loc(chem_eqr)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqr

subroutine f90wrap_chem__array__eqrs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqrs => eqrs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqrs)) then
        dshape(1:1) = shape(chem_eqrs)
        dloc = loc(chem_eqrs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqrs

subroutine f90wrap_chem__array__chomc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chomc => chomc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chomc)) then
        dshape(1:1) = shape(chem_chomc)
        dloc = loc(chem_chomc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chomc

subroutine f90wrap_chem__array__chomt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chomt => chomt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chomt)) then
        dshape(1:1) = shape(chem_chomt)
        dloc = loc(chem_chomt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chomt

subroutine f90wrap_chem__array__chomx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chomx => chomx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chomx)) then
        dshape(1:1) = shape(chem_chomx)
        dloc = loc(chem_chomx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chomx

subroutine f90wrap_chem__array__ordorc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordorc => ordorc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordorc)) then
        dshape(1:1) = shape(chem_ordorc)
        dloc = loc(chem_ordorc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordorc

subroutine f90wrap_chem__array__ordort(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordort => ordort
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordort)) then
        dshape(1:1) = shape(chem_ordort)
        dloc = loc(chem_ordort)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordort

subroutine f90wrap_chem__array__ordorx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordorx => ordorx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordorx)) then
        dshape(1:1) = shape(chem_ordorx)
        dloc = loc(chem_ordorx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordorx

subroutine f90wrap_chem__array__rateor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rateor => rateor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rateor)) then
        dshape(1:1) = shape(chem_rateor)
        dloc = loc(chem_rateor)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rateor

subroutine f90wrap_chem__array__rateox(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rateox => rateox
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rateox)) then
        dshape(1:1) = shape(chem_rateox)
        dloc = loc(chem_rateox)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rateox

subroutine f90wrap_chem__array__totor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totor => totor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totor)) then
        dshape(1:1) = shape(chem_totor)
        dloc = loc(chem_totor)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totor

subroutine f90wrap_chem__array__xnur(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnur => xnur
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnur)) then
        dshape(1:1) = shape(chem_xnur)
        dloc = loc(chem_xnur)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnur

subroutine f90wrap_chem__array__iaor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaor => iaor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaor)) then
        dshape(1:1) = shape(chem_iaor)
        dloc = loc(chem_iaor)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaor

subroutine f90wrap_chem__array__iaorc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaorc => iaorc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaorc)) then
        dshape(1:1) = shape(chem_iaorc)
        dloc = loc(chem_iaorc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaorc

subroutine f90wrap_chem__array__iaort(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaort => iaort
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaort)) then
        dshape(1:1) = shape(chem_iaort)
        dloc = loc(chem_iaort)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaort

subroutine f90wrap_chem__array__iaorx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaorx => iaorx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaorx)) then
        dshape(1:1) = shape(chem_iaorx)
        dloc = loc(chem_iaorx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaorx

subroutine f90wrap_chem__array__iarc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iarc => iarc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iarc)) then
        dshape(1:1) = shape(chem_iarc)
        dloc = loc(chem_iarc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iarc

subroutine f90wrap_chem__array__iars(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iars => iars
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iars)) then
        dshape(1:1) = shape(chem_iars)
        dloc = loc(chem_iars)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iars

subroutine f90wrap_chem__array__jaorc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaorc => jaorc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaorc)) then
        dshape(1:1) = shape(chem_jaorc)
        dloc = loc(chem_jaorc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaorc

subroutine f90wrap_chem__array__jaort(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaort => jaort
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaort)) then
        dshape(1:1) = shape(chem_jaort)
        dloc = loc(chem_jaort)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaort

subroutine f90wrap_chem__array__jaorx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaorx => jaorx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaorx)) then
        dshape(1:1) = shape(chem_jaorx)
        dloc = loc(chem_jaorx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaorx

subroutine f90wrap_chem__array__jarc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jarc => jarc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jarc)) then
        dshape(1:1) = shape(chem_jarc)
        dloc = loc(chem_jarc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jarc

subroutine f90wrap_chem__array__l_namer(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namer => l_namer
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namer)) then
        dshape(1:1) = shape(chem_l_namer)
        dloc = loc(chem_l_namer)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namer

subroutine f90wrap_chem__array__l_namerp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namerp => l_namerp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namerp)) then
        dshape(1:1) = shape(chem_l_namerp)
        dloc = loc(chem_l_namerp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namerp

subroutine f90wrap_chem__array__l_namers(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namers => l_namers
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namers)) then
        dshape(1:1) = shape(chem_l_namers)
        dloc = loc(chem_l_namers)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namers

subroutine f90wrap_chem__get__ncrc(f90wrap_ncrc)
    use chem, only: chem_ncrc => ncrc
    implicit none
    integer(4), intent(out) :: f90wrap_ncrc
    
    f90wrap_ncrc = chem_ncrc
end subroutine f90wrap_chem__get__ncrc

subroutine f90wrap_chem__set__ncrc(f90wrap_ncrc)
    use chem, only: chem_ncrc => ncrc
    implicit none
    integer(4), intent(in) :: f90wrap_ncrc
    
    chem_ncrc = f90wrap_ncrc
end subroutine f90wrap_chem__set__ncrc

subroutine f90wrap_chem__get__nor(f90wrap_nor)
    use chem, only: chem_nor => nor
    implicit none
    integer(4), intent(out) :: f90wrap_nor
    
    f90wrap_nor = chem_nor
end subroutine f90wrap_chem__get__nor

subroutine f90wrap_chem__set__nor(f90wrap_nor)
    use chem, only: chem_nor => nor
    implicit none
    integer(4), intent(in) :: f90wrap_nor
    
    chem_nor = f90wrap_nor
end subroutine f90wrap_chem__set__nor

subroutine f90wrap_chem__get__norc(f90wrap_norc)
    use chem, only: chem_norc => norc
    implicit none
    integer(4), intent(out) :: f90wrap_norc
    
    f90wrap_norc = chem_norc
end subroutine f90wrap_chem__get__norc

subroutine f90wrap_chem__set__norc(f90wrap_norc)
    use chem, only: chem_norc => norc
    implicit none
    integer(4), intent(in) :: f90wrap_norc
    
    chem_norc = f90wrap_norc
end subroutine f90wrap_chem__set__norc

subroutine f90wrap_chem__get__nort(f90wrap_nort)
    use chem, only: chem_nort => nort
    implicit none
    integer(4), intent(out) :: f90wrap_nort
    
    f90wrap_nort = chem_nort
end subroutine f90wrap_chem__get__nort

subroutine f90wrap_chem__set__nort(f90wrap_nort)
    use chem, only: chem_nort => nort
    implicit none
    integer(4), intent(in) :: f90wrap_nort
    
    chem_nort = f90wrap_nort
end subroutine f90wrap_chem__set__nort

subroutine f90wrap_chem__get__norx(f90wrap_norx)
    use chem, only: chem_norx => norx
    implicit none
    integer(4), intent(out) :: f90wrap_norx
    
    f90wrap_norx = chem_norx
end subroutine f90wrap_chem__get__norx

subroutine f90wrap_chem__set__norx(f90wrap_norx)
    use chem, only: chem_norx => norx
    implicit none
    integer(4), intent(in) :: f90wrap_norx
    
    chem_norx = f90wrap_norx
end subroutine f90wrap_chem__set__norx

subroutine f90wrap_chem__get__redox_equil(f90wrap_redox_equil)
    use chem, only: chem_redox_equil => redox_equil
    implicit none
    logical, intent(out) :: f90wrap_redox_equil
    
    f90wrap_redox_equil = chem_redox_equil
end subroutine f90wrap_chem__get__redox_equil

subroutine f90wrap_chem__set__redox_equil(f90wrap_redox_equil)
    use chem, only: chem_redox_equil => redox_equil
    implicit none
    logical, intent(in) :: f90wrap_redox_equil
    
    chem_redox_equil = f90wrap_redox_equil
end subroutine f90wrap_chem__set__redox_equil

subroutine f90wrap_chem__array__cgc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cgc => cgc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cgc)) then
        dshape(1:1) = shape(chem_cgc)
        dloc = loc(chem_cgc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cgc

subroutine f90wrap_chem__array__rateg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rateg => rateg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rateg)) then
        dshape(1:1) = shape(chem_rateg)
        dloc = loc(chem_rateg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rateg

subroutine f90wrap_chem__array__totgn(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totgn => totgn
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totgn)) then
        dshape(1:1) = shape(chem_totgn)
        dloc = loc(chem_totgn)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totgn

subroutine f90wrap_chem__array__totgo(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totgo => totgo
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totgo)) then
        dshape(1:1) = shape(chem_totgo)
        dloc = loc(chem_totgo)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totgo

subroutine f90wrap_chem__array__totrateg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totrateg => totrateg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totrateg)) then
        dshape(1:1) = shape(chem_totrateg)
        dloc = loc(chem_totrateg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totrateg

subroutine f90wrap_chem__array__gfwg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwg => gfwg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwg)) then
        dshape(1:1) = shape(chem_gfwg)
        dloc = loc(chem_gfwg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwg

subroutine f90wrap_chem__array__eqg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqg => eqg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqg)) then
        dshape(1:1) = shape(chem_eqg)
        dloc = loc(chem_eqg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqg

subroutine f90wrap_chem__array__eqgs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqgs => eqgs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqgs)) then
        dshape(1:1) = shape(chem_eqgs)
        dloc = loc(chem_eqgs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqgs

subroutine f90wrap_chem__array__dhcg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcg => dhcg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcg)) then
        dshape(1:1) = shape(chem_dhcg)
        dloc = loc(chem_dhcg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcg

subroutine f90wrap_chem__array__xnug(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnug => xnug
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnug)) then
        dshape(1:1) = shape(chem_xnug)
        dloc = loc(chem_xnug)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnug

subroutine f90wrap_chem__get__degas_rate(f90wrap_degas_rate)
    use chem, only: chem_degas_rate => degas_rate
    implicit none
    real(8), intent(out) :: f90wrap_degas_rate
    
    f90wrap_degas_rate = chem_degas_rate
end subroutine f90wrap_chem__get__degas_rate

subroutine f90wrap_chem__set__degas_rate(f90wrap_degas_rate)
    use chem, only: chem_degas_rate => degas_rate
    implicit none
    real(8), intent(in) :: f90wrap_degas_rate
    
    chem_degas_rate = f90wrap_degas_rate
end subroutine f90wrap_chem__set__degas_rate

subroutine f90wrap_chem__array__iaga(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaga => iaga
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaga)) then
        dshape(1:1) = shape(chem_iaga)
        dloc = loc(chem_iaga)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaga

subroutine f90wrap_chem__array__jaga(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jaga => jaga
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jaga)) then
        dshape(1:1) = shape(chem_jaga)
        dloc = loc(chem_jaga)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jaga

subroutine f90wrap_chem__array__l_nameg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_nameg => l_nameg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_nameg)) then
        dshape(1:1) = shape(chem_l_nameg)
        dloc = loc(chem_l_nameg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_nameg

subroutine f90wrap_chem__get__gas_removal(f90wrap_gas_removal)
    use chem, only: chem_gas_removal => gas_removal
    implicit none
    logical, intent(out) :: f90wrap_gas_removal
    
    f90wrap_gas_removal = chem_gas_removal
end subroutine f90wrap_chem__get__gas_removal

subroutine f90wrap_chem__set__gas_removal(f90wrap_gas_removal)
    use chem, only: chem_gas_removal => gas_removal
    implicit none
    logical, intent(in) :: f90wrap_gas_removal
    
    chem_gas_removal = f90wrap_gas_removal
end subroutine f90wrap_chem__set__gas_removal

subroutine f90wrap_chem__array__csb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_csb => csb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_csb)) then
        dshape(1:1) = shape(chem_csb)
        dloc = loc(chem_csb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__csb

subroutine f90wrap_chem__array__chargesb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chargesb => chargesb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chargesb)) then
        dshape(1:1) = shape(chem_chargesb)
        dloc = loc(chem_chargesb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chargesb

subroutine f90wrap_chem__array__totcsn(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcsn => totcsn
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcsn)) then
        dshape(1:1) = shape(chem_totcsn)
        dloc = loc(chem_totcsn)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcsn

subroutine f90wrap_chem__array__totcso(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcso => totcso
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcso)) then
        dshape(1:1) = shape(chem_totcso)
        dloc = loc(chem_totcso)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcso

subroutine f90wrap_chem__array__gfwsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwsb => gfwsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwsb)) then
        dshape(1:1) = shape(chem_gfwsb)
        dloc = loc(chem_gfwsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwsb

subroutine f90wrap_chem__array__eqsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqsb => eqsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqsb)) then
        dshape(1:1) = shape(chem_eqsb)
        dloc = loc(chem_eqsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqsb

subroutine f90wrap_chem__array__eqsbs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqsbs => eqsbs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqsbs)) then
        dshape(1:1) = shape(chem_eqsbs)
        dloc = loc(chem_eqsbs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqsbs

subroutine f90wrap_chem__array__dhcsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcsb => dhcsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcsb)) then
        dshape(1:1) = shape(chem_dhcsb)
        dloc = loc(chem_dhcsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcsb

subroutine f90wrap_chem__array__xnusb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnusb => xnusb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnusb)) then
        dshape(1:1) = shape(chem_xnusb)
        dloc = loc(chem_xnusb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnusb

subroutine f90wrap_chem__array__site_area(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_site_area => site_area
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_site_area)) then
        dshape(1:1) = shape(chem_site_area)
        dloc = loc(chem_site_area)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__site_area

subroutine f90wrap_chem__array__site_dens(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_site_dens => site_dens
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_site_dens)) then
        dshape(1:1) = shape(chem_site_dens)
        dloc = loc(chem_site_dens)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__site_dens

subroutine f90wrap_chem__array__site_mass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_site_mass => site_mass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_site_mass)) then
        dshape(1:1) = shape(chem_site_mass)
        dloc = loc(chem_site_mass)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__site_mass

subroutine f90wrap_chem__array__dcalcpsi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dcalcpsi => dcalcpsi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dcalcpsi)) then
        dshape(1:1) = shape(chem_dcalcpsi)
        dloc = loc(chem_dcalcpsi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dcalcpsi

subroutine f90wrap_chem__array__cap1(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cap1 => cap1
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cap1)) then
        dshape(1:1) = shape(chem_cap1)
        dloc = loc(chem_cap1)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cap1

subroutine f90wrap_chem__array__cap2(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cap2 => cap2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cap2)) then
        dshape(1:1) = shape(chem_cap2)
        dloc = loc(chem_cap2)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cap2

subroutine f90wrap_chem__array__strionsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_strionsb => strionsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_strionsb)) then
        dshape(1:1) = shape(chem_strionsb)
        dloc = loc(chem_strionsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__strionsb

subroutine f90wrap_chem__array__surfacensb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_surfacensb => surfacensb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_surfacensb)) then
        dshape(1:1) = shape(chem_surfacensb)
        dloc = loc(chem_surfacensb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__surfacensb

subroutine f90wrap_chem__array__calcpsi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_calcpsi => calcpsi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_calcpsi)) then
        dshape(1:1) = shape(chem_calcpsi)
        dloc = loc(chem_calcpsi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__calcpsi

subroutine f90wrap_chem__array__totpsi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totpsi => totpsi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totpsi)) then
        dshape(1:1) = shape(chem_totpsi)
        dloc = loc(chem_totpsi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totpsi

subroutine f90wrap_chem__array__dtotpsi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotpsi => dtotpsi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotpsi)) then
        dshape(1:1) = shape(chem_dtotpsi)
        dloc = loc(chem_dtotpsi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotpsi

subroutine f90wrap_chem__array__dcnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dcnew => dcnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dcnew)) then
        dshape(1:1) = shape(chem_dcnew)
        dloc = loc(chem_dcnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dcnew

subroutine f90wrap_chem__get__cec(f90wrap_cec)
    use chem, only: chem_cec => cec
    implicit none
    real(8), intent(out) :: f90wrap_cec
    
    f90wrap_cec = chem_cec
end subroutine f90wrap_chem__get__cec

subroutine f90wrap_chem__set__cec(f90wrap_cec)
    use chem, only: chem_cec => cec
    implicit none
    real(8), intent(in) :: f90wrap_cec
    
    chem_cec = f90wrap_cec
end subroutine f90wrap_chem__set__cec

subroutine f90wrap_chem__get__rhobulk(f90wrap_rhobulk)
    use chem, only: chem_rhobulk => rhobulk
    implicit none
    real(8), intent(out) :: f90wrap_rhobulk
    
    f90wrap_rhobulk = chem_rhobulk
end subroutine f90wrap_chem__get__rhobulk

subroutine f90wrap_chem__set__rhobulk(f90wrap_rhobulk)
    use chem, only: chem_rhobulk => rhobulk
    implicit none
    real(8), intent(in) :: f90wrap_rhobulk
    
    chem_rhobulk = f90wrap_rhobulk
end subroutine f90wrap_chem__set__rhobulk

subroutine f90wrap_chem__array__iaic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iaic => iaic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iaic)) then
        dshape(1:1) = shape(chem_iaic)
        dloc = loc(chem_iaic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iaic

subroutine f90wrap_chem__array__iais(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iais => iais
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iais)) then
        dshape(1:1) = shape(chem_iais)
        dloc = loc(chem_iais)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iais

subroutine f90wrap_chem__array__iasb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iasb => iasb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iasb)) then
        dshape(1:1) = shape(chem_iasb)
        dloc = loc(chem_iasb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iasb

subroutine f90wrap_chem__array__jasb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jasb => jasb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jasb)) then
        dshape(1:1) = shape(chem_jasb)
        dloc = loc(chem_jasb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jasb

subroutine f90wrap_chem__array__l_namesb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namesb => l_namesb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namesb)) then
        dshape(1:1) = shape(chem_l_namesb)
        dloc = loc(chem_l_namesb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namesb

subroutine f90wrap_chem__get__nsb(f90wrap_nsb)
    use chem, only: chem_nsb => nsb
    implicit none
    integer(4), intent(out) :: f90wrap_nsb
    
    f90wrap_nsb = chem_nsb
end subroutine f90wrap_chem__get__nsb

subroutine f90wrap_chem__set__nsb(f90wrap_nsb)
    use chem, only: chem_nsb => nsb
    implicit none
    integer(4), intent(in) :: f90wrap_nsb
    
    chem_nsb = f90wrap_nsb
end subroutine f90wrap_chem__set__nsb

subroutine f90wrap_chem__get__nsites(f90wrap_nsites)
    use chem, only: chem_nsites => nsites
    implicit none
    integer(4), intent(out) :: f90wrap_nsites
    
    f90wrap_nsites = chem_nsites
end subroutine f90wrap_chem__get__nsites

subroutine f90wrap_chem__set__nsites(f90wrap_nsites)
    use chem, only: chem_nsites => nsites
    implicit none
    integer(4), intent(in) :: f90wrap_nsites
    
    chem_nsites = f90wrap_nsites
end subroutine f90wrap_chem__set__nsites

subroutine f90wrap_chem__get__nsites2(f90wrap_nsites2)
    use chem, only: chem_nsites2 => nsites2
    implicit none
    integer(4), intent(out) :: f90wrap_nsites2
    
    f90wrap_nsites2 = chem_nsites2
end subroutine f90wrap_chem__get__nsites2

subroutine f90wrap_chem__set__nsites2(f90wrap_nsites2)
    use chem, only: chem_nsites2 => nsites2
    implicit none
    integer(4), intent(in) :: f90wrap_nsites2
    
    chem_nsites2 = f90wrap_nsites2
end subroutine f90wrap_chem__set__nsites2

subroutine f90wrap_chem__get__nlinear(f90wrap_nlinear)
    use chem, only: chem_nlinear => nlinear
    implicit none
    integer(4), intent(out) :: f90wrap_nlinear
    
    f90wrap_nlinear = chem_nlinear
end subroutine f90wrap_chem__get__nlinear

subroutine f90wrap_chem__set__nlinear(f90wrap_nlinear)
    use chem, only: chem_nlinear => nlinear
    implicit none
    integer(4), intent(in) :: f90wrap_nlinear
    
    chem_nlinear = f90wrap_nlinear
end subroutine f90wrap_chem__set__nlinear

subroutine f90wrap_chem__get__nelec(f90wrap_nelec)
    use chem, only: chem_nelec => nelec
    implicit none
    integer(4), intent(out) :: f90wrap_nelec
    
    f90wrap_nelec = chem_nelec
end subroutine f90wrap_chem__get__nelec

subroutine f90wrap_chem__set__nelec(f90wrap_nelec)
    use chem, only: chem_nelec => nelec
    implicit none
    integer(4), intent(in) :: f90wrap_nelec
    
    chem_nelec = f90wrap_nelec
end subroutine f90wrap_chem__set__nelec

subroutine f90wrap_chem__array__chargencsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_chargencsb => chargencsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_chargencsb)) then
        dshape(1:1) = shape(chem_chargencsb)
        dloc = loc(chem_chargencsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__chargencsb

subroutine f90wrap_chem__array__totan(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totan => totan
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totan)) then
        dshape(1:1) = shape(chem_totan)
        dloc = loc(chem_totan)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totan

subroutine f90wrap_chem__array__totao(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totao => totao
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totao)) then
        dshape(1:1) = shape(chem_totao)
        dloc = loc(chem_totao)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totao

subroutine f90wrap_chem__array__gfwncsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwncsb => gfwncsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwncsb)) then
        dshape(1:1) = shape(chem_gfwncsb)
        dloc = loc(chem_gfwncsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwncsb

subroutine f90wrap_chem__array__eqncsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqncsb => eqncsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqncsb)) then
        dshape(1:1) = shape(chem_eqncsb)
        dloc = loc(chem_eqncsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqncsb

subroutine f90wrap_chem__array__eqncsbs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqncsbs => eqncsbs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqncsbs)) then
        dshape(1:1) = shape(chem_eqncsbs)
        dloc = loc(chem_eqncsbs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqncsbs

subroutine f90wrap_chem__array__dhncsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhncsb => dhncsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhncsb)) then
        dshape(1:1) = shape(chem_dhncsb)
        dloc = loc(chem_dhncsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhncsb

subroutine f90wrap_chem__array__xnuncsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnuncsb => xnuncsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnuncsb)) then
        dshape(1:1) = shape(chem_xnuncsb)
        dloc = loc(chem_xnuncsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnuncsb

subroutine f90wrap_chem__array__iancsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iancsb => iancsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iancsb)) then
        dshape(1:1) = shape(chem_iancsb)
        dloc = loc(chem_iancsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iancsb

subroutine f90wrap_chem__array__jancsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jancsb => jancsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jancsb)) then
        dshape(1:1) = shape(chem_jancsb)
        dloc = loc(chem_jancsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jancsb

subroutine f90wrap_chem__array__l_nameanc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_nameanc => l_nameanc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_nameanc)) then
        dshape(1:1) = shape(chem_l_nameanc)
        dloc = loc(chem_l_nameanc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_nameanc

subroutine f90wrap_chem__get__nanc(f90wrap_nanc)
    use chem, only: chem_nanc => nanc
    implicit none
    integer(4), intent(out) :: f90wrap_nanc
    
    f90wrap_nanc = chem_nanc
end subroutine f90wrap_chem__get__nanc

subroutine f90wrap_chem__set__nanc(f90wrap_nanc)
    use chem, only: chem_nanc => nanc
    implicit none
    integer(4), intent(in) :: f90wrap_nanc
    
    chem_nanc = f90wrap_nanc
end subroutine f90wrap_chem__set__nanc

subroutine f90wrap_chem__get__ncsb(f90wrap_ncsb)
    use chem, only: chem_ncsb => ncsb
    implicit none
    integer(4), intent(out) :: f90wrap_ncsb
    
    f90wrap_ncsb = chem_ncsb
end subroutine f90wrap_chem__get__ncsb

subroutine f90wrap_chem__set__ncsb(f90wrap_ncsb)
    use chem, only: chem_ncsb => ncsb
    implicit none
    integer(4), intent(in) :: f90wrap_ncsb
    
    chem_ncsb = f90wrap_ncsb
end subroutine f90wrap_chem__set__ncsb

subroutine &
    f90wrap_chem__get__noncompetitive_sorption(f90wrap_noncompetitive_sorption)
    use chem, only: chem_noncompetitive_sorption => noncompetitive_sorption
    implicit none
    logical, intent(out) :: f90wrap_noncompetitive_sorption
    
    f90wrap_noncompetitive_sorption = chem_noncompetitive_sorption
end subroutine f90wrap_chem__get__noncompetitive_sorption

subroutine &
    f90wrap_chem__set__noncompetitive_sorption(f90wrap_noncompetitive_sorption)
    use chem, only: chem_noncompetitive_sorption => noncompetitive_sorption
    implicit none
    logical, intent(in) :: f90wrap_noncompetitive_sorption
    
    chem_noncompetitive_sorption = f90wrap_noncompetitive_sorption
end subroutine f90wrap_chem__set__noncompetitive_sorption

subroutine f90wrap_chem__get__linear_sorption(f90wrap_linear_sorption)
    use chem, only: chem_linear_sorption => linear_sorption
    implicit none
    logical, intent(out) :: f90wrap_linear_sorption
    
    f90wrap_linear_sorption = chem_linear_sorption
end subroutine f90wrap_chem__get__linear_sorption

subroutine f90wrap_chem__set__linear_sorption(f90wrap_linear_sorption)
    use chem, only: chem_linear_sorption => linear_sorption
    implicit none
    logical, intent(in) :: f90wrap_linear_sorption
    
    chem_linear_sorption = f90wrap_linear_sorption
end subroutine f90wrap_chem__set__linear_sorption

subroutine f90wrap_chem__array__areac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_areac => areac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_areac)) then
        dshape(1:1) = shape(chem_areac)
        dloc = loc(chem_areac)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__areac

subroutine f90wrap_chem__array__areainit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_areainit => areainit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_areainit)) then
        dshape(1:1) = shape(chem_areainit)
        dloc = loc(chem_areainit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__areainit

subroutine f90wrap_chem__array__cmcold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cmcold => cmcold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cmcold)) then
        dshape(1:1) = shape(chem_cmcold)
        dloc = loc(chem_cmcold)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cmcold

subroutine f90wrap_chem__array__cmcnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cmcnew => cmcnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cmcnew)) then
        dshape(1:1) = shape(chem_cmcnew)
        dloc = loc(chem_cmcnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cmcnew

subroutine f90wrap_chem__array__cmcmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cmcmin => cmcmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cmcmin)) then
        dshape(1:1) = shape(chem_cmcmin)
        dloc = loc(chem_cmcmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cmcmin

subroutine f90wrap_chem__array__dgcm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dgcm => dgcm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dgcm)) then
        dshape(1:1) = shape(chem_dgcm)
        dloc = loc(chem_dgcm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dgcm

subroutine f90wrap_chem__array__dhcm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcm => dhcm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcm)) then
        dshape(1:1) = shape(chem_dhcm)
        dloc = loc(chem_dhcm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcm

subroutine f90wrap_chem__array__dhcmx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dhcmx => dhcmx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dhcmx)) then
        dshape(1:1) = shape(chem_dhcmx)
        dloc = loc(chem_dhcmx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dhcmx

subroutine f90wrap_chem__array__expphi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_expphi => expphi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_expphi)) then
        dshape(1:1) = shape(chem_expphi)
        dloc = loc(chem_expphi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__expphi

subroutine f90wrap_chem__array__phic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phic => phic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phic)) then
        dshape(1:1) = shape(chem_phic)
        dloc = loc(chem_phic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phic

subroutine f90wrap_chem__array__phicold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phicold => phicold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phicold)) then
        dshape(1:1) = shape(chem_phicold)
        dloc = loc(chem_phicold)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phicold

subroutine f90wrap_chem__array__fmdi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmdi => fmdi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmdi)) then
        dshape(1:1) = shape(chem_fmdi)
        dloc = loc(chem_fmdi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmdi

subroutine f90wrap_chem__array__fmdm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmdm => fmdm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmdm)) then
        dshape(1:1) = shape(chem_fmdm)
        dloc = loc(chem_fmdm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmdm

subroutine f90wrap_chem__array__fmic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmic => fmic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmic)) then
        dshape(1:1) = shape(chem_fmic)
        dloc = loc(chem_fmic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmic

subroutine f90wrap_chem__array__fmhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmhc => fmhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmhc)) then
        dshape(1:1) = shape(chem_fmhc)
        dloc = loc(chem_fmhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmhc

subroutine f90wrap_chem__array__fmdpi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmdpi => fmdpi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmdpi)) then
        dshape(1:1) = shape(chem_fmdpi)
        dloc = loc(chem_fmdpi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmdpi

subroutine f90wrap_chem__array__fmdpm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_fmdpm => fmdpm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_fmdpm)) then
        dshape(1:1) = shape(chem_fmdpm)
        dloc = loc(chem_fmdpm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__fmdpm

subroutine f90wrap_chem__array__rads(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rads => rads
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rads)) then
        dshape(1:1) = shape(chem_rads)
        dloc = loc(chem_rads)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rads

subroutine f90wrap_chem__array__radi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_radi => radi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_radi)) then
        dshape(1:1) = shape(chem_radi)
        dloc = loc(chem_radi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__radi

subroutine f90wrap_chem__array__phimin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phimin => phimin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phimin)) then
        dshape(1:1) = shape(chem_phimin)
        dloc = loc(chem_phimin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phimin

subroutine f90wrap_chem__array__phimin_out(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phimin_out => phimin_out
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phimin_out)) then
        dshape(1:1) = shape(chem_phimin_out)
        dloc = loc(chem_phimin_out)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phimin_out

subroutine f90wrap_chem__array__phiinit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phiinit => phiinit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phiinit)) then
        dshape(1:1) = shape(chem_phiinit)
        dloc = loc(chem_phiinit)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phiinit

subroutine f90wrap_chem__array__phi_out(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_phi_out => phi_out
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_phi_out)) then
        dshape(1:1) = shape(chem_phi_out)
        dloc = loc(chem_phi_out)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__phi_out

subroutine f90wrap_chem__array__radmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_radmin => radmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_radmin)) then
        dshape(1:1) = shape(chem_radmin)
        dloc = loc(chem_radmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__radmin

subroutine f90wrap_chem__array__supsatm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_supsatm => supsatm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_supsatm)) then
        dshape(1:1) = shape(chem_supsatm)
        dloc = loc(chem_supsatm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__supsatm

subroutine f90wrap_chem__array__scalfac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_scalfac => scalfac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_scalfac)) then
        dshape(1:1) = shape(chem_scalfac)
        dloc = loc(chem_scalfac)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__scalfac

subroutine f90wrap_chem__array__gfwm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gfwm => gfwm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_gfwm)) then
        dshape(1:1) = shape(chem_gfwm)
        dloc = loc(chem_gfwm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__gfwm

subroutine f90wrap_chem__array__diffm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_diffm => diffm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_diffm)) then
        dshape(1:1) = shape(chem_diffm)
        dloc = loc(chem_diffm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__diffm

subroutine f90wrap_chem__array__densm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_densm => densm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_densm)) then
        dshape(1:1) = shape(chem_densm)
        dloc = loc(chem_densm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__densm

subroutine f90wrap_chem__array__eqm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqm => eqm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqm)) then
        dshape(1:1) = shape(chem_eqm)
        dloc = loc(chem_eqm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqm

subroutine f90wrap_chem__array__eqmx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqmx => eqmx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqmx)) then
        dshape(1:1) = shape(chem_eqmx)
        dloc = loc(chem_eqmx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqmx

subroutine f90wrap_chem__array__eqms(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqms => eqms
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqms)) then
        dshape(1:1) = shape(chem_eqms)
        dloc = loc(chem_eqms)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqms

subroutine f90wrap_chem__array__eqmxs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_eqmxs => eqmxs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_eqmxs)) then
        dshape(1:1) = shape(chem_eqmxs)
        dloc = loc(chem_eqmxs)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__eqmxs

subroutine f90wrap_chem__array__rated(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rated => rated
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rated)) then
        dshape(1:1) = shape(chem_rated)
        dloc = loc(chem_rated)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rated

subroutine f90wrap_chem__array__rateds(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_rateds => rateds
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_rateds)) then
        dshape(1:1) = shape(chem_rateds)
        dloc = loc(chem_rateds)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__rateds

subroutine f90wrap_chem__array__ratemp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ratemp => ratemp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ratemp)) then
        dshape(1:1) = shape(chem_ratemp)
        dloc = loc(chem_ratemp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ratemp

subroutine f90wrap_chem__array__orddc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_orddc => orddc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_orddc)) then
        dshape(1:1) = shape(chem_orddc)
        dloc = loc(chem_orddc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__orddc

subroutine f90wrap_chem__array__orddcx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_orddcx => orddcx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_orddcx)) then
        dshape(1:1) = shape(chem_orddcx)
        dloc = loc(chem_orddcx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__orddcx

subroutine f90wrap_chem__array__orddt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_orddt => orddt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_orddt)) then
        dshape(1:1) = shape(chem_orddt)
        dloc = loc(chem_orddt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__orddt

subroutine f90wrap_chem__array__orddm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_orddm => orddm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_orddm)) then
        dshape(1:1) = shape(chem_orddm)
        dloc = loc(chem_orddm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__orddm

subroutine f90wrap_chem__array__ordm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordm => ordm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordm)) then
        dshape(1:1) = shape(chem_ordm)
        dloc = loc(chem_ordm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordm

subroutine f90wrap_chem__array__ordmdi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmdi => ordmdi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmdi)) then
        dshape(1:1) = shape(chem_ordmdi)
        dloc = loc(chem_ordmdi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmdi

subroutine f90wrap_chem__array__ordmdm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmdm => ordmdm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmdm)) then
        dshape(1:1) = shape(chem_ordmdm)
        dloc = loc(chem_ordmdm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmdm

subroutine f90wrap_chem__array__ordmic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmic => ordmic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmic)) then
        dshape(1:1) = shape(chem_ordmic)
        dloc = loc(chem_ordmic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmic

subroutine f90wrap_chem__array__ordmhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmhc => ordmhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmhc)) then
        dshape(1:1) = shape(chem_ordmhc)
        dloc = loc(chem_ordmhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmhc

subroutine f90wrap_chem__array__ordmdpi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmdpi => ordmdpi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmdpi)) then
        dshape(1:1) = shape(chem_ordmdpi)
        dloc = loc(chem_ordmdpi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmdpi

subroutine f90wrap_chem__array__ordmdpm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordmdpm => ordmdpm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordmdpm)) then
        dshape(1:1) = shape(chem_ordmdpm)
        dloc = loc(chem_ordmdpm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordmdpm

subroutine f90wrap_chem__array__ordn(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ordn => ordn
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ordn)) then
        dshape(1:1) = shape(chem_ordn)
        dloc = loc(chem_ordn)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ordn

subroutine f90wrap_chem__array__totratem(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totratem => totratem
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totratem)) then
        dshape(1:1) = shape(chem_totratem)
        dloc = loc(chem_totratem)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totratem

subroutine f90wrap_chem__array__xnud(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnud => xnud
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnud)) then
        dshape(1:1) = shape(chem_xnud)
        dloc = loc(chem_xnud)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnud

subroutine f90wrap_chem__array__xnum(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnum => xnum
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnum)) then
        dshape(1:1) = shape(chem_xnum)
        dloc = loc(chem_xnum)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnum

subroutine f90wrap_chem__array__xnumx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_xnumx => xnumx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_xnumx)) then
        dshape(1:1) = shape(chem_xnumx)
        dloc = loc(chem_xnumx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__xnumx

subroutine f90wrap_chem__array__satm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_satm => satm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_satm)) then
        dshape(1:1) = shape(chem_satm)
        dloc = loc(chem_satm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__satm

subroutine f90wrap_chem__array__satm_log(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_satm_log => satm_log
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_satm_log)) then
        dshape(1:1) = shape(chem_satm_log)
        dloc = loc(chem_satm_log)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__satm_log

subroutine f90wrap_chem__array__satmx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_satmx => satmx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_satmx)) then
        dshape(1:1) = shape(chem_satmx)
        dloc = loc(chem_satmx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__satmx

subroutine f90wrap_chem__get__conc_mol_avg(f90wrap_conc_mol_avg)
    use chem, only: chem_conc_mol_avg => conc_mol_avg
    implicit none
    real(8), intent(out) :: f90wrap_conc_mol_avg
    
    f90wrap_conc_mol_avg = chem_conc_mol_avg
end subroutine f90wrap_chem__get__conc_mol_avg

subroutine f90wrap_chem__set__conc_mol_avg(f90wrap_conc_mol_avg)
    use chem, only: chem_conc_mol_avg => conc_mol_avg
    implicit none
    real(8), intent(in) :: f90wrap_conc_mol_avg
    
    chem_conc_mol_avg = f90wrap_conc_mol_avg
end subroutine f90wrap_chem__set__conc_mol_avg

subroutine f90wrap_chem__array__iam(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iam => iam
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iam)) then
        dshape(1:1) = shape(chem_iam)
        dloc = loc(chem_iam)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iam

subroutine f90wrap_chem__array__iamx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamx => iamx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamx)) then
        dshape(1:1) = shape(chem_iamx)
        dloc = loc(chem_iamx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamx

subroutine f90wrap_chem__array__iamd(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamd => iamd
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamd)) then
        dshape(1:1) = shape(chem_iamd)
        dloc = loc(chem_iamd)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamd

subroutine f90wrap_chem__array__iamdc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdc => iamdc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdc)) then
        dshape(1:1) = shape(chem_iamdc)
        dloc = loc(chem_iamdc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdc

subroutine f90wrap_chem__array__iamdcx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdcx => iamdcx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdcx)) then
        dshape(1:1) = shape(chem_iamdcx)
        dloc = loc(chem_iamdcx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdcx

subroutine f90wrap_chem__array__iamdi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdi => iamdi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdi)) then
        dshape(1:1) = shape(chem_iamdi)
        dloc = loc(chem_iamdi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdi

subroutine f90wrap_chem__array__iamdm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdm => iamdm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdm)) then
        dshape(1:1) = shape(chem_iamdm)
        dloc = loc(chem_iamdm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdm

subroutine f90wrap_chem__array__iamic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamic => iamic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamic)) then
        dshape(1:1) = shape(chem_iamic)
        dloc = loc(chem_iamic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamic

subroutine f90wrap_chem__array__iamhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamhc => iamhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamhc)) then
        dshape(1:1) = shape(chem_iamhc)
        dloc = loc(chem_iamhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamhc

subroutine f90wrap_chem__array__iamdpi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdpi => iamdpi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdpi)) then
        dshape(1:1) = shape(chem_iamdpi)
        dloc = loc(chem_iamdpi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdpi

subroutine f90wrap_chem__array__iamdpm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdpm => iamdpm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdpm)) then
        dshape(1:1) = shape(chem_iamdpm)
        dloc = loc(chem_iamdpm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdpm

subroutine f90wrap_chem__array__iamdt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdt => iamdt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdt)) then
        dshape(1:1) = shape(chem_iamdt)
        dloc = loc(chem_iamdt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdt

subroutine f90wrap_chem__array__iamdmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamdmin => iamdmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamdmin)) then
        dshape(1:1) = shape(chem_iamdmin)
        dloc = loc(chem_iamdmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamdmin

subroutine f90wrap_chem__array__iamp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_iamp => iamp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_iamp)) then
        dshape(1:1) = shape(chem_iamp)
        dloc = loc(chem_iamp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__iamp

subroutine f90wrap_chem__array__jam(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jam => jam
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jam)) then
        dshape(1:1) = shape(chem_jam)
        dloc = loc(chem_jam)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jam

subroutine f90wrap_chem__array__jamx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamx => jamx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamx)) then
        dshape(1:1) = shape(chem_jamx)
        dloc = loc(chem_jamx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamx

subroutine f90wrap_chem__array__jamdc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdc => jamdc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdc)) then
        dshape(1:1) = shape(chem_jamdc)
        dloc = loc(chem_jamdc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdc

subroutine f90wrap_chem__array__jamdcx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdcx => jamdcx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdcx)) then
        dshape(1:1) = shape(chem_jamdcx)
        dloc = loc(chem_jamdcx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdcx

subroutine f90wrap_chem__array__jamdi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdi => jamdi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdi)) then
        dshape(1:1) = shape(chem_jamdi)
        dloc = loc(chem_jamdi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdi

subroutine f90wrap_chem__array__jamdm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdm => jamdm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdm)) then
        dshape(1:1) = shape(chem_jamdm)
        dloc = loc(chem_jamdm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdm

subroutine f90wrap_chem__array__jamic(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamic => jamic
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamic)) then
        dshape(1:1) = shape(chem_jamic)
        dloc = loc(chem_jamic)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamic

subroutine f90wrap_chem__array__jamhc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamhc => jamhc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamhc)) then
        dshape(1:1) = shape(chem_jamhc)
        dloc = loc(chem_jamhc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamhc

subroutine f90wrap_chem__array__jamdpi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdpi => jamdpi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdpi)) then
        dshape(1:1) = shape(chem_jamdpi)
        dloc = loc(chem_jamdpi)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdpi

subroutine f90wrap_chem__array__jamdpm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdpm => jamdpm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdpm)) then
        dshape(1:1) = shape(chem_jamdpm)
        dloc = loc(chem_jamdpm)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdpm

subroutine f90wrap_chem__array__jamdt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdt => jamdt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdt)) then
        dshape(1:1) = shape(chem_jamdt)
        dloc = loc(chem_jamdt)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdt

subroutine f90wrap_chem__array__jamdmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamdmin => jamdmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamdmin)) then
        dshape(1:1) = shape(chem_jamdmin)
        dloc = loc(chem_jamdmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamdmin

subroutine f90wrap_chem__array__jamp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_jamp => jamp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_jamp)) then
        dshape(1:1) = shape(chem_jamp)
        dloc = loc(chem_jamp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__jamp

subroutine f90wrap_chem__array__l_namem(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namem => l_namem
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namem)) then
        dshape(1:1) = shape(chem_l_namem)
        dloc = loc(chem_l_namem)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namem

subroutine f90wrap_chem__array__l_namemp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namemp => l_namemp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namemp)) then
        dshape(1:1) = shape(chem_l_namemp)
        dloc = loc(chem_l_namemp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namemp

subroutine f90wrap_chem__array__l_namemx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_l_namemx => l_namemx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_l_namemx)) then
        dshape(1:1) = shape(chem_l_namemx)
        dloc = loc(chem_l_namemx)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__l_namemx

subroutine f90wrap_chem__array__far_from_equil(dummy_this, nd, dtype, dshape, &
    dloc)
    use parm
    use chem, only: chem_far_from_equil => far_from_equil
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(chem_far_from_equil)) then
        dshape(1:1) = shape(chem_far_from_equil)
        dloc = loc(chem_far_from_equil)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__far_from_equil

subroutine f90wrap_chem__array__tmp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_tmp => tmp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_tmp)) then
        dshape(1:1) = shape(chem_tmp)
        dloc = loc(chem_tmp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__tmp

subroutine f90wrap_chem__array__ztmp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ztmp => ztmp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ztmp)) then
        dshape(1:1) = shape(chem_ztmp)
        dloc = loc(chem_ztmp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ztmp

subroutine f90wrap_chem__get__dt_tmp(f90wrap_dt_tmp)
    use chem, only: chem_dt_tmp => dt_tmp
    implicit none
    real(8), intent(out) :: f90wrap_dt_tmp
    
    f90wrap_dt_tmp = chem_dt_tmp
end subroutine f90wrap_chem__get__dt_tmp

subroutine f90wrap_chem__set__dt_tmp(f90wrap_dt_tmp)
    use chem, only: chem_dt_tmp => dt_tmp
    implicit none
    real(8), intent(in) :: f90wrap_dt_tmp
    
    chem_dt_tmp = f90wrap_dt_tmp
end subroutine f90wrap_chem__set__dt_tmp

subroutine f90wrap_chem__get__tmp_read(f90wrap_tmp_read)
    use chem, only: chem_tmp_read => tmp_read
    implicit none
    real(8), intent(out) :: f90wrap_tmp_read
    
    f90wrap_tmp_read = chem_tmp_read
end subroutine f90wrap_chem__get__tmp_read

subroutine f90wrap_chem__set__tmp_read(f90wrap_tmp_read)
    use chem, only: chem_tmp_read => tmp_read
    implicit none
    real(8), intent(in) :: f90wrap_tmp_read
    
    chem_tmp_read = f90wrap_tmp_read
end subroutine f90wrap_chem__set__tmp_read

subroutine f90wrap_chem__get__ntmp(f90wrap_ntmp)
    use chem, only: chem_ntmp => ntmp
    implicit none
    integer(4), intent(out) :: f90wrap_ntmp
    
    f90wrap_ntmp = chem_ntmp
end subroutine f90wrap_chem__get__ntmp

subroutine f90wrap_chem__set__ntmp(f90wrap_ntmp)
    use chem, only: chem_ntmp => ntmp
    implicit none
    integer(4), intent(in) :: f90wrap_ntmp
    
    chem_ntmp = f90wrap_ntmp
end subroutine f90wrap_chem__set__ntmp

subroutine f90wrap_chem__get__update_temp(f90wrap_update_temp)
    use chem, only: chem_update_temp => update_temp
    implicit none
    logical, intent(out) :: f90wrap_update_temp
    
    f90wrap_update_temp = chem_update_temp
end subroutine f90wrap_chem__get__update_temp

subroutine f90wrap_chem__set__update_temp(f90wrap_update_temp)
    use chem, only: chem_update_temp => update_temp
    implicit none
    logical, intent(in) :: f90wrap_update_temp
    
    chem_update_temp = f90wrap_update_temp
end subroutine f90wrap_chem__set__update_temp

subroutine f90wrap_chem__array__cinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cinc => cinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cinc)) then
        dshape(1:1) = shape(chem_cinc)
        dloc = loc(chem_cinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cinc

subroutine f90wrap_chem__array__cxinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_cxinc => cxinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_cxinc)) then
        dshape(1:1) = shape(chem_cxinc)
        dloc = loc(chem_cxinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__cxinc

subroutine f90wrap_chem__array__dcsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dcsb => dcsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dcsb)) then
        dshape(1:1) = shape(chem_dcsb)
        dloc = loc(chem_dcsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dcsb

subroutine f90wrap_chem__array__dncsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dncsb => dncsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dncsb)) then
        dshape(1:1) = shape(chem_dncsb)
        dloc = loc(chem_dncsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dncsb

subroutine f90wrap_chem__array__ginc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ginc => ginc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ginc)) then
        dshape(1:1) = shape(chem_ginc)
        dloc = loc(chem_ginc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ginc

subroutine f90wrap_chem__array__dtotc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotc => dtotc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotc)) then
        dshape(1:1) = shape(chem_dtotc)
        dloc = loc(chem_dtotc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotc

subroutine f90wrap_chem__array__dtotg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotg => dtotg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotg)) then
        dshape(1:1) = shape(chem_dtotg)
        dloc = loc(chem_dtotg)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotg

subroutine f90wrap_chem__array__dtotsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotsb => dtotsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotsb)) then
        dshape(1:1) = shape(chem_dtotsb)
        dloc = loc(chem_dtotsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotsb

subroutine f90wrap_chem__array__ratedp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_ratedp => ratedp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_ratedp)) then
        dshape(1:1) = shape(chem_ratedp)
        dloc = loc(chem_ratedp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__ratedp

subroutine f90wrap_chem__array__dratedp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dratedp => dratedp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dratedp)) then
        dshape(1:1) = shape(chem_dratedp)
        dloc = loc(chem_dratedp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dratedp

subroutine f90wrap_chem__array__totdp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totdp => totdp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totdp)) then
        dshape(1:1) = shape(chem_totdp)
        dloc = loc(chem_totdp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totdp

subroutine f90wrap_chem__array__dtotdp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtotdp => dtotdp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtotdp)) then
        dshape(1:1) = shape(chem_dtotdp)
        dloc = loc(chem_dtotdp)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtotdp

subroutine f90wrap_chem__array__totsb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totsb => totsb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totsb)) then
        dshape(1:1) = shape(chem_totsb)
        dloc = loc(chem_totsb)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totsb

subroutine f90wrap_chem__array__totcinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_totcinc => totcinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_totcinc)) then
        dshape(1:1) = shape(chem_totcinc)
        dloc = loc(chem_totcinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__totcinc

subroutine f90wrap_chem__array__dtota(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_dtota => dtota
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_dtota)) then
        dshape(1:1) = shape(chem_dtota)
        dloc = loc(chem_dtota)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__dtota

subroutine f90wrap_chem__array__alc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_alc => alc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(chem_alc)) then
        dshape(1:2) = shape(chem_alc)
        dloc = loc(chem_alc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__alc

subroutine f90wrap_chem__array__blc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_blc => blc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(chem_blc)) then
        dshape(1:1) = shape(chem_blc)
        dloc = loc(chem_blc)
    else
        dloc = 0
    end if
end subroutine f90wrap_chem__array__blc

subroutine f90wrap_chem__array__conct(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_conct => conct
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    dshape(1:1) = shape(chem_conct)
    dloc = loc(chem_conct)
end subroutine f90wrap_chem__array__conct

subroutine f90wrap_chem__array__gammat(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use chem, only: chem_gammat => gammat
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    dshape(1:1) = shape(chem_gammat)
    dloc = loc(chem_gammat)
end subroutine f90wrap_chem__array__gammat

subroutine f90wrap_chem__get__depth_dependence(f90wrap_depth_dependence)
    use chem, only: chem_depth_dependence => depth_dependence
    implicit none
    logical, intent(out) :: f90wrap_depth_dependence
    
    f90wrap_depth_dependence = chem_depth_dependence
end subroutine f90wrap_chem__get__depth_dependence

subroutine f90wrap_chem__set__depth_dependence(f90wrap_depth_dependence)
    use chem, only: chem_depth_dependence => depth_dependence
    implicit none
    logical, intent(in) :: f90wrap_depth_dependence
    
    chem_depth_dependence = f90wrap_depth_dependence
end subroutine f90wrap_chem__set__depth_dependence

! End of module chem defined in file ../src/chem.f

