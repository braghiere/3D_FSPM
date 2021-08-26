! Module gen defined in file ../src/gen.f

subroutine f90wrap_gen__get__cpuint(f90wrap_cpuint)
    use gen, only: gen_cpuint => cpuint
    implicit none
    real(8), intent(out) :: f90wrap_cpuint
    
    f90wrap_cpuint = gen_cpuint
end subroutine f90wrap_gen__get__cpuint

subroutine f90wrap_gen__set__cpuint(f90wrap_cpuint)
    use gen, only: gen_cpuint => cpuint
    implicit none
    real(8), intent(in) :: f90wrap_cpuint
    
    gen_cpuint = f90wrap_cpuint
end subroutine f90wrap_gen__set__cpuint

subroutine f90wrap_gen__get__csec(f90wrap_csec)
    use gen, only: gen_csec => csec
    implicit none
    real(8), intent(out) :: f90wrap_csec
    
    f90wrap_csec = gen_csec
end subroutine f90wrap_gen__get__csec

subroutine f90wrap_gen__set__csec(f90wrap_csec)
    use gen, only: gen_csec => csec
    implicit none
    real(8), intent(in) :: f90wrap_csec
    
    gen_csec = f90wrap_csec
end subroutine f90wrap_gen__set__csec

subroutine f90wrap_gen__get__varsat_flow(f90wrap_varsat_flow)
    use gen, only: gen_varsat_flow => varsat_flow
    implicit none
    logical, intent(out) :: f90wrap_varsat_flow
    
    f90wrap_varsat_flow = gen_varsat_flow
end subroutine f90wrap_gen__get__varsat_flow

subroutine f90wrap_gen__set__varsat_flow(f90wrap_varsat_flow)
    use gen, only: gen_varsat_flow => varsat_flow
    implicit none
    logical, intent(in) :: f90wrap_varsat_flow
    
    gen_varsat_flow = f90wrap_varsat_flow
end subroutine f90wrap_gen__set__varsat_flow

subroutine f90wrap_gen__get__steady_flow(f90wrap_steady_flow)
    use gen, only: gen_steady_flow => steady_flow
    implicit none
    logical, intent(out) :: f90wrap_steady_flow
    
    f90wrap_steady_flow = gen_steady_flow
end subroutine f90wrap_gen__get__steady_flow

subroutine f90wrap_gen__set__steady_flow(f90wrap_steady_flow)
    use gen, only: gen_steady_flow => steady_flow
    implicit none
    logical, intent(in) :: f90wrap_steady_flow
    
    gen_steady_flow = f90wrap_steady_flow
end subroutine f90wrap_gen__set__steady_flow

subroutine f90wrap_gen__get__transient_flow(f90wrap_transient_flow)
    use gen, only: gen_transient_flow => transient_flow
    implicit none
    logical, intent(out) :: f90wrap_transient_flow
    
    f90wrap_transient_flow = gen_transient_flow
end subroutine f90wrap_gen__get__transient_flow

subroutine f90wrap_gen__set__transient_flow(f90wrap_transient_flow)
    use gen, only: gen_transient_flow => transient_flow
    implicit none
    logical, intent(in) :: f90wrap_transient_flow
    
    gen_transient_flow = f90wrap_transient_flow
end subroutine f90wrap_gen__set__transient_flow

subroutine f90wrap_gen__get__not_converged(f90wrap_not_converged)
    use gen, only: gen_not_converged => not_converged
    implicit none
    logical, intent(out) :: f90wrap_not_converged
    
    f90wrap_not_converged = gen_not_converged
end subroutine f90wrap_gen__get__not_converged

subroutine f90wrap_gen__set__not_converged(f90wrap_not_converged)
    use gen, only: gen_not_converged => not_converged
    implicit none
    logical, intent(in) :: f90wrap_not_converged
    
    gen_not_converged = f90wrap_not_converged
end subroutine f90wrap_gen__set__not_converged

subroutine f90wrap_gen__get__full_path(f90wrap_full_path)
    use gen, only: gen_full_path => full_path
    implicit none
    logical, intent(out) :: f90wrap_full_path
    
    f90wrap_full_path = gen_full_path
end subroutine f90wrap_gen__get__full_path

subroutine f90wrap_gen__set__full_path(f90wrap_full_path)
    use gen, only: gen_full_path => full_path
    implicit none
    logical, intent(in) :: f90wrap_full_path
    
    gen_full_path = f90wrap_full_path
end subroutine f90wrap_gen__set__full_path

subroutine f90wrap_gen__get__fully_saturated(f90wrap_fully_saturated)
    use gen, only: gen_fully_saturated => fully_saturated
    implicit none
    logical, intent(out) :: f90wrap_fully_saturated
    
    f90wrap_fully_saturated = gen_fully_saturated
end subroutine f90wrap_gen__get__fully_saturated

subroutine f90wrap_gen__set__fully_saturated(f90wrap_fully_saturated)
    use gen, only: gen_fully_saturated => fully_saturated
    implicit none
    logical, intent(in) :: f90wrap_fully_saturated
    
    gen_fully_saturated = f90wrap_fully_saturated
end subroutine f90wrap_gen__set__fully_saturated

subroutine f90wrap_gen__get__variably_saturated(f90wrap_variably_saturated)
    use gen, only: gen_variably_saturated => variably_saturated
    implicit none
    logical, intent(out) :: f90wrap_variably_saturated
    
    f90wrap_variably_saturated = gen_variably_saturated
end subroutine f90wrap_gen__get__variably_saturated

subroutine f90wrap_gen__set__variably_saturated(f90wrap_variably_saturated)
    use gen, only: gen_variably_saturated => variably_saturated
    implicit none
    logical, intent(in) :: f90wrap_variably_saturated
    
    gen_variably_saturated = f90wrap_variably_saturated
end subroutine f90wrap_gen__set__variably_saturated

subroutine f90wrap_gen__get__geo_chemistry(f90wrap_geo_chemistry)
    use gen, only: gen_geo_chemistry => geo_chemistry
    implicit none
    logical, intent(out) :: f90wrap_geo_chemistry
    
    f90wrap_geo_chemistry = gen_geo_chemistry
end subroutine f90wrap_gen__get__geo_chemistry

subroutine f90wrap_gen__set__geo_chemistry(f90wrap_geo_chemistry)
    use gen, only: gen_geo_chemistry => geo_chemistry
    implicit none
    logical, intent(in) :: f90wrap_geo_chemistry
    
    gen_geo_chemistry = f90wrap_geo_chemistry
end subroutine f90wrap_gen__set__geo_chemistry

subroutine f90wrap_gen__get__reactive_transport(f90wrap_reactive_transport)
    use gen, only: gen_reactive_transport => reactive_transport
    implicit none
    logical, intent(out) :: f90wrap_reactive_transport
    
    f90wrap_reactive_transport = gen_reactive_transport
end subroutine f90wrap_gen__get__reactive_transport

subroutine f90wrap_gen__set__reactive_transport(f90wrap_reactive_transport)
    use gen, only: gen_reactive_transport => reactive_transport
    implicit none
    logical, intent(in) :: f90wrap_reactive_transport
    
    gen_reactive_transport = f90wrap_reactive_transport
end subroutine f90wrap_gen__set__reactive_transport

subroutine f90wrap_gen__get__show_module(f90wrap_show_module)
    use gen, only: gen_show_module => show_module
    implicit none
    logical, intent(out) :: f90wrap_show_module
    
    f90wrap_show_module = gen_show_module
end subroutine f90wrap_gen__get__show_module

subroutine f90wrap_gen__set__show_module(f90wrap_show_module)
    use gen, only: gen_show_module => show_module
    implicit none
    logical, intent(in) :: f90wrap_show_module
    
    gen_show_module = f90wrap_show_module
end subroutine f90wrap_gen__set__show_module

subroutine f90wrap_gen__get__log_file(f90wrap_log_file)
    use gen, only: gen_log_file => log_file
    implicit none
    logical, intent(out) :: f90wrap_log_file
    
    f90wrap_log_file = gen_log_file
end subroutine f90wrap_gen__get__log_file

subroutine f90wrap_gen__set__log_file(f90wrap_log_file)
    use gen, only: gen_log_file => log_file
    implicit none
    logical, intent(in) :: f90wrap_log_file
    
    gen_log_file = f90wrap_log_file
end subroutine f90wrap_gen__set__log_file

subroutine f90wrap_gen__get__depth_output(f90wrap_depth_output)
    use gen, only: gen_depth_output => depth_output
    implicit none
    logical, intent(out) :: f90wrap_depth_output
    
    f90wrap_depth_output = gen_depth_output
end subroutine f90wrap_gen__get__depth_output

subroutine f90wrap_gen__set__depth_output(f90wrap_depth_output)
    use gen, only: gen_depth_output => depth_output
    implicit none
    logical, intent(in) :: f90wrap_depth_output
    
    gen_depth_output = f90wrap_depth_output
end subroutine f90wrap_gen__set__depth_output

subroutine f90wrap_gen__get__update_porosity(f90wrap_update_porosity)
    use gen, only: gen_update_porosity => update_porosity
    implicit none
    logical, intent(out) :: f90wrap_update_porosity
    
    f90wrap_update_porosity = gen_update_porosity
end subroutine f90wrap_gen__get__update_porosity

subroutine f90wrap_gen__set__update_porosity(f90wrap_update_porosity)
    use gen, only: gen_update_porosity => update_porosity
    implicit none
    logical, intent(in) :: f90wrap_update_porosity
    
    gen_update_porosity = f90wrap_update_porosity
end subroutine f90wrap_gen__set__update_porosity

subroutine f90wrap_gen__get__update_permeability(f90wrap_update_permeability)
    use gen, only: gen_update_permeability => update_permeability
    implicit none
    logical, intent(out) :: f90wrap_update_permeability
    
    f90wrap_update_permeability = gen_update_permeability
end subroutine f90wrap_gen__get__update_permeability

subroutine f90wrap_gen__set__update_permeability(f90wrap_update_permeability)
    use gen, only: gen_update_permeability => update_permeability
    implicit none
    logical, intent(in) :: f90wrap_update_permeability
    
    gen_update_permeability = f90wrap_update_permeability
end subroutine f90wrap_gen__set__update_permeability

subroutine f90wrap_gen__get__pure_evap(f90wrap_pure_evap)
    use gen, only: gen_pure_evap => pure_evap
    implicit none
    logical, intent(out) :: f90wrap_pure_evap
    
    f90wrap_pure_evap = gen_pure_evap
end subroutine f90wrap_gen__get__pure_evap

subroutine f90wrap_gen__set__pure_evap(f90wrap_pure_evap)
    use gen, only: gen_pure_evap => pure_evap
    implicit none
    logical, intent(in) :: f90wrap_pure_evap
    
    gen_pure_evap = f90wrap_pure_evap
end subroutine f90wrap_gen__set__pure_evap

subroutine f90wrap_gen__get__sec_per_days(f90wrap_sec_per_days)
    use gen, only: gen_sec_per_days => sec_per_days
    implicit none
    real(8), intent(out) :: f90wrap_sec_per_days
    
    f90wrap_sec_per_days = gen_sec_per_days
end subroutine f90wrap_gen__get__sec_per_days

subroutine f90wrap_gen__set__sec_per_days(f90wrap_sec_per_days)
    use gen, only: gen_sec_per_days => sec_per_days
    implicit none
    real(8), intent(in) :: f90wrap_sec_per_days
    
    gen_sec_per_days = f90wrap_sec_per_days
end subroutine f90wrap_gen__set__sec_per_days

subroutine f90wrap_gen__get__gacc(f90wrap_gacc)
    use gen, only: gen_gacc => gacc
    implicit none
    real(8), intent(out) :: f90wrap_gacc
    
    f90wrap_gacc = gen_gacc
end subroutine f90wrap_gen__get__gacc

subroutine f90wrap_gen__set__gacc(f90wrap_gacc)
    use gen, only: gen_gacc => gacc
    implicit none
    real(8), intent(in) :: f90wrap_gacc
    
    gen_gacc = f90wrap_gacc
end subroutine f90wrap_gen__set__gacc

subroutine f90wrap_gen__array__xg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_xg => xg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_xg)) then
        dshape(1:1) = shape(gen_xg)
        dloc = loc(gen_xg)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__xg

subroutine f90wrap_gen__array__yg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_yg => yg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_yg)) then
        dshape(1:1) = shape(gen_yg)
        dloc = loc(gen_yg)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__yg

subroutine f90wrap_gen__array__zg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_zg => zg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_zg)) then
        dshape(1:1) = shape(gen_zg)
        dloc = loc(gen_zg)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__zg

subroutine f90wrap_gen__array__dimcv(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dimcv => dimcv
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_dimcv)) then
        dshape(1:2) = shape(gen_dimcv)
        dloc = loc(gen_dimcv)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dimcv

subroutine f90wrap_gen__array__cvol(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cvol => cvol
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cvol)) then
        dshape(1:1) = shape(gen_cvol)
        dloc = loc(gen_cvol)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cvol

subroutine f90wrap_gen__array__delx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_delx => delx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_delx)) then
        dshape(1:1) = shape(gen_delx)
        dloc = loc(gen_delx)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__delx

subroutine f90wrap_gen__array__dely(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dely => dely
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_dely)) then
        dshape(1:1) = shape(gen_dely)
        dloc = loc(gen_dely)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dely

subroutine f90wrap_gen__array__delz(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_delz => delz
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_delz)) then
        dshape(1:1) = shape(gen_delz)
        dloc = loc(gen_delz)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__delz

subroutine f90wrap_gen__array__xmax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_xmax => xmax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_xmax)) then
        dshape(1:1) = shape(gen_xmax)
        dloc = loc(gen_xmax)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__xmax

subroutine f90wrap_gen__array__xmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_xmin => xmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_xmin)) then
        dshape(1:1) = shape(gen_xmin)
        dloc = loc(gen_xmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__xmin

subroutine f90wrap_gen__array__ymax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ymax => ymax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_ymax)) then
        dshape(1:1) = shape(gen_ymax)
        dloc = loc(gen_ymax)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ymax

subroutine f90wrap_gen__array__ymin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ymin => ymin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_ymin)) then
        dshape(1:1) = shape(gen_ymin)
        dloc = loc(gen_ymin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ymin

subroutine f90wrap_gen__array__zmax(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_zmax => zmax
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_zmax)) then
        dshape(1:1) = shape(gen_zmax)
        dloc = loc(gen_zmax)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__zmax

subroutine f90wrap_gen__array__zmin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_zmin => zmin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(gen_zmin)) then
        dshape(1:1) = shape(gen_zmin)
        dloc = loc(gen_zmin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__zmin

subroutine f90wrap_gen__get__elevmax(f90wrap_elevmax)
    use gen, only: gen_elevmax => elevmax
    implicit none
    real(8), intent(out) :: f90wrap_elevmax
    
    f90wrap_elevmax = gen_elevmax
end subroutine f90wrap_gen__get__elevmax

subroutine f90wrap_gen__set__elevmax(f90wrap_elevmax)
    use gen, only: gen_elevmax => elevmax
    implicit none
    real(8), intent(in) :: f90wrap_elevmax
    
    gen_elevmax = f90wrap_elevmax
end subroutine f90wrap_gen__set__elevmax

subroutine f90wrap_gen__get__toparea(f90wrap_toparea)
    use gen, only: gen_toparea => toparea
    implicit none
    real(8), intent(out) :: f90wrap_toparea
    
    f90wrap_toparea = gen_toparea
end subroutine f90wrap_gen__get__toparea

subroutine f90wrap_gen__set__toparea(f90wrap_toparea)
    use gen, only: gen_toparea => toparea
    implicit none
    real(8), intent(in) :: f90wrap_toparea
    
    gen_toparea = f90wrap_toparea
end subroutine f90wrap_gen__set__toparea

subroutine f90wrap_gen__array__nvix(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_nvix => nvix
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_nvix)) then
        dshape(1:1) = shape(gen_nvix)
        dloc = loc(gen_nvix)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__nvix

subroutine f90wrap_gen__array__nviy(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_nviy => nviy
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_nviy)) then
        dshape(1:1) = shape(gen_nviy)
        dloc = loc(gen_nviy)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__nviy

subroutine f90wrap_gen__array__nviz(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_nviz => nviz
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_nviz)) then
        dshape(1:1) = shape(gen_nviz)
        dloc = loc(gen_nviz)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__nviz

subroutine f90wrap_gen__get__nxx(f90wrap_nxx)
    use gen, only: gen_nxx => nxx
    implicit none
    integer(4), intent(out) :: f90wrap_nxx
    
    f90wrap_nxx = gen_nxx
end subroutine f90wrap_gen__get__nxx

subroutine f90wrap_gen__set__nxx(f90wrap_nxx)
    use gen, only: gen_nxx => nxx
    implicit none
    integer(4), intent(in) :: f90wrap_nxx
    
    gen_nxx = f90wrap_nxx
end subroutine f90wrap_gen__set__nxx

subroutine f90wrap_gen__get__nyy(f90wrap_nyy)
    use gen, only: gen_nyy => nyy
    implicit none
    integer(4), intent(out) :: f90wrap_nyy
    
    f90wrap_nyy = gen_nyy
end subroutine f90wrap_gen__get__nyy

subroutine f90wrap_gen__set__nyy(f90wrap_nyy)
    use gen, only: gen_nyy => nyy
    implicit none
    integer(4), intent(in) :: f90wrap_nyy
    
    gen_nyy = f90wrap_nyy
end subroutine f90wrap_gen__set__nyy

subroutine f90wrap_gen__get__nzz(f90wrap_nzz)
    use gen, only: gen_nzz => nzz
    implicit none
    integer(4), intent(out) :: f90wrap_nzz
    
    f90wrap_nzz = gen_nzz
end subroutine f90wrap_gen__get__nzz

subroutine f90wrap_gen__set__nzz(f90wrap_nzz)
    use gen, only: gen_nzz => nzz
    implicit none
    integer(4), intent(in) :: f90wrap_nzz
    
    gen_nzz = f90wrap_nzz
end subroutine f90wrap_gen__set__nzz

subroutine f90wrap_gen__get__nvx(f90wrap_nvx)
    use gen, only: gen_nvx => nvx
    implicit none
    integer(4), intent(out) :: f90wrap_nvx
    
    f90wrap_nvx = gen_nvx
end subroutine f90wrap_gen__get__nvx

subroutine f90wrap_gen__set__nvx(f90wrap_nvx)
    use gen, only: gen_nvx => nvx
    implicit none
    integer(4), intent(in) :: f90wrap_nvx
    
    gen_nvx = f90wrap_nvx
end subroutine f90wrap_gen__set__nvx

subroutine f90wrap_gen__get__nvy(f90wrap_nvy)
    use gen, only: gen_nvy => nvy
    implicit none
    integer(4), intent(out) :: f90wrap_nvy
    
    f90wrap_nvy = gen_nvy
end subroutine f90wrap_gen__get__nvy

subroutine f90wrap_gen__set__nvy(f90wrap_nvy)
    use gen, only: gen_nvy => nvy
    implicit none
    integer(4), intent(in) :: f90wrap_nvy
    
    gen_nvy = f90wrap_nvy
end subroutine f90wrap_gen__set__nvy

subroutine f90wrap_gen__get__nvz(f90wrap_nvz)
    use gen, only: gen_nvz => nvz
    implicit none
    integer(4), intent(out) :: f90wrap_nvz
    
    f90wrap_nvz = gen_nvz
end subroutine f90wrap_gen__get__nvz

subroutine f90wrap_gen__set__nvz(f90wrap_nvz)
    use gen, only: gen_nvz => nvz
    implicit none
    integer(4), intent(in) :: f90wrap_nvz
    
    gen_nvz = f90wrap_nvz
end subroutine f90wrap_gen__set__nvz

subroutine f90wrap_gen__get__nn(f90wrap_nn)
    use gen, only: gen_nn => nn
    implicit none
    integer(4), intent(out) :: f90wrap_nn
    
    f90wrap_nn = gen_nn
end subroutine f90wrap_gen__get__nn

subroutine f90wrap_gen__set__nn(f90wrap_nn)
    use gen, only: gen_nn => nn
    implicit none
    integer(4), intent(in) :: f90wrap_nn
    
    gen_nn = f90wrap_nn
end subroutine f90wrap_gen__set__nn

subroutine f90wrap_gen__get__half_cells(f90wrap_half_cells)
    use gen, only: gen_half_cells => half_cells
    implicit none
    logical, intent(out) :: f90wrap_half_cells
    
    f90wrap_half_cells = gen_half_cells
end subroutine f90wrap_gen__get__half_cells

subroutine f90wrap_gen__set__half_cells(f90wrap_half_cells)
    use gen, only: gen_half_cells => half_cells
    implicit none
    logical, intent(in) :: f90wrap_half_cells
    
    gen_half_cells = f90wrap_half_cells
end subroutine f90wrap_gen__set__half_cells

subroutine f90wrap_gen__array__delta_c(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_delta_c => delta_c
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_delta_c)) then
        dshape(1:1) = shape(gen_delta_c)
        dloc = loc(gen_delta_c)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__delta_c

subroutine f90wrap_gen__array__delta_c_max(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_delta_c_max => delta_c_max
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_delta_c_max)) then
        dshape(1:1) = shape(gen_delta_c_max)
        dloc = loc(gen_delta_c_max)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__delta_c_max

subroutine f90wrap_gen__get__time(f90wrap_time)
    use gen, only: gen_time => time
    implicit none
    real(8), intent(out) :: f90wrap_time
    
    f90wrap_time = gen_time
end subroutine f90wrap_gen__get__time

subroutine f90wrap_gen__set__time(f90wrap_time)
    use gen, only: gen_time => time
    implicit none
    real(8), intent(in) :: f90wrap_time
    
    gen_time = f90wrap_time
end subroutine f90wrap_gen__set__time

subroutine f90wrap_gen__get__time_io(f90wrap_time_io)
    use gen, only: gen_time_io => time_io
    implicit none
    real(8), intent(out) :: f90wrap_time_io
    
    f90wrap_time_io = gen_time_io
end subroutine f90wrap_gen__get__time_io

subroutine f90wrap_gen__set__time_io(f90wrap_time_io)
    use gen, only: gen_time_io => time_io
    implicit none
    real(8), intent(in) :: f90wrap_time_io
    
    gen_time_io = f90wrap_time_io
end subroutine f90wrap_gen__set__time_io

subroutine f90wrap_gen__get__time_io_bis(f90wrap_time_io_bis)
    use gen, only: gen_time_io_bis => time_io_bis
    implicit none
    real(4), intent(out) :: f90wrap_time_io_bis
    
    f90wrap_time_io_bis = gen_time_io_bis
end subroutine f90wrap_gen__get__time_io_bis

subroutine f90wrap_gen__set__time_io_bis(f90wrap_time_io_bis)
    use gen, only: gen_time_io_bis => time_io_bis
    implicit none
    real(4), intent(in) :: f90wrap_time_io_bis
    
    gen_time_io_bis = f90wrap_time_io_bis
end subroutine f90wrap_gen__set__time_io_bis

subroutine f90wrap_gen__get__time_io_prec(f90wrap_time_io_prec)
    use gen, only: gen_time_io_prec => time_io_prec
    implicit none
    real(8), intent(out) :: f90wrap_time_io_prec
    
    f90wrap_time_io_prec = gen_time_io_prec
end subroutine f90wrap_gen__get__time_io_prec

subroutine f90wrap_gen__set__time_io_prec(f90wrap_time_io_prec)
    use gen, only: gen_time_io_prec => time_io_prec
    implicit none
    real(8), intent(in) :: f90wrap_time_io_prec
    
    gen_time_io_prec = f90wrap_time_io_prec
end subroutine f90wrap_gen__set__time_io_prec

subroutine f90wrap_gen__get__time_factor(f90wrap_time_factor)
    use gen, only: gen_time_factor => time_factor
    implicit none
    real(8), intent(out) :: f90wrap_time_factor
    
    f90wrap_time_factor = gen_time_factor
end subroutine f90wrap_gen__get__time_factor

subroutine f90wrap_gen__set__time_factor(f90wrap_time_factor)
    use gen, only: gen_time_factor => time_factor
    implicit none
    real(8), intent(in) :: f90wrap_time_factor
    
    gen_time_factor = f90wrap_time_factor
end subroutine f90wrap_gen__set__time_factor

subroutine f90wrap_gen__get__tfinal(f90wrap_tfinal)
    use gen, only: gen_tfinal => tfinal
    implicit none
    real(8), intent(out) :: f90wrap_tfinal
    
    f90wrap_tfinal = gen_tfinal
end subroutine f90wrap_gen__get__tfinal

subroutine f90wrap_gen__set__tfinal(f90wrap_tfinal)
    use gen, only: gen_tfinal => tfinal
    implicit none
    real(8), intent(in) :: f90wrap_tfinal
    
    gen_tfinal = f90wrap_tfinal
end subroutine f90wrap_gen__set__tfinal

subroutine f90wrap_gen__get__tfinal_bis(f90wrap_tfinal_bis)
    use gen, only: gen_tfinal_bis => tfinal_bis
    implicit none
    integer(4), intent(out) :: f90wrap_tfinal_bis
    
    f90wrap_tfinal_bis = gen_tfinal_bis
end subroutine f90wrap_gen__get__tfinal_bis

subroutine f90wrap_gen__set__tfinal_bis(f90wrap_tfinal_bis)
    use gen, only: gen_tfinal_bis => tfinal_bis
    implicit none
    integer(4), intent(in) :: f90wrap_tfinal_bis
    
    gen_tfinal_bis = f90wrap_tfinal_bis
end subroutine f90wrap_gen__set__tfinal_bis

subroutine f90wrap_gen__get__delt(f90wrap_delt)
    use gen, only: gen_delt => delt
    implicit none
    real(8), intent(out) :: f90wrap_delt
    
    f90wrap_delt = gen_delt
end subroutine f90wrap_gen__get__delt

subroutine f90wrap_gen__set__delt(f90wrap_delt)
    use gen, only: gen_delt => delt
    implicit none
    real(8), intent(in) :: f90wrap_delt
    
    gen_delt = f90wrap_delt
end subroutine f90wrap_gen__set__delt

subroutine f90wrap_gen__get__delt_io(f90wrap_delt_io)
    use gen, only: gen_delt_io => delt_io
    implicit none
    real(8), intent(out) :: f90wrap_delt_io
    
    f90wrap_delt_io = gen_delt_io
end subroutine f90wrap_gen__get__delt_io

subroutine f90wrap_gen__set__delt_io(f90wrap_delt_io)
    use gen, only: gen_delt_io => delt_io
    implicit none
    real(8), intent(in) :: f90wrap_delt_io
    
    gen_delt_io = f90wrap_delt_io
end subroutine f90wrap_gen__set__delt_io

subroutine f90wrap_gen__get__delt_vs(f90wrap_delt_vs)
    use gen, only: gen_delt_vs => delt_vs
    implicit none
    real(8), intent(out) :: f90wrap_delt_vs
    
    f90wrap_delt_vs = gen_delt_vs
end subroutine f90wrap_gen__get__delt_vs

subroutine f90wrap_gen__set__delt_vs(f90wrap_delt_vs)
    use gen, only: gen_delt_vs => delt_vs
    implicit none
    real(8), intent(in) :: f90wrap_delt_vs
    
    gen_delt_vs = f90wrap_delt_vs
end subroutine f90wrap_gen__set__delt_vs

subroutine f90wrap_gen__get__delt_rt(f90wrap_delt_rt)
    use gen, only: gen_delt_rt => delt_rt
    implicit none
    real(8), intent(out) :: f90wrap_delt_rt
    
    f90wrap_delt_rt = gen_delt_rt
end subroutine f90wrap_gen__get__delt_rt

subroutine f90wrap_gen__set__delt_rt(f90wrap_delt_rt)
    use gen, only: gen_delt_rt => delt_rt
    implicit none
    real(8), intent(in) :: f90wrap_delt_rt
    
    gen_delt_rt = f90wrap_delt_rt
end subroutine f90wrap_gen__set__delt_rt

subroutine f90wrap_gen__get__deltmin(f90wrap_deltmin)
    use gen, only: gen_deltmin => deltmin
    implicit none
    real(8), intent(out) :: f90wrap_deltmin
    
    f90wrap_deltmin = gen_deltmin
end subroutine f90wrap_gen__get__deltmin

subroutine f90wrap_gen__set__deltmin(f90wrap_deltmin)
    use gen, only: gen_deltmin => deltmin
    implicit none
    real(8), intent(in) :: f90wrap_deltmin
    
    gen_deltmin = f90wrap_deltmin
end subroutine f90wrap_gen__set__deltmin

subroutine f90wrap_gen__get__deltmax(f90wrap_deltmax)
    use gen, only: gen_deltmax => deltmax
    implicit none
    real(8), intent(out) :: f90wrap_deltmax
    
    f90wrap_deltmax = gen_deltmax
end subroutine f90wrap_gen__get__deltmax

subroutine f90wrap_gen__set__deltmax(f90wrap_deltmax)
    use gen, only: gen_deltmax => deltmax
    implicit none
    real(8), intent(in) :: f90wrap_deltmax
    
    gen_deltmax = f90wrap_deltmax
end subroutine f90wrap_gen__set__deltmax

subroutine f90wrap_gen__get__urtant_log(f90wrap_urtant_log)
    use gen, only: gen_urtant_log => urtant_log
    implicit none
    real(8), intent(out) :: f90wrap_urtant_log
    
    f90wrap_urtant_log = gen_urtant_log
end subroutine f90wrap_gen__get__urtant_log

subroutine f90wrap_gen__set__urtant_log(f90wrap_urtant_log)
    use gen, only: gen_urtant_log => urtant_log
    implicit none
    real(8), intent(in) :: f90wrap_urtant_log
    
    gen_urtant_log = f90wrap_urtant_log
end subroutine f90wrap_gen__set__urtant_log

subroutine f90wrap_gen__get__l_time_unit(f90wrap_l_time_unit)
    use gen, only: gen_l_time_unit => l_time_unit
    implicit none
    integer(4), intent(out) :: f90wrap_l_time_unit
    
    f90wrap_l_time_unit = gen_l_time_unit
end subroutine f90wrap_gen__get__l_time_unit

subroutine f90wrap_gen__set__l_time_unit(f90wrap_l_time_unit)
    use gen, only: gen_l_time_unit => l_time_unit
    implicit none
    integer(4), intent(in) :: f90wrap_l_time_unit
    
    gen_l_time_unit = f90wrap_l_time_unit
end subroutine f90wrap_gen__set__l_time_unit

subroutine f90wrap_gen__get__mtime(f90wrap_mtime)
    use gen, only: gen_mtime => mtime
    implicit none
    integer(4), intent(out) :: f90wrap_mtime
    
    f90wrap_mtime = gen_mtime
end subroutine f90wrap_gen__get__mtime

subroutine f90wrap_gen__set__mtime(f90wrap_mtime)
    use gen, only: gen_mtime => mtime
    implicit none
    integer(4), intent(in) :: f90wrap_mtime
    
    gen_mtime = f90wrap_mtime
end subroutine f90wrap_gen__set__mtime

subroutine f90wrap_gen__get__mtime_f(f90wrap_mtime_f)
    use gen, only: gen_mtime_f => mtime_f
    implicit none
    integer(4), intent(out) :: f90wrap_mtime_f
    
    f90wrap_mtime_f = gen_mtime_f
end subroutine f90wrap_gen__get__mtime_f

subroutine f90wrap_gen__set__mtime_f(f90wrap_mtime_f)
    use gen, only: gen_mtime_f => mtime_f
    implicit none
    integer(4), intent(in) :: f90wrap_mtime_f
    
    gen_mtime_f = f90wrap_mtime_f
end subroutine f90wrap_gen__set__mtime_f

subroutine f90wrap_gen__get__reduce_timestep(f90wrap_reduce_timestep)
    use gen, only: gen_reduce_timestep => reduce_timestep
    implicit none
    logical, intent(out) :: f90wrap_reduce_timestep
    
    f90wrap_reduce_timestep = gen_reduce_timestep
end subroutine f90wrap_gen__get__reduce_timestep

subroutine f90wrap_gen__set__reduce_timestep(f90wrap_reduce_timestep)
    use gen, only: gen_reduce_timestep => reduce_timestep
    implicit none
    logical, intent(in) :: f90wrap_reduce_timestep
    
    gen_reduce_timestep = f90wrap_reduce_timestep
end subroutine f90wrap_gen__set__reduce_timestep

subroutine f90wrap_gen__array__gs_tout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gs_tout => gs_tout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gs_tout)) then
        dshape(1:1) = shape(gen_gs_tout)
        dloc = loc(gen_gs_tout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gs_tout

subroutine f90wrap_gen__array__iamb(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iamb => iamb
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iamb)) then
        dshape(1:1) = shape(gen_iamb)
        dloc = loc(gen_iamb)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iamb

subroutine f90wrap_gen__array__ngb_vol(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ngb_vol => ngb_vol
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_ngb_vol)) then
        dshape(1:1) = shape(gen_ngb_vol)
        dloc = loc(gen_ngb_vol)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ngb_vol

subroutine f90wrap_gen__get__ngb(f90wrap_ngb)
    use gen, only: gen_ngb => ngb
    implicit none
    integer(4), intent(out) :: f90wrap_ngb
    
    f90wrap_ngb = gen_ngb
end subroutine f90wrap_gen__get__ngb

subroutine f90wrap_gen__set__ngb(f90wrap_ngb)
    use gen, only: gen_ngb => ngb
    implicit none
    integer(4), intent(in) :: f90wrap_ngb
    
    gen_ngb = f90wrap_ngb
end subroutine f90wrap_gen__set__ngb

subroutine f90wrap_gen__get__ngs(f90wrap_ngs)
    use gen, only: gen_ngs => ngs
    implicit none
    integer(4), intent(out) :: f90wrap_ngs
    
    f90wrap_ngs = gen_ngs
end subroutine f90wrap_gen__get__ngs

subroutine f90wrap_gen__set__ngs(f90wrap_ngs)
    use gen, only: gen_ngs => ngs
    implicit none
    integer(4), intent(in) :: f90wrap_ngs
    
    gen_ngs = f90wrap_ngs
end subroutine f90wrap_gen__set__ngs

subroutine f90wrap_gen__get__igstime(f90wrap_igstime)
    use gen, only: gen_igstime => igstime
    implicit none
    integer(4), intent(out) :: f90wrap_igstime
    
    f90wrap_igstime = gen_igstime
end subroutine f90wrap_gen__get__igstime

subroutine f90wrap_gen__set__igstime(f90wrap_igstime)
    use gen, only: gen_igstime => igstime
    implicit none
    integer(4), intent(in) :: f90wrap_igstime
    
    gen_igstime = f90wrap_igstime
end subroutine f90wrap_gen__set__igstime

subroutine f90wrap_gen__get__ngb_step(f90wrap_ngb_step)
    use gen, only: gen_ngb_step => ngb_step
    implicit none
    integer(4), intent(out) :: f90wrap_ngb_step
    
    f90wrap_ngb_step = gen_ngb_step
end subroutine f90wrap_gen__get__ngb_step

subroutine f90wrap_gen__set__ngb_step(f90wrap_ngb_step)
    use gen, only: gen_ngb_step => ngb_step
    implicit none
    integer(4), intent(in) :: f90wrap_ngb_step
    
    gen_ngb_step = f90wrap_ngb_step
end subroutine f90wrap_gen__set__ngb_step

subroutine f90wrap_gen__get__nmb(f90wrap_nmb)
    use gen, only: gen_nmb => nmb
    implicit none
    integer(4), intent(out) :: f90wrap_nmb
    
    f90wrap_nmb = gen_nmb
end subroutine f90wrap_gen__get__nmb

subroutine f90wrap_gen__set__nmb(f90wrap_nmb)
    use gen, only: gen_nmb => nmb
    implicit none
    integer(4), intent(in) :: f90wrap_nmb
    
    gen_nmb = f90wrap_nmb
end subroutine f90wrap_gen__set__nmb

subroutine f90wrap_gen__get__l_prfx(f90wrap_l_prfx)
    use gen, only: gen_l_prfx => l_prfx
    implicit none
    integer(4), intent(out) :: f90wrap_l_prfx
    
    f90wrap_l_prfx = gen_l_prfx
end subroutine f90wrap_gen__get__l_prfx

subroutine f90wrap_gen__set__l_prfx(f90wrap_l_prfx)
    use gen, only: gen_l_prfx => l_prfx
    implicit none
    integer(4), intent(in) :: f90wrap_l_prfx
    
    gen_l_prfx = f90wrap_l_prfx
end subroutine f90wrap_gen__set__l_prfx

subroutine f90wrap_gen__get__l_dbs_dir(f90wrap_l_dbs_dir)
    use gen, only: gen_l_dbs_dir => l_dbs_dir
    implicit none
    integer(4), intent(out) :: f90wrap_l_dbs_dir
    
    f90wrap_l_dbs_dir = gen_l_dbs_dir
end subroutine f90wrap_gen__get__l_dbs_dir

subroutine f90wrap_gen__set__l_dbs_dir(f90wrap_l_dbs_dir)
    use gen, only: gen_l_dbs_dir => l_dbs_dir
    implicit none
    integer(4), intent(in) :: f90wrap_l_dbs_dir
    
    gen_l_dbs_dir = f90wrap_l_dbs_dir
end subroutine f90wrap_gen__set__l_dbs_dir

subroutine f90wrap_gen__get__idat(f90wrap_idat)
    use gen, only: gen_idat => idat
    implicit none
    integer(4), intent(out) :: f90wrap_idat
    
    f90wrap_idat = gen_idat
end subroutine f90wrap_gen__get__idat

subroutine f90wrap_gen__set__idat(f90wrap_idat)
    use gen, only: gen_idat => idat
    implicit none
    integer(4), intent(in) :: f90wrap_idat
    
    gen_idat = f90wrap_idat
end subroutine f90wrap_gen__set__idat

subroutine f90wrap_gen__get__igen(f90wrap_igen)
    use gen, only: gen_igen => igen
    implicit none
    integer(4), intent(out) :: f90wrap_igen
    
    f90wrap_igen = gen_igen
end subroutine f90wrap_gen__get__igen

subroutine f90wrap_gen__set__igen(f90wrap_igen)
    use gen, only: gen_igen => igen
    implicit none
    integer(4), intent(in) :: f90wrap_igen
    
    gen_igen = f90wrap_igen
end subroutine f90wrap_gen__set__igen

subroutine f90wrap_gen__get__ifls(f90wrap_ifls)
    use gen, only: gen_ifls => ifls
    implicit none
    integer(4), intent(out) :: f90wrap_ifls
    
    f90wrap_ifls = gen_ifls
end subroutine f90wrap_gen__get__ifls

subroutine f90wrap_gen__set__ifls(f90wrap_ifls)
    use gen, only: gen_ifls => ifls
    implicit none
    integer(4), intent(in) :: f90wrap_ifls
    
    gen_ifls = f90wrap_ifls
end subroutine f90wrap_gen__set__ifls

subroutine f90wrap_gen__get__idbg(f90wrap_idbg)
    use gen, only: gen_idbg => idbg
    implicit none
    integer(4), intent(out) :: f90wrap_idbg
    
    f90wrap_idbg = gen_idbg
end subroutine f90wrap_gen__get__idbg

subroutine f90wrap_gen__set__idbg(f90wrap_idbg)
    use gen, only: gen_idbg => idbg
    implicit none
    integer(4), intent(in) :: f90wrap_idbg
    
    gen_idbg = f90wrap_idbg
end subroutine f90wrap_gen__set__idbg

subroutine f90wrap_gen__get__ilog(f90wrap_ilog)
    use gen, only: gen_ilog => ilog
    implicit none
    integer(4), intent(out) :: f90wrap_ilog
    
    f90wrap_ilog = gen_ilog
end subroutine f90wrap_gen__get__ilog

subroutine f90wrap_gen__set__ilog(f90wrap_ilog)
    use gen, only: gen_ilog => ilog
    implicit none
    integer(4), intent(in) :: f90wrap_ilog
    
    gen_ilog = f90wrap_ilog
end subroutine f90wrap_gen__set__ilog

subroutine f90wrap_gen__get__idelt(f90wrap_idelt)
    use gen, only: gen_idelt => idelt
    implicit none
    integer(4), intent(out) :: f90wrap_idelt
    
    f90wrap_idelt = gen_idelt
end subroutine f90wrap_gen__get__idelt

subroutine f90wrap_gen__set__idelt(f90wrap_idelt)
    use gen, only: gen_idelt => idelt
    implicit none
    integer(4), intent(in) :: f90wrap_idelt
    
    gen_idelt = f90wrap_idelt
end subroutine f90wrap_gen__set__idelt

subroutine f90wrap_gen__get__icnv(f90wrap_icnv)
    use gen, only: gen_icnv => icnv
    implicit none
    integer(4), intent(out) :: f90wrap_icnv
    
    f90wrap_icnv = gen_icnv
end subroutine f90wrap_gen__get__icnv

subroutine f90wrap_gen__set__icnv(f90wrap_icnv)
    use gen, only: gen_icnv => icnv
    implicit none
    integer(4), intent(in) :: f90wrap_icnv
    
    gen_icnv = f90wrap_icnv
end subroutine f90wrap_gen__set__icnv

subroutine f90wrap_gen__get__ihyc(f90wrap_ihyc)
    use gen, only: gen_ihyc => ihyc
    implicit none
    integer(4), intent(out) :: f90wrap_ihyc
    
    f90wrap_ihyc = gen_ihyc
end subroutine f90wrap_gen__get__ihyc

subroutine f90wrap_gen__set__ihyc(f90wrap_ihyc)
    use gen, only: gen_ihyc => ihyc
    implicit none
    integer(4), intent(in) :: f90wrap_ihyc
    
    gen_ihyc = f90wrap_ihyc
end subroutine f90wrap_gen__set__ihyc

subroutine f90wrap_gen__get__itmp(f90wrap_itmp)
    use gen, only: gen_itmp => itmp
    implicit none
    integer(4), intent(out) :: f90wrap_itmp
    
    f90wrap_itmp = gen_itmp
end subroutine f90wrap_gen__get__itmp

subroutine f90wrap_gen__set__itmp(f90wrap_itmp)
    use gen, only: gen_itmp => itmp
    implicit none
    integer(4), intent(in) :: f90wrap_itmp
    
    gen_itmp = f90wrap_itmp
end subroutine f90wrap_gen__set__itmp

subroutine f90wrap_gen__get__ivel(f90wrap_ivel)
    use gen, only: gen_ivel => ivel
    implicit none
    integer(4), intent(out) :: f90wrap_ivel
    
    f90wrap_ivel = gen_ivel
end subroutine f90wrap_gen__get__ivel

subroutine f90wrap_gen__set__ivel(f90wrap_ivel)
    use gen, only: gen_ivel => ivel
    implicit none
    integer(4), intent(in) :: f90wrap_ivel
    
    gen_ivel = f90wrap_ivel
end subroutine f90wrap_gen__set__ivel

subroutine f90wrap_gen__get__icdbs(f90wrap_icdbs)
    use gen, only: gen_icdbs => icdbs
    implicit none
    integer(4), intent(out) :: f90wrap_icdbs
    
    f90wrap_icdbs = gen_icdbs
end subroutine f90wrap_gen__get__icdbs

subroutine f90wrap_gen__set__icdbs(f90wrap_icdbs)
    use gen, only: gen_icdbs => icdbs
    implicit none
    integer(4), intent(in) :: f90wrap_icdbs
    
    gen_icdbs = f90wrap_icdbs
end subroutine f90wrap_gen__set__icdbs

subroutine f90wrap_gen__get__ixdbs(f90wrap_ixdbs)
    use gen, only: gen_ixdbs => ixdbs
    implicit none
    integer(4), intent(out) :: f90wrap_ixdbs
    
    f90wrap_ixdbs = gen_ixdbs
end subroutine f90wrap_gen__get__ixdbs

subroutine f90wrap_gen__set__ixdbs(f90wrap_ixdbs)
    use gen, only: gen_ixdbs => ixdbs
    implicit none
    integer(4), intent(in) :: f90wrap_ixdbs
    
    gen_ixdbs = f90wrap_ixdbs
end subroutine f90wrap_gen__set__ixdbs

subroutine f90wrap_gen__get__imdbs(f90wrap_imdbs)
    use gen, only: gen_imdbs => imdbs
    implicit none
    integer(4), intent(out) :: f90wrap_imdbs
    
    f90wrap_imdbs = gen_imdbs
end subroutine f90wrap_gen__get__imdbs

subroutine f90wrap_gen__set__imdbs(f90wrap_imdbs)
    use gen, only: gen_imdbs => imdbs
    implicit none
    integer(4), intent(in) :: f90wrap_imdbs
    
    gen_imdbs = f90wrap_imdbs
end subroutine f90wrap_gen__set__imdbs

subroutine f90wrap_gen__get__isdbs(f90wrap_isdbs)
    use gen, only: gen_isdbs => isdbs
    implicit none
    integer(4), intent(out) :: f90wrap_isdbs
    
    f90wrap_isdbs = gen_isdbs
end subroutine f90wrap_gen__get__isdbs

subroutine f90wrap_gen__set__isdbs(f90wrap_isdbs)
    use gen, only: gen_isdbs => isdbs
    implicit none
    integer(4), intent(in) :: f90wrap_isdbs
    
    gen_isdbs = f90wrap_isdbs
end subroutine f90wrap_gen__set__isdbs

subroutine f90wrap_gen__get__irdbs(f90wrap_irdbs)
    use gen, only: gen_irdbs => irdbs
    implicit none
    integer(4), intent(out) :: f90wrap_irdbs
    
    f90wrap_irdbs = gen_irdbs
end subroutine f90wrap_gen__get__irdbs

subroutine f90wrap_gen__set__irdbs(f90wrap_irdbs)
    use gen, only: gen_irdbs => irdbs
    implicit none
    integer(4), intent(in) :: f90wrap_irdbs
    
    gen_irdbs = f90wrap_irdbs
end subroutine f90wrap_gen__set__irdbs

subroutine f90wrap_gen__get__igdbs(f90wrap_igdbs)
    use gen, only: gen_igdbs => igdbs
    implicit none
    integer(4), intent(out) :: f90wrap_igdbs
    
    f90wrap_igdbs = gen_igdbs
end subroutine f90wrap_gen__get__igdbs

subroutine f90wrap_gen__set__igdbs(f90wrap_igdbs)
    use gen, only: gen_igdbs => igdbs
    implicit none
    integer(4), intent(in) :: f90wrap_igdbs
    
    gen_igdbs = f90wrap_igdbs
end subroutine f90wrap_gen__set__igdbs

subroutine f90wrap_gen__get__imvs(f90wrap_imvs)
    use gen, only: gen_imvs => imvs
    implicit none
    integer(4), intent(out) :: f90wrap_imvs
    
    f90wrap_imvs = gen_imvs
end subroutine f90wrap_gen__get__imvs

subroutine f90wrap_gen__set__imvs(f90wrap_imvs)
    use gen, only: gen_imvs => imvs
    implicit none
    integer(4), intent(in) :: f90wrap_imvs
    
    gen_imvs = f90wrap_imvs
end subroutine f90wrap_gen__set__imvs

subroutine f90wrap_gen__get__imvs_first(f90wrap_imvs_first)
    use gen, only: gen_imvs_first => imvs_first
    implicit none
    integer(4), intent(out) :: f90wrap_imvs_first
    
    f90wrap_imvs_first = gen_imvs_first
end subroutine f90wrap_gen__get__imvs_first

subroutine f90wrap_gen__set__imvs_first(f90wrap_imvs_first)
    use gen, only: gen_imvs_first => imvs_first
    implicit none
    integer(4), intent(in) :: f90wrap_imvs_first
    
    gen_imvs_first = f90wrap_imvs_first
end subroutine f90wrap_gen__set__imvs_first

subroutine f90wrap_gen__get__imvs_last(f90wrap_imvs_last)
    use gen, only: gen_imvs_last => imvs_last
    implicit none
    integer(4), intent(out) :: f90wrap_imvs_last
    
    f90wrap_imvs_last = gen_imvs_last
end subroutine f90wrap_gen__get__imvs_last

subroutine f90wrap_gen__set__imvs_last(f90wrap_imvs_last)
    use gen, only: gen_imvs_last => imvs_last
    implicit none
    integer(4), intent(in) :: f90wrap_imvs_last
    
    gen_imvs_last = f90wrap_imvs_last
end subroutine f90wrap_gen__set__imvs_last

subroutine f90wrap_gen__get__imrt(f90wrap_imrt)
    use gen, only: gen_imrt => imrt
    implicit none
    integer(4), intent(out) :: f90wrap_imrt
    
    f90wrap_imrt = gen_imrt
end subroutine f90wrap_gen__get__imrt

subroutine f90wrap_gen__set__imrt(f90wrap_imrt)
    use gen, only: gen_imrt => imrt
    implicit none
    integer(4), intent(in) :: f90wrap_imrt
    
    gen_imrt = f90wrap_imrt
end subroutine f90wrap_gen__set__imrt

subroutine f90wrap_gen__get__imrt_first(f90wrap_imrt_first)
    use gen, only: gen_imrt_first => imrt_first
    implicit none
    integer(4), intent(out) :: f90wrap_imrt_first
    
    f90wrap_imrt_first = gen_imrt_first
end subroutine f90wrap_gen__get__imrt_first

subroutine f90wrap_gen__set__imrt_first(f90wrap_imrt_first)
    use gen, only: gen_imrt_first => imrt_first
    implicit none
    integer(4), intent(in) :: f90wrap_imrt_first
    
    gen_imrt_first = f90wrap_imrt_first
end subroutine f90wrap_gen__set__imrt_first

subroutine f90wrap_gen__get__imrt_last(f90wrap_imrt_last)
    use gen, only: gen_imrt_last => imrt_last
    implicit none
    integer(4), intent(out) :: f90wrap_imrt_last
    
    f90wrap_imrt_last = gen_imrt_last
end subroutine f90wrap_gen__get__imrt_last

subroutine f90wrap_gen__set__imrt_last(f90wrap_imrt_last)
    use gen, only: gen_imrt_last => imrt_last
    implicit none
    integer(4), intent(in) :: f90wrap_imrt_last
    
    gen_imrt_last = f90wrap_imrt_last
end subroutine f90wrap_gen__set__imrt_last

subroutine f90wrap_gen__get__igsp(f90wrap_igsp)
    use gen, only: gen_igsp => igsp
    implicit none
    integer(4), intent(out) :: f90wrap_igsp
    
    f90wrap_igsp = gen_igsp
end subroutine f90wrap_gen__get__igsp

subroutine f90wrap_gen__set__igsp(f90wrap_igsp)
    use gen, only: gen_igsp => igsp
    implicit none
    integer(4), intent(in) :: f90wrap_igsp
    
    gen_igsp = f90wrap_igsp
end subroutine f90wrap_gen__set__igsp

subroutine f90wrap_gen__get__igsb(f90wrap_igsb)
    use gen, only: gen_igsb => igsb
    implicit none
    integer(4), intent(out) :: f90wrap_igsb
    
    f90wrap_igsb = gen_igsb
end subroutine f90wrap_gen__get__igsb

subroutine f90wrap_gen__set__igsb(f90wrap_igsb)
    use gen, only: gen_igsb => igsb
    implicit none
    integer(4), intent(in) :: f90wrap_igsb
    
    gen_igsb = f90wrap_igsb
end subroutine f90wrap_gen__set__igsb

subroutine f90wrap_gen__get__igsc(f90wrap_igsc)
    use gen, only: gen_igsc => igsc
    implicit none
    integer(4), intent(out) :: f90wrap_igsc
    
    f90wrap_igsc = gen_igsc
end subroutine f90wrap_gen__get__igsc

subroutine f90wrap_gen__set__igsc(f90wrap_igsc)
    use gen, only: gen_igsc => igsc
    implicit none
    integer(4), intent(in) :: f90wrap_igsc
    
    gen_igsc = f90wrap_igsc
end subroutine f90wrap_gen__set__igsc

subroutine f90wrap_gen__get__igsd(f90wrap_igsd)
    use gen, only: gen_igsd => igsd
    implicit none
    integer(4), intent(out) :: f90wrap_igsd
    
    f90wrap_igsd = gen_igsd
end subroutine f90wrap_gen__get__igsd

subroutine f90wrap_gen__set__igsd(f90wrap_igsd)
    use gen, only: gen_igsd => igsd
    implicit none
    integer(4), intent(in) :: f90wrap_igsd
    
    gen_igsd = f90wrap_igsd
end subroutine f90wrap_gen__set__igsd

subroutine f90wrap_gen__get__igsg(f90wrap_igsg)
    use gen, only: gen_igsg => igsg
    implicit none
    integer(4), intent(out) :: f90wrap_igsg
    
    f90wrap_igsg = gen_igsg
end subroutine f90wrap_gen__get__igsg

subroutine f90wrap_gen__set__igsg(f90wrap_igsg)
    use gen, only: gen_igsg => igsg
    implicit none
    integer(4), intent(in) :: f90wrap_igsg
    
    gen_igsg = f90wrap_igsg
end subroutine f90wrap_gen__set__igsg

subroutine f90wrap_gen__get__igsgr(f90wrap_igsgr)
    use gen, only: gen_igsgr => igsgr
    implicit none
    integer(4), intent(out) :: f90wrap_igsgr
    
    f90wrap_igsgr = gen_igsgr
end subroutine f90wrap_gen__get__igsgr

subroutine f90wrap_gen__set__igsgr(f90wrap_igsgr)
    use gen, only: gen_igsgr => igsgr
    implicit none
    integer(4), intent(in) :: f90wrap_igsgr
    
    gen_igsgr = f90wrap_igsgr
end subroutine f90wrap_gen__set__igsgr

subroutine f90wrap_gen__get__igsm(f90wrap_igsm)
    use gen, only: gen_igsm => igsm
    implicit none
    integer(4), intent(out) :: f90wrap_igsm
    
    f90wrap_igsm = gen_igsm
end subroutine f90wrap_gen__get__igsm

subroutine f90wrap_gen__set__igsm(f90wrap_igsm)
    use gen, only: gen_igsm => igsm
    implicit none
    integer(4), intent(in) :: f90wrap_igsm
    
    gen_igsm = f90wrap_igsm
end subroutine f90wrap_gen__set__igsm

subroutine f90wrap_gen__get__igsi(f90wrap_igsi)
    use gen, only: gen_igsi => igsi
    implicit none
    integer(4), intent(out) :: f90wrap_igsi
    
    f90wrap_igsi = gen_igsi
end subroutine f90wrap_gen__get__igsi

subroutine f90wrap_gen__set__igsi(f90wrap_igsi)
    use gen, only: gen_igsi => igsi
    implicit none
    integer(4), intent(in) :: f90wrap_igsi
    
    gen_igsi = f90wrap_igsi
end subroutine f90wrap_gen__set__igsi

subroutine f90wrap_gen__get__igss(f90wrap_igss)
    use gen, only: gen_igss => igss
    implicit none
    integer(4), intent(out) :: f90wrap_igss
    
    f90wrap_igss = gen_igss
end subroutine f90wrap_gen__get__igss

subroutine f90wrap_gen__set__igss(f90wrap_igss)
    use gen, only: gen_igss => igss
    implicit none
    integer(4), intent(in) :: f90wrap_igss
    
    gen_igss = f90wrap_igss
end subroutine f90wrap_gen__set__igss

subroutine f90wrap_gen__get__igst(f90wrap_igst)
    use gen, only: gen_igst => igst
    implicit none
    integer(4), intent(out) :: f90wrap_igst
    
    f90wrap_igst = gen_igst
end subroutine f90wrap_gen__get__igst

subroutine f90wrap_gen__set__igst(f90wrap_igst)
    use gen, only: gen_igst => igst
    implicit none
    integer(4), intent(in) :: f90wrap_igst
    
    gen_igst = f90wrap_igst
end subroutine f90wrap_gen__set__igst

subroutine f90wrap_gen__get__igsv(f90wrap_igsv)
    use gen, only: gen_igsv => igsv
    implicit none
    integer(4), intent(out) :: f90wrap_igsv
    
    f90wrap_igsv = gen_igsv
end subroutine f90wrap_gen__get__igsv

subroutine f90wrap_gen__set__igsv(f90wrap_igsv)
    use gen, only: gen_igsv => igsv
    implicit none
    integer(4), intent(in) :: f90wrap_igsv
    
    gen_igsv = f90wrap_igsv
end subroutine f90wrap_gen__set__igsv

subroutine f90wrap_gen__get__igsx(f90wrap_igsx)
    use gen, only: gen_igsx => igsx
    implicit none
    integer(4), intent(out) :: f90wrap_igsx
    
    f90wrap_igsx = gen_igsx
end subroutine f90wrap_gen__get__igsx

subroutine f90wrap_gen__set__igsx(f90wrap_igsx)
    use gen, only: gen_igsx => igsx
    implicit none
    integer(4), intent(in) :: f90wrap_igsx
    
    gen_igsx = f90wrap_igsx
end subroutine f90wrap_gen__set__igsx

subroutine f90wrap_gen__get__igb_start(f90wrap_igb_start)
    use gen, only: gen_igb_start => igb_start
    implicit none
    integer(4), intent(out) :: f90wrap_igb_start
    
    f90wrap_igb_start = gen_igb_start
end subroutine f90wrap_gen__get__igb_start

subroutine f90wrap_gen__set__igb_start(f90wrap_igb_start)
    use gen, only: gen_igb_start => igb_start
    implicit none
    integer(4), intent(in) :: f90wrap_igb_start
    
    gen_igb_start = f90wrap_igb_start
end subroutine f90wrap_gen__set__igb_start

subroutine f90wrap_gen__get__igbb(f90wrap_igbb)
    use gen, only: gen_igbb => igbb
    implicit none
    integer(4), intent(out) :: f90wrap_igbb
    
    f90wrap_igbb = gen_igbb
end subroutine f90wrap_gen__get__igbb

subroutine f90wrap_gen__set__igbb(f90wrap_igbb)
    use gen, only: gen_igbb => igbb
    implicit none
    integer(4), intent(in) :: f90wrap_igbb
    
    gen_igbb = f90wrap_igbb
end subroutine f90wrap_gen__set__igbb

subroutine f90wrap_gen__get__igbc(f90wrap_igbc)
    use gen, only: gen_igbc => igbc
    implicit none
    integer(4), intent(out) :: f90wrap_igbc
    
    f90wrap_igbc = gen_igbc
end subroutine f90wrap_gen__get__igbc

subroutine f90wrap_gen__set__igbc(f90wrap_igbc)
    use gen, only: gen_igbc => igbc
    implicit none
    integer(4), intent(in) :: f90wrap_igbc
    
    gen_igbc = f90wrap_igbc
end subroutine f90wrap_gen__set__igbc

subroutine f90wrap_gen__get__igbd(f90wrap_igbd)
    use gen, only: gen_igbd => igbd
    implicit none
    integer(4), intent(out) :: f90wrap_igbd
    
    f90wrap_igbd = gen_igbd
end subroutine f90wrap_gen__get__igbd

subroutine f90wrap_gen__set__igbd(f90wrap_igbd)
    use gen, only: gen_igbd => igbd
    implicit none
    integer(4), intent(in) :: f90wrap_igbd
    
    gen_igbd = f90wrap_igbd
end subroutine f90wrap_gen__set__igbd

subroutine f90wrap_gen__get__igbg(f90wrap_igbg)
    use gen, only: gen_igbg => igbg
    implicit none
    integer(4), intent(out) :: f90wrap_igbg
    
    f90wrap_igbg = gen_igbg
end subroutine f90wrap_gen__get__igbg

subroutine f90wrap_gen__set__igbg(f90wrap_igbg)
    use gen, only: gen_igbg => igbg
    implicit none
    integer(4), intent(in) :: f90wrap_igbg
    
    gen_igbg = f90wrap_igbg
end subroutine f90wrap_gen__set__igbg

subroutine f90wrap_gen__get__igbgr(f90wrap_igbgr)
    use gen, only: gen_igbgr => igbgr
    implicit none
    integer(4), intent(out) :: f90wrap_igbgr
    
    f90wrap_igbgr = gen_igbgr
end subroutine f90wrap_gen__get__igbgr

subroutine f90wrap_gen__set__igbgr(f90wrap_igbgr)
    use gen, only: gen_igbgr => igbgr
    implicit none
    integer(4), intent(in) :: f90wrap_igbgr
    
    gen_igbgr = f90wrap_igbgr
end subroutine f90wrap_gen__set__igbgr

subroutine f90wrap_gen__get__igbm(f90wrap_igbm)
    use gen, only: gen_igbm => igbm
    implicit none
    integer(4), intent(out) :: f90wrap_igbm
    
    f90wrap_igbm = gen_igbm
end subroutine f90wrap_gen__get__igbm

subroutine f90wrap_gen__set__igbm(f90wrap_igbm)
    use gen, only: gen_igbm => igbm
    implicit none
    integer(4), intent(in) :: f90wrap_igbm
    
    gen_igbm = f90wrap_igbm
end subroutine f90wrap_gen__set__igbm

subroutine f90wrap_gen__get__igbp(f90wrap_igbp)
    use gen, only: gen_igbp => igbp
    implicit none
    integer(4), intent(out) :: f90wrap_igbp
    
    f90wrap_igbp = gen_igbp
end subroutine f90wrap_gen__get__igbp

subroutine f90wrap_gen__set__igbp(f90wrap_igbp)
    use gen, only: gen_igbp => igbp
    implicit none
    integer(4), intent(in) :: f90wrap_igbp
    
    gen_igbp = f90wrap_igbp
end subroutine f90wrap_gen__set__igbp

subroutine f90wrap_gen__get__igbi(f90wrap_igbi)
    use gen, only: gen_igbi => igbi
    implicit none
    integer(4), intent(out) :: f90wrap_igbi
    
    f90wrap_igbi = gen_igbi
end subroutine f90wrap_gen__get__igbi

subroutine f90wrap_gen__set__igbi(f90wrap_igbi)
    use gen, only: gen_igbi => igbi
    implicit none
    integer(4), intent(in) :: f90wrap_igbi
    
    gen_igbi = f90wrap_igbi
end subroutine f90wrap_gen__set__igbi

subroutine f90wrap_gen__get__igbs(f90wrap_igbs)
    use gen, only: gen_igbs => igbs
    implicit none
    integer(4), intent(out) :: f90wrap_igbs
    
    f90wrap_igbs = gen_igbs
end subroutine f90wrap_gen__get__igbs

subroutine f90wrap_gen__set__igbs(f90wrap_igbs)
    use gen, only: gen_igbs => igbs
    implicit none
    integer(4), intent(in) :: f90wrap_igbs
    
    gen_igbs = f90wrap_igbs
end subroutine f90wrap_gen__set__igbs

subroutine f90wrap_gen__get__igbt(f90wrap_igbt)
    use gen, only: gen_igbt => igbt
    implicit none
    integer(4), intent(out) :: f90wrap_igbt
    
    f90wrap_igbt = gen_igbt
end subroutine f90wrap_gen__get__igbt

subroutine f90wrap_gen__set__igbt(f90wrap_igbt)
    use gen, only: gen_igbt => igbt
    implicit none
    integer(4), intent(in) :: f90wrap_igbt
    
    gen_igbt = f90wrap_igbt
end subroutine f90wrap_gen__set__igbt

subroutine f90wrap_gen__get__igbv(f90wrap_igbv)
    use gen, only: gen_igbv => igbv
    implicit none
    integer(4), intent(out) :: f90wrap_igbv
    
    f90wrap_igbv = gen_igbv
end subroutine f90wrap_gen__get__igbv

subroutine f90wrap_gen__set__igbv(f90wrap_igbv)
    use gen, only: gen_igbv => igbv
    implicit none
    integer(4), intent(in) :: f90wrap_igbv
    
    gen_igbv = f90wrap_igbv
end subroutine f90wrap_gen__set__igbv

subroutine f90wrap_gen__get__igbx(f90wrap_igbx)
    use gen, only: gen_igbx => igbx
    implicit none
    integer(4), intent(out) :: f90wrap_igbx
    
    f90wrap_igbx = gen_igbx
end subroutine f90wrap_gen__get__igbx

subroutine f90wrap_gen__set__igbx(f90wrap_igbx)
    use gen, only: gen_igbx => igbx
    implicit none
    integer(4), intent(in) :: f90wrap_igbx
    
    gen_igbx = f90wrap_igbx
end subroutine f90wrap_gen__set__igbx

subroutine f90wrap_gen__get__ipsp(f90wrap_ipsp)
    use gen, only: gen_ipsp => ipsp
    implicit none
    integer(4), intent(out) :: f90wrap_ipsp
    
    f90wrap_ipsp = gen_ipsp
end subroutine f90wrap_gen__get__ipsp

subroutine f90wrap_gen__set__ipsp(f90wrap_ipsp)
    use gen, only: gen_ipsp => ipsp
    implicit none
    integer(4), intent(in) :: f90wrap_ipsp
    
    gen_ipsp = f90wrap_ipsp
end subroutine f90wrap_gen__set__ipsp

subroutine f90wrap_gen__get__itec(f90wrap_itec)
    use gen, only: gen_itec => itec
    implicit none
    integer(4), intent(out) :: f90wrap_itec
    
    f90wrap_itec = gen_itec
end subroutine f90wrap_gen__get__itec

subroutine f90wrap_gen__set__itec(f90wrap_itec)
    use gen, only: gen_itec => itec
    implicit none
    integer(4), intent(in) :: f90wrap_itec
    
    gen_itec = f90wrap_itec
end subroutine f90wrap_gen__set__itec

subroutine f90wrap_gen__get__item(f90wrap_item)
    use gen, only: gen_item => item
    implicit none
    integer(4), intent(out) :: f90wrap_item
    
    f90wrap_item = gen_item
end subroutine f90wrap_gen__get__item

subroutine f90wrap_gen__set__item(f90wrap_item)
    use gen, only: gen_item => item
    implicit none
    integer(4), intent(in) :: f90wrap_item
    
    gen_item = f90wrap_item
end subroutine f90wrap_gen__set__item

subroutine f90wrap_gen__get__jtec(f90wrap_jtec)
    use gen, only: gen_jtec => jtec
    implicit none
    integer(4), intent(out) :: f90wrap_jtec
    
    f90wrap_jtec = gen_jtec
end subroutine f90wrap_gen__get__jtec

subroutine f90wrap_gen__set__jtec(f90wrap_jtec)
    use gen, only: gen_jtec => jtec
    implicit none
    integer(4), intent(in) :: f90wrap_jtec
    
    gen_jtec = f90wrap_jtec
end subroutine f90wrap_gen__set__jtec

subroutine f90wrap_gen__get__ktec(f90wrap_ktec)
    use gen, only: gen_ktec => ktec
    implicit none
    integer(4), intent(out) :: f90wrap_ktec
    
    f90wrap_ktec = gen_ktec
end subroutine f90wrap_gen__get__ktec

subroutine f90wrap_gen__set__ktec(f90wrap_ktec)
    use gen, only: gen_ktec => ktec
    implicit none
    integer(4), intent(in) :: f90wrap_ktec
    
    gen_ktec = f90wrap_ktec
end subroutine f90wrap_gen__set__ktec

subroutine f90wrap_gen__get__l_zone_name(f90wrap_l_zone_name)
    use gen, only: gen_l_zone_name => l_zone_name
    implicit none
    integer(4), intent(out) :: f90wrap_l_zone_name
    
    f90wrap_l_zone_name = gen_l_zone_name
end subroutine f90wrap_gen__get__l_zone_name

subroutine f90wrap_gen__set__l_zone_name(f90wrap_l_zone_name)
    use gen, only: gen_l_zone_name => l_zone_name
    implicit none
    integer(4), intent(in) :: f90wrap_l_zone_name
    
    gen_l_zone_name = f90wrap_l_zone_name
end subroutine f90wrap_gen__set__l_zone_name

subroutine f90wrap_gen__get__igsa(f90wrap_igsa)
    use gen, only: gen_igsa => igsa
    implicit none
    integer(4), intent(out) :: f90wrap_igsa
    
    f90wrap_igsa = gen_igsa
end subroutine f90wrap_gen__get__igsa

subroutine f90wrap_gen__set__igsa(f90wrap_igsa)
    use gen, only: gen_igsa => igsa
    implicit none
    integer(4), intent(in) :: f90wrap_igsa
    
    gen_igsa = f90wrap_igsa
end subroutine f90wrap_gen__set__igsa

subroutine f90wrap_gen__get__igsa_first(f90wrap_igsa_first)
    use gen, only: gen_igsa_first => igsa_first
    implicit none
    integer(4), intent(out) :: f90wrap_igsa_first
    
    f90wrap_igsa_first = gen_igsa_first
end subroutine f90wrap_gen__get__igsa_first

subroutine f90wrap_gen__set__igsa_first(f90wrap_igsa_first)
    use gen, only: gen_igsa_first => igsa_first
    implicit none
    integer(4), intent(in) :: f90wrap_igsa_first
    
    gen_igsa_first = f90wrap_igsa_first
end subroutine f90wrap_gen__set__igsa_first

subroutine f90wrap_gen__get__igsa_last(f90wrap_igsa_last)
    use gen, only: gen_igsa_last => igsa_last
    implicit none
    integer(4), intent(out) :: f90wrap_igsa_last
    
    f90wrap_igsa_last = gen_igsa_last
end subroutine f90wrap_gen__get__igsa_last

subroutine f90wrap_gen__set__igsa_last(f90wrap_igsa_last)
    use gen, only: gen_igsa_last => igsa_last
    implicit none
    integer(4), intent(in) :: f90wrap_igsa_last
    
    gen_igsa_last = f90wrap_igsa_last
end subroutine f90wrap_gen__set__igsa_last

subroutine f90wrap_gen__get__igs2(f90wrap_igs2)
    use gen, only: gen_igs2 => igs2
    implicit none
    integer(4), intent(out) :: f90wrap_igs2
    
    f90wrap_igs2 = gen_igs2
end subroutine f90wrap_gen__get__igs2

subroutine f90wrap_gen__set__igs2(f90wrap_igs2)
    use gen, only: gen_igs2 => igs2
    implicit none
    integer(4), intent(in) :: f90wrap_igs2
    
    gen_igs2 = f90wrap_igs2
end subroutine f90wrap_gen__set__igs2

subroutine f90wrap_gen__get__igsr(f90wrap_igsr)
    use gen, only: gen_igsr => igsr
    implicit none
    integer(4), intent(out) :: f90wrap_igsr
    
    f90wrap_igsr = gen_igsr
end subroutine f90wrap_gen__get__igsr

subroutine f90wrap_gen__set__igsr(f90wrap_igsr)
    use gen, only: gen_igsr => igsr
    implicit none
    integer(4), intent(in) :: f90wrap_igsr
    
    gen_igsr = f90wrap_igsr
end subroutine f90wrap_gen__set__igsr

subroutine f90wrap_gen__get__igsy(f90wrap_igsy)
    use gen, only: gen_igsy => igsy
    implicit none
    integer(4), intent(out) :: f90wrap_igsy
    
    f90wrap_igsy = gen_igsy
end subroutine f90wrap_gen__get__igsy

subroutine f90wrap_gen__set__igsy(f90wrap_igsy)
    use gen, only: gen_igsy => igsy
    implicit none
    integer(4), intent(in) :: f90wrap_igsy
    
    gen_igsy = f90wrap_igsy
end subroutine f90wrap_gen__set__igsy

subroutine f90wrap_gen__get__igsf(f90wrap_igsf)
    use gen, only: gen_igsf => igsf
    implicit none
    integer(4), intent(out) :: f90wrap_igsf
    
    f90wrap_igsf = gen_igsf
end subroutine f90wrap_gen__get__igsf

subroutine f90wrap_gen__set__igsf(f90wrap_igsf)
    use gen, only: gen_igsf => igsf
    implicit none
    integer(4), intent(in) :: f90wrap_igsf
    
    gen_igsf = f90wrap_igsf
end subroutine f90wrap_gen__set__igsf

subroutine f90wrap_gen__get__igsf_first(f90wrap_igsf_first)
    use gen, only: gen_igsf_first => igsf_first
    implicit none
    integer(4), intent(out) :: f90wrap_igsf_first
    
    f90wrap_igsf_first = gen_igsf_first
end subroutine f90wrap_gen__get__igsf_first

subroutine f90wrap_gen__set__igsf_first(f90wrap_igsf_first)
    use gen, only: gen_igsf_first => igsf_first
    implicit none
    integer(4), intent(in) :: f90wrap_igsf_first
    
    gen_igsf_first = f90wrap_igsf_first
end subroutine f90wrap_gen__set__igsf_first

subroutine f90wrap_gen__get__igsf_last(f90wrap_igsf_last)
    use gen, only: gen_igsf_last => igsf_last
    implicit none
    integer(4), intent(out) :: f90wrap_igsf_last
    
    f90wrap_igsf_last = gen_igsf_last
end subroutine f90wrap_gen__get__igsf_last

subroutine f90wrap_gen__set__igsf_last(f90wrap_igsf_last)
    use gen, only: gen_igsf_last => igsf_last
    implicit none
    integer(4), intent(in) :: f90wrap_igsf_last
    
    gen_igsf_last = f90wrap_igsf_last
end subroutine f90wrap_gen__set__igsf_last

subroutine f90wrap_gen__get__igsk(f90wrap_igsk)
    use gen, only: gen_igsk => igsk
    implicit none
    integer(4), intent(out) :: f90wrap_igsk
    
    f90wrap_igsk = gen_igsk
end subroutine f90wrap_gen__get__igsk

subroutine f90wrap_gen__set__igsk(f90wrap_igsk)
    use gen, only: gen_igsk => igsk
    implicit none
    integer(4), intent(in) :: f90wrap_igsk
    
    gen_igsk = f90wrap_igsk
end subroutine f90wrap_gen__set__igsk

subroutine f90wrap_gen__get__igsw(f90wrap_igsw)
    use gen, only: gen_igsw => igsw
    implicit none
    integer(4), intent(out) :: f90wrap_igsw
    
    f90wrap_igsw = gen_igsw
end subroutine f90wrap_gen__get__igsw

subroutine f90wrap_gen__set__igsw(f90wrap_igsw)
    use gen, only: gen_igsw => igsw
    implicit none
    integer(4), intent(in) :: f90wrap_igsw
    
    gen_igsw = f90wrap_igsw
end subroutine f90wrap_gen__set__igsw

subroutine f90wrap_gen__get__initial_condition(f90wrap_initial_condition)
    use gen, only: gen_initial_condition => initial_condition
    implicit none
    logical, intent(out) :: f90wrap_initial_condition
    
    f90wrap_initial_condition = gen_initial_condition
end subroutine f90wrap_gen__get__initial_condition

subroutine f90wrap_gen__set__initial_condition(f90wrap_initial_condition)
    use gen, only: gen_initial_condition => initial_condition
    implicit none
    logical, intent(in) :: f90wrap_initial_condition
    
    gen_initial_condition = f90wrap_initial_condition
end subroutine f90wrap_gen__set__initial_condition

subroutine f90wrap_gen__get__extended_output(f90wrap_extended_output)
    use gen, only: gen_extended_output => extended_output
    implicit none
    logical, intent(out) :: f90wrap_extended_output
    
    f90wrap_extended_output = gen_extended_output
end subroutine f90wrap_gen__get__extended_output

subroutine f90wrap_gen__set__extended_output(f90wrap_extended_output)
    use gen, only: gen_extended_output => extended_output
    implicit none
    logical, intent(in) :: f90wrap_extended_output
    
    gen_extended_output = f90wrap_extended_output
end subroutine f90wrap_gen__set__extended_output

subroutine f90wrap_gen__get__gs_output(f90wrap_gs_output)
    use gen, only: gen_gs_output => gs_output
    implicit none
    logical, intent(out) :: f90wrap_gs_output
    
    f90wrap_gs_output = gen_gs_output
end subroutine f90wrap_gen__get__gs_output

subroutine f90wrap_gen__set__gs_output(f90wrap_gs_output)
    use gen, only: gen_gs_output => gs_output
    implicit none
    logical, intent(in) :: f90wrap_gs_output
    
    gen_gs_output = f90wrap_gs_output
end subroutine f90wrap_gen__set__gs_output

subroutine f90wrap_gen__get__gb_output(f90wrap_gb_output)
    use gen, only: gen_gb_output => gb_output
    implicit none
    logical, intent(out) :: f90wrap_gb_output
    
    f90wrap_gb_output = gen_gb_output
end subroutine f90wrap_gen__get__gb_output

subroutine f90wrap_gen__set__gb_output(f90wrap_gb_output)
    use gen, only: gen_gb_output => gb_output
    implicit none
    logical, intent(in) :: f90wrap_gb_output
    
    gen_gb_output = f90wrap_gb_output
end subroutine f90wrap_gen__set__gb_output

subroutine f90wrap_gen__get__tec_header(f90wrap_tec_header)
    use gen, only: gen_tec_header => tec_header
    implicit none
    logical, intent(out) :: f90wrap_tec_header
    
    f90wrap_tec_header = gen_tec_header
end subroutine f90wrap_gen__get__tec_header

subroutine f90wrap_gen__set__tec_header(f90wrap_tec_header)
    use gen, only: gen_tec_header => tec_header
    implicit none
    logical, intent(in) :: f90wrap_tec_header
    
    gen_tec_header = f90wrap_tec_header
end subroutine f90wrap_gen__set__tec_header

subroutine f90wrap_gen__get__dinc_rt(f90wrap_dinc_rt)
    use gen, only: gen_dinc_rt => dinc_rt
    implicit none
    real(8), intent(out) :: f90wrap_dinc_rt
    
    f90wrap_dinc_rt = gen_dinc_rt
end subroutine f90wrap_gen__get__dinc_rt

subroutine f90wrap_gen__set__dinc_rt(f90wrap_dinc_rt)
    use gen, only: gen_dinc_rt => dinc_rt
    implicit none
    real(8), intent(in) :: f90wrap_dinc_rt
    
    gen_dinc_rt = f90wrap_dinc_rt
end subroutine f90wrap_gen__set__dinc_rt

subroutine f90wrap_gen__get__tol_rt(f90wrap_tol_rt)
    use gen, only: gen_tol_rt => tol_rt
    implicit none
    real(8), intent(out) :: f90wrap_tol_rt
    
    f90wrap_tol_rt = gen_tol_rt
end subroutine f90wrap_gen__get__tol_rt

subroutine f90wrap_gen__set__tol_rt(f90wrap_tol_rt)
    use gen, only: gen_tol_rt => tol_rt
    implicit none
    real(8), intent(in) :: f90wrap_tol_rt
    
    gen_tol_rt = f90wrap_tol_rt
end subroutine f90wrap_gen__set__tol_rt

subroutine f90wrap_gen__get__srelfac_rt(f90wrap_srelfac_rt)
    use gen, only: gen_srelfac_rt => srelfac_rt
    implicit none
    real(8), intent(out) :: f90wrap_srelfac_rt
    
    f90wrap_srelfac_rt = gen_srelfac_rt
end subroutine f90wrap_gen__get__srelfac_rt

subroutine f90wrap_gen__set__srelfac_rt(f90wrap_srelfac_rt)
    use gen, only: gen_srelfac_rt => srelfac_rt
    implicit none
    real(8), intent(in) :: f90wrap_srelfac_rt
    
    gen_srelfac_rt = f90wrap_srelfac_rt
end subroutine f90wrap_gen__set__srelfac_rt

subroutine f90wrap_gen__get__n(f90wrap_n)
    use gen, only: gen_n => n
    implicit none
    integer(4), intent(out) :: f90wrap_n
    
    f90wrap_n = gen_n
end subroutine f90wrap_gen__get__n

subroutine f90wrap_gen__set__n(f90wrap_n)
    use gen, only: gen_n => n
    implicit none
    integer(4), intent(in) :: f90wrap_n
    
    gen_n = f90wrap_n
end subroutine f90wrap_gen__set__n

subroutine f90wrap_gen__get__iter_rt(f90wrap_iter_rt)
    use gen, only: gen_iter_rt => iter_rt
    implicit none
    integer(4), intent(out) :: f90wrap_iter_rt
    
    f90wrap_iter_rt = gen_iter_rt
end subroutine f90wrap_gen__get__iter_rt

subroutine f90wrap_gen__set__iter_rt(f90wrap_iter_rt)
    use gen, only: gen_iter_rt => iter_rt
    implicit none
    integer(4), intent(in) :: f90wrap_iter_rt
    
    gen_iter_rt = f90wrap_iter_rt
end subroutine f90wrap_gen__set__iter_rt

subroutine f90wrap_gen__get__iter_rt_ant(f90wrap_iter_rt_ant)
    use gen, only: gen_iter_rt_ant => iter_rt_ant
    implicit none
    integer(4), intent(out) :: f90wrap_iter_rt_ant
    
    f90wrap_iter_rt_ant = gen_iter_rt_ant
end subroutine f90wrap_gen__get__iter_rt_ant

subroutine f90wrap_gen__set__iter_rt_ant(f90wrap_iter_rt_ant)
    use gen, only: gen_iter_rt_ant => iter_rt_ant
    implicit none
    integer(4), intent(in) :: f90wrap_iter_rt_ant
    
    gen_iter_rt_ant = f90wrap_iter_rt_ant
end subroutine f90wrap_gen__set__iter_rt_ant

subroutine f90wrap_gen__get__maxit_rt(f90wrap_maxit_rt)
    use gen, only: gen_maxit_rt => maxit_rt
    implicit none
    integer(4), intent(out) :: f90wrap_maxit_rt
    
    f90wrap_maxit_rt = gen_maxit_rt
end subroutine f90wrap_gen__get__maxit_rt

subroutine f90wrap_gen__set__maxit_rt(f90wrap_maxit_rt)
    use gen, only: gen_maxit_rt => maxit_rt
    implicit none
    integer(4), intent(in) :: f90wrap_maxit_rt
    
    gen_maxit_rt = f90wrap_maxit_rt
end subroutine f90wrap_gen__set__maxit_rt

subroutine f90wrap_gen__get__itsolvtot_rt(f90wrap_itsolvtot_rt)
    use gen, only: gen_itsolvtot_rt => itsolvtot_rt
    implicit none
    integer(4), intent(out) :: f90wrap_itsolvtot_rt
    
    f90wrap_itsolvtot_rt = gen_itsolvtot_rt
end subroutine f90wrap_gen__get__itsolvtot_rt

subroutine f90wrap_gen__set__itsolvtot_rt(f90wrap_itsolvtot_rt)
    use gen, only: gen_itsolvtot_rt => itsolvtot_rt
    implicit none
    integer(4), intent(in) :: f90wrap_itsolvtot_rt
    
    gen_itsolvtot_rt = f90wrap_itsolvtot_rt
end subroutine f90wrap_gen__set__itsolvtot_rt

subroutine f90wrap_gen__get__ittot_rt(f90wrap_ittot_rt)
    use gen, only: gen_ittot_rt => ittot_rt
    implicit none
    integer(4), intent(out) :: f90wrap_ittot_rt
    
    f90wrap_ittot_rt = gen_ittot_rt
end subroutine f90wrap_gen__get__ittot_rt

subroutine f90wrap_gen__set__ittot_rt(f90wrap_ittot_rt)
    use gen, only: gen_ittot_rt => ittot_rt
    implicit none
    integer(4), intent(in) :: f90wrap_ittot_rt
    
    gen_ittot_rt = f90wrap_ittot_rt
end subroutine f90wrap_gen__set__ittot_rt

subroutine f90wrap_gen__get__analyt_deriv_rt(f90wrap_analyt_deriv_rt)
    use gen, only: gen_analyt_deriv_rt => analyt_deriv_rt
    implicit none
    logical, intent(out) :: f90wrap_analyt_deriv_rt
    
    f90wrap_analyt_deriv_rt = gen_analyt_deriv_rt
end subroutine f90wrap_gen__get__analyt_deriv_rt

subroutine f90wrap_gen__set__analyt_deriv_rt(f90wrap_analyt_deriv_rt)
    use gen, only: gen_analyt_deriv_rt => analyt_deriv_rt
    implicit none
    logical, intent(in) :: f90wrap_analyt_deriv_rt
    
    gen_analyt_deriv_rt = f90wrap_analyt_deriv_rt
end subroutine f90wrap_gen__set__analyt_deriv_rt

subroutine f90wrap_gen__get__mass_balance_rt(f90wrap_mass_balance_rt)
    use gen, only: gen_mass_balance_rt => mass_balance_rt
    implicit none
    logical, intent(out) :: f90wrap_mass_balance_rt
    
    f90wrap_mass_balance_rt = gen_mass_balance_rt
end subroutine f90wrap_gen__get__mass_balance_rt

subroutine f90wrap_gen__set__mass_balance_rt(f90wrap_mass_balance_rt)
    use gen, only: gen_mass_balance_rt => mass_balance_rt
    implicit none
    logical, intent(in) :: f90wrap_mass_balance_rt
    
    gen_mass_balance_rt = f90wrap_mass_balance_rt
end subroutine f90wrap_gen__set__mass_balance_rt

subroutine f90wrap_gen__get__sparse_blocks(f90wrap_sparse_blocks)
    use gen, only: gen_sparse_blocks => sparse_blocks
    implicit none
    logical, intent(out) :: f90wrap_sparse_blocks
    
    f90wrap_sparse_blocks = gen_sparse_blocks
end subroutine f90wrap_gen__get__sparse_blocks

subroutine f90wrap_gen__set__sparse_blocks(f90wrap_sparse_blocks)
    use gen, only: gen_sparse_blocks => sparse_blocks
    implicit none
    logical, intent(in) :: f90wrap_sparse_blocks
    
    gen_sparse_blocks = f90wrap_sparse_blocks
end subroutine f90wrap_gen__set__sparse_blocks

subroutine f90wrap_gen__get__redox_equil_rt(f90wrap_redox_equil_rt)
    use gen, only: gen_redox_equil_rt => redox_equil_rt
    implicit none
    logical, intent(out) :: f90wrap_redox_equil_rt
    
    f90wrap_redox_equil_rt = gen_redox_equil_rt
end subroutine f90wrap_gen__get__redox_equil_rt

subroutine f90wrap_gen__set__redox_equil_rt(f90wrap_redox_equil_rt)
    use gen, only: gen_redox_equil_rt => redox_equil_rt
    implicit none
    logical, intent(in) :: f90wrap_redox_equil_rt
    
    gen_redox_equil_rt = f90wrap_redox_equil_rt
end subroutine f90wrap_gen__set__redox_equil_rt

subroutine f90wrap_gen__get__under_relax_rt(f90wrap_under_relax_rt)
    use gen, only: gen_under_relax_rt => under_relax_rt
    implicit none
    logical, intent(out) :: f90wrap_under_relax_rt
    
    f90wrap_under_relax_rt = gen_under_relax_rt
end subroutine f90wrap_gen__get__under_relax_rt

subroutine f90wrap_gen__set__under_relax_rt(f90wrap_under_relax_rt)
    use gen, only: gen_under_relax_rt => under_relax_rt
    implicit none
    logical, intent(in) :: f90wrap_under_relax_rt
    
    gen_under_relax_rt = f90wrap_under_relax_rt
end subroutine f90wrap_gen__set__under_relax_rt

subroutine f90wrap_gen__get__gas_advection(f90wrap_gas_advection)
    use gen, only: gen_gas_advection => gas_advection
    implicit none
    logical, intent(out) :: f90wrap_gas_advection
    
    f90wrap_gas_advection = gen_gas_advection
end subroutine f90wrap_gen__get__gas_advection

subroutine f90wrap_gen__set__gas_advection(f90wrap_gas_advection)
    use gen, only: gen_gas_advection => gas_advection
    implicit none
    logical, intent(in) :: f90wrap_gas_advection
    
    gen_gas_advection = f90wrap_gas_advection
end subroutine f90wrap_gen__set__gas_advection

subroutine f90wrap_gen__get__cum_molfrac(f90wrap_cum_molfrac)
    use gen, only: gen_cum_molfrac => cum_molfrac
    implicit none
    logical, intent(out) :: f90wrap_cum_molfrac
    
    f90wrap_cum_molfrac = gen_cum_molfrac
end subroutine f90wrap_gen__get__cum_molfrac

subroutine f90wrap_gen__set__cum_molfrac(f90wrap_cum_molfrac)
    use gen, only: gen_cum_molfrac => cum_molfrac
    implicit none
    logical, intent(in) :: f90wrap_cum_molfrac
    
    gen_cum_molfrac = f90wrap_cum_molfrac
end subroutine f90wrap_gen__set__cum_molfrac

subroutine f90wrap_gen__get__gas_gravity(f90wrap_gas_gravity)
    use gen, only: gen_gas_gravity => gas_gravity
    implicit none
    logical, intent(out) :: f90wrap_gas_gravity
    
    f90wrap_gas_gravity = gen_gas_gravity
end subroutine f90wrap_gen__get__gas_gravity

subroutine f90wrap_gen__set__gas_gravity(f90wrap_gas_gravity)
    use gen, only: gen_gas_gravity => gas_gravity
    implicit none
    logical, intent(in) :: f90wrap_gas_gravity
    
    gen_gas_gravity = f90wrap_gas_gravity
end subroutine f90wrap_gen__set__gas_gravity

subroutine f90wrap_gen__get__update_tortuosity(f90wrap_update_tortuosity)
    use gen, only: gen_update_tortuosity => update_tortuosity
    implicit none
    logical, intent(out) :: f90wrap_update_tortuosity
    
    f90wrap_update_tortuosity = gen_update_tortuosity
end subroutine f90wrap_gen__get__update_tortuosity

subroutine f90wrap_gen__set__update_tortuosity(f90wrap_update_tortuosity)
    use gen, only: gen_update_tortuosity => update_tortuosity
    implicit none
    logical, intent(in) :: f90wrap_update_tortuosity
    
    gen_update_tortuosity = f90wrap_update_tortuosity
end subroutine f90wrap_gen__set__update_tortuosity

subroutine f90wrap_gen__array__c(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_c => c
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_c)) then
        dshape(1:2) = shape(gen_c)
        dloc = loc(gen_c)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__c

subroutine f90wrap_gen__array__cnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cnew => cnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_cnew)) then
        dshape(1:2) = shape(gen_cnew)
        dloc = loc(gen_cnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cnew

subroutine f90wrap_gen__array__cec_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cec_g => cec_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cec_g)) then
        dshape(1:1) = shape(gen_cec_g)
        dloc = loc(gen_cec_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cec_g

subroutine f90wrap_gen__array__gamma(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gamma => gamma
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gamma)) then
        dshape(1:2) = shape(gen_gamma)
        dloc = loc(gen_gamma)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gamma

subroutine f90wrap_gen__array__totaold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totaold => totaold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totaold)) then
        dshape(1:2) = shape(gen_totaold)
        dloc = loc(gen_totaold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totaold

subroutine f90wrap_gen__array__totanew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totanew => totanew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totanew)) then
        dshape(1:2) = shape(gen_totanew)
        dloc = loc(gen_totanew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totanew

subroutine f90wrap_gen__array__totcold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcold => totcold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totcold)) then
        dshape(1:2) = shape(gen_totcold)
        dloc = loc(gen_totcold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcold

subroutine f90wrap_gen__array__totcnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcnew => totcnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totcnew)) then
        dshape(1:2) = shape(gen_totcnew)
        dloc = loc(gen_totcnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcnew

subroutine f90wrap_gen__array__totgold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgold => totgold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totgold)) then
        dshape(1:2) = shape(gen_totgold)
        dloc = loc(gen_totgold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgold

subroutine f90wrap_gen__array__totgnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgnew => totgnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totgnew)) then
        dshape(1:2) = shape(gen_totgnew)
        dloc = loc(gen_totgnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgnew

subroutine f90wrap_gen__array__totsold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totsold => totsold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totsold)) then
        dshape(1:2) = shape(gen_totsold)
        dloc = loc(gen_totsold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totsold

subroutine f90wrap_gen__array__totsnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totsnew => totsnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totsnew)) then
        dshape(1:2) = shape(gen_totsnew)
        dloc = loc(gen_totsnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totsnew

subroutine f90wrap_gen__array__cmold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmold => cmold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_cmold)) then
        dshape(1:2) = shape(gen_cmold)
        dloc = loc(gen_cmold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmold

subroutine f90wrap_gen__array__cmnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmnew => cmnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_cmnew)) then
        dshape(1:2) = shape(gen_cmnew)
        dloc = loc(gen_cmnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmnew

subroutine f90wrap_gen__array__distcoff_rt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_distcoff_rt => distcoff_rt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_distcoff_rt)) then
        dshape(1:2) = shape(gen_distcoff_rt)
        dloc = loc(gen_distcoff_rt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__distcoff_rt

subroutine f90wrap_gen__array__ksb2(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ksb2 => ksb2
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_ksb2)) then
        dshape(1:2) = shape(gen_ksb2)
        dloc = loc(gen_ksb2)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ksb2

subroutine f90wrap_gen__array__pdm_rt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_pdm_rt => pdm_rt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_pdm_rt)) then
        dshape(1:2) = shape(gen_pdm_rt)
        dloc = loc(gen_pdm_rt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__pdm_rt

subroutine f90wrap_gen__array__gold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gold => gold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gold)) then
        dshape(1:2) = shape(gen_gold)
        dloc = loc(gen_gold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gold

subroutine f90wrap_gen__array__gnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gnew => gnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gnew)) then
        dshape(1:2) = shape(gen_gnew)
        dloc = loc(gen_gnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gnew

subroutine f90wrap_gen__array__cx(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cx => cx
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_cx)) then
        dshape(1:2) = shape(gen_cx)
        dloc = loc(gen_cx)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cx

subroutine f90wrap_gen__array__sionnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sionnew => sionnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sionnew)) then
        dshape(1:1) = shape(gen_sionnew)
        dloc = loc(gen_sionnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sionnew

subroutine f90wrap_gen__array__sionold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sionold => sionold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sionold)) then
        dshape(1:1) = shape(gen_sionold)
        dloc = loc(gen_sionold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sionold

subroutine f90wrap_gen__array__phi(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_phi => phi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_phi)) then
        dshape(1:2) = shape(gen_phi)
        dloc = loc(gen_phi)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__phi

subroutine f90wrap_gen__array__phiold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_phiold => phiold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_phiold)) then
        dshape(1:2) = shape(gen_phiold)
        dloc = loc(gen_phiold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__phiold

subroutine f90wrap_gen__array__phi_init(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_phi_init => phi_init
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_phi_init)) then
        dshape(1:2) = shape(gen_phi_init)
        dloc = loc(gen_phi_init)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__phi_init

subroutine f90wrap_gen__array__area(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_area => area
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_area)) then
        dshape(1:2) = shape(gen_area)
        dloc = loc(gen_area)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__area

subroutine f90wrap_gen__array__cinfrt_va(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfrt_va => cinfrt_va
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfrt_va)) then
        dshape(1:1) = shape(gen_cinfrt_va)
        dloc = loc(gen_cinfrt_va)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfrt_va

subroutine f90wrap_gen__array__cinfrt_da(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfrt_da => cinfrt_da
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfrt_da)) then
        dshape(1:1) = shape(gen_cinfrt_da)
        dloc = loc(gen_cinfrt_da)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfrt_da

subroutine f90wrap_gen__array__cinfrt_dg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfrt_dg => cinfrt_dg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfrt_dg)) then
        dshape(1:1) = shape(gen_cinfrt_dg)
        dloc = loc(gen_cinfrt_dg)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfrt_dg

subroutine f90wrap_gen__array__deltaij(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_deltaij => deltaij
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_deltaij)) then
        dshape(1:1) = shape(gen_deltaij)
        dloc = loc(gen_deltaij)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__deltaij

subroutine f90wrap_gen__array__tauij(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_tauij => tauij
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_tauij)) then
        dshape(1:1) = shape(gen_tauij)
        dloc = loc(gen_tauij)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__tauij

subroutine f90wrap_gen__array__gporij(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gporij => gporij
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gporij)) then
        dshape(1:1) = shape(gen_gporij)
        dloc = loc(gen_gporij)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gporij

subroutine f90wrap_gen__array__gsatij(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gsatij => gsatij
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gsatij)) then
        dshape(1:1) = shape(gen_gsatij)
        dloc = loc(gen_gsatij)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gsatij

subroutine f90wrap_gen__array__tkel(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_tkel => tkel
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_tkel)) then
        dshape(1:1) = shape(gen_tkel)
        dloc = loc(gen_tkel)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__tkel

subroutine f90wrap_gen__array__gmfrac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gmfrac => gmfrac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gmfrac)) then
        dshape(1:2) = shape(gen_gmfrac)
        dloc = loc(gen_gmfrac)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gmfrac

subroutine f90wrap_gen__array__totgmfrac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgmfrac => totgmfrac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totgmfrac)) then
        dshape(1:2) = shape(gen_totgmfrac)
        dloc = loc(gen_totgmfrac)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgmfrac

subroutine f90wrap_gen__array__mpropc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_mpropc => mpropc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_mpropc)) then
        dshape(1:1) = shape(gen_mpropc)
        dloc = loc(gen_mpropc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__mpropc

subroutine f90wrap_gen__array__bcondrt_a(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bcondrt_a => bcondrt_a
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_bcondrt_a)) then
        dshape(1:2) = shape(gen_bcondrt_a)
        dloc = loc(gen_bcondrt_a)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bcondrt_a

subroutine f90wrap_gen__array__bcondrt_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bcondrt_g => bcondrt_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_bcondrt_g)) then
        dshape(1:2) = shape(gen_bcondrt_g)
        dloc = loc(gen_bcondrt_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bcondrt_g

subroutine f90wrap_gen__array__bdycrt_d(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bdycrt_d => bdycrt_d
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_bdycrt_d)) then
        dshape(1:1) = shape(gen_bdycrt_d)
        dloc = loc(gen_bdycrt_d)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bdycrt_d

subroutine f90wrap_gen__array__zgbrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_zgbrt => zgbrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_zgbrt)) then
        dshape(1:1) = shape(gen_zgbrt)
        dloc = loc(gen_zgbrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__zgbrt

subroutine f90wrap_gen__array__dijbrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dijbrt => dijbrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dijbrt)) then
        dshape(1:1) = shape(gen_dijbrt)
        dloc = loc(gen_dijbrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dijbrt

subroutine f90wrap_gen__array__gbrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gbrt => gbrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gbrt)) then
        dshape(1:2) = shape(gen_gbrt)
        dloc = loc(gen_gbrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gbrt

subroutine f90wrap_gen__array__tsrc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_tsrc => tsrc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_tsrc)) then
        dshape(1:1) = shape(gen_tsrc)
        dloc = loc(gen_tsrc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__tsrc

subroutine f90wrap_gen__array__permbrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_permbrt => permbrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_permbrt)) then
        dshape(1:1) = shape(gen_permbrt)
        dloc = loc(gen_permbrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__permbrt

subroutine f90wrap_gen__array__cinfvs_gbrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfvs_gbrt => cinfvs_gbrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfvs_gbrt)) then
        dshape(1:1) = shape(gen_cinfvs_gbrt)
        dloc = loc(gen_cinfvs_gbrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfvs_gbrt

subroutine f90wrap_gen__array__iabrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iabrt => iabrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iabrt)) then
        dshape(1:1) = shape(gen_iabrt)
        dloc = loc(gen_iabrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iabrt

subroutine f90wrap_gen__array__jabrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jabrt => jabrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jabrt)) then
        dshape(1:1) = shape(gen_jabrt)
        dloc = loc(gen_jabrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jabrt

subroutine f90wrap_gen__get__itsrc(f90wrap_itsrc)
    use gen, only: gen_itsrc => itsrc
    implicit none
    integer(4), intent(out) :: f90wrap_itsrc
    
    f90wrap_itsrc = gen_itsrc
end subroutine f90wrap_gen__get__itsrc

subroutine f90wrap_gen__set__itsrc(f90wrap_itsrc)
    use gen, only: gen_itsrc => itsrc
    implicit none
    integer(4), intent(in) :: f90wrap_itsrc
    
    gen_itsrc = f90wrap_itsrc
end subroutine f90wrap_gen__set__itsrc

subroutine f90wrap_gen__get__nbrt(f90wrap_nbrt)
    use gen, only: gen_nbrt => nbrt
    implicit none
    integer(4), intent(out) :: f90wrap_nbrt
    
    f90wrap_nbrt = gen_nbrt
end subroutine f90wrap_gen__get__nbrt

subroutine f90wrap_gen__set__nbrt(f90wrap_nbrt)
    use gen, only: gen_nbrt => nbrt
    implicit none
    integer(4), intent(in) :: f90wrap_nbrt
    
    gen_nbrt = f90wrap_nbrt
end subroutine f90wrap_gen__set__nbrt

subroutine f90wrap_gen__get__nbzrt(f90wrap_nbzrt)
    use gen, only: gen_nbzrt => nbzrt
    implicit none
    integer(4), intent(out) :: f90wrap_nbzrt
    
    f90wrap_nbzrt = gen_nbzrt
end subroutine f90wrap_gen__get__nbzrt

subroutine f90wrap_gen__set__nbzrt(f90wrap_nbzrt)
    use gen, only: gen_nbzrt => nbzrt
    implicit none
    integer(4), intent(in) :: f90wrap_nbzrt
    
    gen_nbzrt = f90wrap_nbzrt
end subroutine f90wrap_gen__set__nbzrt

subroutine f90wrap_gen__get__ntsrc(f90wrap_ntsrc)
    use gen, only: gen_ntsrc => ntsrc
    implicit none
    integer(4), intent(out) :: f90wrap_ntsrc
    
    f90wrap_ntsrc = gen_ntsrc
end subroutine f90wrap_gen__get__ntsrc

subroutine f90wrap_gen__set__ntsrc(f90wrap_ntsrc)
    use gen, only: gen_ntsrc => ntsrc
    implicit none
    integer(4), intent(in) :: f90wrap_ntsrc
    
    gen_ntsrc = f90wrap_ntsrc
end subroutine f90wrap_gen__set__ntsrc

subroutine f90wrap_gen__get__spec_conc(f90wrap_spec_conc)
    use gen, only: gen_spec_conc => spec_conc
    implicit none
    logical, intent(out) :: f90wrap_spec_conc
    
    f90wrap_spec_conc = gen_spec_conc
end subroutine f90wrap_gen__get__spec_conc

subroutine f90wrap_gen__set__spec_conc(f90wrap_spec_conc)
    use gen, only: gen_spec_conc => spec_conc
    implicit none
    logical, intent(in) :: f90wrap_spec_conc
    
    gen_spec_conc = f90wrap_spec_conc
end subroutine f90wrap_gen__set__spec_conc

subroutine f90wrap_gen__get__transient_source(f90wrap_transient_source)
    use gen, only: gen_transient_source => transient_source
    implicit none
    logical, intent(out) :: f90wrap_transient_source
    
    f90wrap_transient_source = gen_transient_source
end subroutine f90wrap_gen__get__transient_source

subroutine f90wrap_gen__set__transient_source(f90wrap_transient_source)
    use gen, only: gen_transient_source => transient_source
    implicit none
    logical, intent(in) :: f90wrap_transient_source
    
    gen_transient_source = f90wrap_transient_source
end subroutine f90wrap_gen__set__transient_source

subroutine f90wrap_gen__get__update_bcrt(f90wrap_update_bcrt)
    use gen, only: gen_update_bcrt => update_bcrt
    implicit none
    logical, intent(out) :: f90wrap_update_bcrt
    
    f90wrap_update_bcrt = gen_update_bcrt
end subroutine f90wrap_gen__get__update_bcrt

subroutine f90wrap_gen__set__update_bcrt(f90wrap_update_bcrt)
    use gen, only: gen_update_bcrt => update_bcrt
    implicit none
    logical, intent(in) :: f90wrap_update_bcrt
    
    gen_update_bcrt = f90wrap_update_bcrt
end subroutine f90wrap_gen__set__update_bcrt

subroutine f90wrap_gen__array__astor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_astor => astor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_astor)) then
        dshape(1:1) = shape(gen_astor)
        dloc = loc(gen_astor)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__astor

subroutine f90wrap_gen__array__cflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cflux => cflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_cflux)) then
        dshape(1:2) = shape(gen_cflux)
        dloc = loc(gen_cflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cflux

subroutine f90wrap_gen__array__cstor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cstor => cstor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cstor)) then
        dshape(1:1) = shape(gen_cstor)
        dloc = loc(gen_cstor)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cstor

subroutine f90wrap_gen__array__gflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gflux => gflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_gflux)) then
        dshape(1:2) = shape(gen_gflux)
        dloc = loc(gen_gflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gflux

subroutine f90wrap_gen__array__gstor(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gstor => gstor
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gstor)) then
        dshape(1:1) = shape(gen_gstor)
        dloc = loc(gen_gstor)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gstor

subroutine f90wrap_gen__array__dtotcflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dtotcflux => dtotcflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dtotcflux)) then
        dshape(1:1) = shape(gen_dtotcflux)
        dloc = loc(gen_dtotcflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dtotcflux

subroutine f90wrap_gen__array__dtotgflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dtotgflux => dtotgflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dtotgflux)) then
        dshape(1:1) = shape(gen_dtotgflux)
        dloc = loc(gen_dtotgflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dtotgflux

subroutine f90wrap_gen__array__ratemdp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ratemdp => ratemdp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_ratemdp)) then
        dshape(1:2) = shape(gen_ratemdp)
        dloc = loc(gen_ratemdp)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ratemdp

subroutine f90wrap_gen__array__totcflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcflux => totcflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totcflux)) then
        dshape(1:1) = shape(gen_totcflux)
        dloc = loc(gen_totcflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcflux

subroutine f90wrap_gen__array__totgflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgflux => totgflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgflux)) then
        dshape(1:1) = shape(gen_totgflux)
        dloc = loc(gen_totgflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgflux

subroutine f90wrap_gen__array__totgaflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgaflux => totgaflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgaflux)) then
        dshape(1:1) = shape(gen_totgaflux)
        dloc = loc(gen_totgaflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgaflux

subroutine f90wrap_gen__array__totmdp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totmdp => totmdp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_totmdp)) then
        dshape(1:2) = shape(gen_totmdp)
        dloc = loc(gen_totmdp)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totmdp

subroutine f90wrap_gen__array__i2up(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_i2up => i2up
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_i2up)) then
        dshape(1:1) = shape(gen_i2up)
        dloc = loc(gen_i2up)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__i2up

subroutine f90wrap_gen__array__art(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_art => art
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_art)) then
        dshape(1:1) = shape(gen_art)
        dloc = loc(gen_art)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__art

subroutine f90wrap_gen__array__brt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_brt => brt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_brt)) then
        dshape(1:1) = shape(gen_brt)
        dloc = loc(gen_brt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__brt

subroutine f90wrap_gen__array__urt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_urt => urt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_urt)) then
        dshape(1:1) = shape(gen_urt)
        dloc = loc(gen_urt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__urt

subroutine f90wrap_gen__array__resrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_resrt => resrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_resrt)) then
        dshape(1:1) = shape(gen_resrt)
        dloc = loc(gen_resrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__resrt

subroutine f90wrap_gen__array__afrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_afrt => afrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_afrt)) then
        dshape(1:1) = shape(gen_afrt)
        dloc = loc(gen_afrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__afrt

subroutine f90wrap_gen__get__restol_rt(f90wrap_restol_rt)
    use gen, only: gen_restol_rt => restol_rt
    implicit none
    real(8), intent(out) :: f90wrap_restol_rt
    
    f90wrap_restol_rt = gen_restol_rt
end subroutine f90wrap_gen__get__restol_rt

subroutine f90wrap_gen__set__restol_rt(f90wrap_restol_rt)
    use gen, only: gen_restol_rt => restol_rt
    implicit none
    real(8), intent(in) :: f90wrap_restol_rt
    
    gen_restol_rt = f90wrap_restol_rt
end subroutine f90wrap_gen__set__restol_rt

subroutine f90wrap_gen__get__deltol_rt(f90wrap_deltol_rt)
    use gen, only: gen_deltol_rt => deltol_rt
    implicit none
    real(8), intent(out) :: f90wrap_deltol_rt
    
    f90wrap_deltol_rt = gen_deltol_rt
end subroutine f90wrap_gen__get__deltol_rt

subroutine f90wrap_gen__set__deltol_rt(f90wrap_deltol_rt)
    use gen, only: gen_deltol_rt => deltol_rt
    implicit none
    real(8), intent(in) :: f90wrap_deltol_rt
    
    gen_deltol_rt = f90wrap_deltol_rt
end subroutine f90wrap_gen__set__deltol_rt

subroutine f90wrap_gen__get__urtlim_log(f90wrap_urtlim_log)
    use gen, only: gen_urtlim_log => urtlim_log
    implicit none
    real(8), intent(out) :: f90wrap_urtlim_log
    
    f90wrap_urtlim_log = gen_urtlim_log
end subroutine f90wrap_gen__get__urtlim_log

subroutine f90wrap_gen__set__urtlim_log(f90wrap_urtlim_log)
    use gen, only: gen_urtlim_log => urtlim_log
    implicit none
    real(8), intent(in) :: f90wrap_urtlim_log
    
    gen_urtlim_log = f90wrap_urtlim_log
end subroutine f90wrap_gen__set__urtlim_log

subroutine f90wrap_gen__array__iart(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iart => iart
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iart)) then
        dshape(1:1) = shape(gen_iart)
        dloc = loc(gen_iart)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iart

subroutine f90wrap_gen__array__jart(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jart => jart
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jart)) then
        dshape(1:1) = shape(gen_jart)
        dloc = loc(gen_jart)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jart

subroutine f90wrap_gen__array__lart(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_lart => lart
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_lart)) then
        dshape(1:1) = shape(gen_lart)
        dloc = loc(gen_lart)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__lart

subroutine f90wrap_gen__array__kbl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_kbl => kbl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 5
    if (allocated(gen_kbl)) then
        dshape(1:2) = shape(gen_kbl)
        dloc = loc(gen_kbl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__kbl

subroutine f90wrap_gen__array__kart(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_kart => kart
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_kart)) then
        dshape(1:1) = shape(gen_kart)
        dloc = loc(gen_kart)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__kart

subroutine f90wrap_gen__array__iafrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iafrt => iafrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iafrt)) then
        dshape(1:1) = shape(gen_iafrt)
        dloc = loc(gen_iafrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iafrt

subroutine f90wrap_gen__array__jafrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jafrt => jafrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jafrt)) then
        dshape(1:1) = shape(gen_jafrt)
        dloc = loc(gen_jafrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jafrt

subroutine f90wrap_gen__array__iafdrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iafdrt => iafdrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iafdrt)) then
        dshape(1:1) = shape(gen_iafdrt)
        dloc = loc(gen_iafdrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iafdrt

subroutine f90wrap_gen__array__lorderrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_lorderrt => lorderrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_lorderrt)) then
        dshape(1:1) = shape(gen_lorderrt)
        dloc = loc(gen_lorderrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__lorderrt

subroutine f90wrap_gen__array__invordrt(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_invordrt => invordrt
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_invordrt)) then
        dshape(1:1) = shape(gen_invordrt)
        dloc = loc(gen_invordrt)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__invordrt

subroutine f90wrap_gen__array__iadbl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iadbl => iadbl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iadbl)) then
        dshape(1:1) = shape(gen_iadbl)
        dloc = loc(gen_iadbl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iadbl

subroutine f90wrap_gen__array__jadbl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jadbl => jadbl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jadbl)) then
        dshape(1:1) = shape(gen_jadbl)
        dloc = loc(gen_jadbl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jadbl

subroutine f90wrap_gen__array__kadbl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_kadbl => kadbl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 5
    if (allocated(gen_kadbl)) then
        dshape(1:2) = shape(gen_kadbl)
        dloc = loc(gen_kadbl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__kadbl

subroutine f90wrap_gen__array__iaobl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iaobl => iaobl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iaobl)) then
        dshape(1:1) = shape(gen_iaobl)
        dloc = loc(gen_iaobl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iaobl

subroutine f90wrap_gen__array__jaobl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jaobl => jaobl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jaobl)) then
        dshape(1:1) = shape(gen_jaobl)
        dloc = loc(gen_jaobl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jaobl

subroutine f90wrap_gen__array__kaobl(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_kaobl => kaobl
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 5
    if (allocated(gen_kaobl)) then
        dshape(1:2) = shape(gen_kaobl)
        dloc = loc(gen_kaobl)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__kaobl

subroutine f90wrap_gen__get__mnjart(f90wrap_mnjart)
    use gen, only: gen_mnjart => mnjart
    implicit none
    integer(4), intent(out) :: f90wrap_mnjart
    
    f90wrap_mnjart = gen_mnjart
end subroutine f90wrap_gen__get__mnjart

subroutine f90wrap_gen__set__mnjart(f90wrap_mnjart)
    use gen, only: gen_mnjart => mnjart
    implicit none
    integer(4), intent(in) :: f90wrap_mnjart
    
    gen_mnjart = f90wrap_mnjart
end subroutine f90wrap_gen__set__mnjart

subroutine f90wrap_gen__get__mnjafrt(f90wrap_mnjafrt)
    use gen, only: gen_mnjafrt => mnjafrt
    implicit none
    integer(4), intent(out) :: f90wrap_mnjafrt
    
    f90wrap_mnjafrt = gen_mnjafrt
end subroutine f90wrap_gen__get__mnjafrt

subroutine f90wrap_gen__set__mnjafrt(f90wrap_mnjafrt)
    use gen, only: gen_mnjafrt => mnjafrt
    implicit none
    integer(4), intent(in) :: f90wrap_mnjafrt
    
    gen_mnjafrt = f90wrap_mnjafrt
end subroutine f90wrap_gen__set__mnjafrt

subroutine f90wrap_gen__get__njart(f90wrap_njart)
    use gen, only: gen_njart => njart
    implicit none
    integer(4), intent(out) :: f90wrap_njart
    
    f90wrap_njart = gen_njart
end subroutine f90wrap_gen__get__njart

subroutine f90wrap_gen__set__njart(f90wrap_njart)
    use gen, only: gen_njart => njart
    implicit none
    integer(4), intent(in) :: f90wrap_njart
    
    gen_njart = f90wrap_njart
end subroutine f90wrap_gen__set__njart

subroutine f90wrap_gen__get__njafrt(f90wrap_njafrt)
    use gen, only: gen_njafrt => njafrt
    implicit none
    integer(4), intent(out) :: f90wrap_njafrt
    
    f90wrap_njafrt = gen_njafrt
end subroutine f90wrap_gen__get__njafrt

subroutine f90wrap_gen__set__njafrt(f90wrap_njafrt)
    use gen, only: gen_njafrt => njafrt
    implicit none
    integer(4), intent(in) :: f90wrap_njafrt
    
    gen_njafrt = f90wrap_njafrt
end subroutine f90wrap_gen__set__njafrt

subroutine f90wrap_gen__get__njadbl(f90wrap_njadbl)
    use gen, only: gen_njadbl => njadbl
    implicit none
    integer(4), intent(out) :: f90wrap_njadbl
    
    f90wrap_njadbl = gen_njadbl
end subroutine f90wrap_gen__get__njadbl

subroutine f90wrap_gen__set__njadbl(f90wrap_njadbl)
    use gen, only: gen_njadbl => njadbl
    implicit none
    integer(4), intent(in) :: f90wrap_njadbl
    
    gen_njadbl = f90wrap_njadbl
end subroutine f90wrap_gen__set__njadbl

subroutine f90wrap_gen__get__njaobl(f90wrap_njaobl)
    use gen, only: gen_njaobl => njaobl
    implicit none
    integer(4), intent(out) :: f90wrap_njaobl
    
    f90wrap_njaobl = gen_njaobl
end subroutine f90wrap_gen__get__njaobl

subroutine f90wrap_gen__set__njaobl(f90wrap_njaobl)
    use gen, only: gen_njaobl => njaobl
    implicit none
    integer(4), intent(in) :: f90wrap_njaobl
    
    gen_njaobl = f90wrap_njaobl
end subroutine f90wrap_gen__set__njaobl

subroutine f90wrap_gen__get__level_rt(f90wrap_level_rt)
    use gen, only: gen_level_rt => level_rt
    implicit none
    integer(4), intent(out) :: f90wrap_level_rt
    
    f90wrap_level_rt = gen_level_rt
end subroutine f90wrap_gen__get__level_rt

subroutine f90wrap_gen__set__level_rt(f90wrap_level_rt)
    use gen, only: gen_level_rt => level_rt
    implicit none
    integer(4), intent(in) :: f90wrap_level_rt
    
    gen_level_rt = f90wrap_level_rt
end subroutine f90wrap_gen__set__level_rt

subroutine f90wrap_gen__get__msolvit_rt(f90wrap_msolvit_rt)
    use gen, only: gen_msolvit_rt => msolvit_rt
    implicit none
    integer(4), intent(out) :: f90wrap_msolvit_rt
    
    f90wrap_msolvit_rt = gen_msolvit_rt
end subroutine f90wrap_gen__get__msolvit_rt

subroutine f90wrap_gen__set__msolvit_rt(f90wrap_msolvit_rt)
    use gen, only: gen_msolvit_rt => msolvit_rt
    implicit none
    integer(4), intent(in) :: f90wrap_msolvit_rt
    
    gen_msolvit_rt = f90wrap_msolvit_rt
end subroutine f90wrap_gen__set__msolvit_rt

subroutine f90wrap_gen__get__nexvol_old_rt(f90wrap_nexvol_old_rt)
    use gen, only: gen_nexvol_old_rt => nexvol_old_rt
    implicit none
    integer(4), intent(out) :: f90wrap_nexvol_old_rt
    
    f90wrap_nexvol_old_rt = gen_nexvol_old_rt
end subroutine f90wrap_gen__get__nexvol_old_rt

subroutine f90wrap_gen__set__nexvol_old_rt(f90wrap_nexvol_old_rt)
    use gen, only: gen_nexvol_old_rt => nexvol_old_rt
    implicit none
    integer(4), intent(in) :: f90wrap_nexvol_old_rt
    
    gen_nexvol_old_rt = f90wrap_nexvol_old_rt
end subroutine f90wrap_gen__set__nexvol_old_rt

subroutine f90wrap_gen__get__idetail_rt(f90wrap_idetail_rt)
    use gen, only: gen_idetail_rt => idetail_rt
    implicit none
    integer(4), intent(out) :: f90wrap_idetail_rt
    
    f90wrap_idetail_rt = gen_idetail_rt
end subroutine f90wrap_gen__get__idetail_rt

subroutine f90wrap_gen__set__idetail_rt(f90wrap_idetail_rt)
    use gen, only: gen_idetail_rt => idetail_rt
    implicit none
    integer(4), intent(in) :: f90wrap_idetail_rt
    
    gen_idetail_rt = f90wrap_idetail_rt
end subroutine f90wrap_gen__set__idetail_rt

subroutine f90wrap_gen__get__rcm_ordering_rt(f90wrap_rcm_ordering_rt)
    use gen, only: gen_rcm_ordering_rt => rcm_ordering_rt
    implicit none
    logical, intent(out) :: f90wrap_rcm_ordering_rt
    
    f90wrap_rcm_ordering_rt = gen_rcm_ordering_rt
end subroutine f90wrap_gen__get__rcm_ordering_rt

subroutine f90wrap_gen__set__rcm_ordering_rt(f90wrap_rcm_ordering_rt)
    use gen, only: gen_rcm_ordering_rt => rcm_ordering_rt
    implicit none
    logical, intent(in) :: f90wrap_rcm_ordering_rt
    
    gen_rcm_ordering_rt = f90wrap_rcm_ordering_rt
end subroutine f90wrap_gen__set__rcm_ordering_rt

subroutine f90wrap_gen__array__cfluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cfluxin => cfluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cfluxin)) then
        dshape(1:1) = shape(gen_cfluxin)
        dloc = loc(gen_cfluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cfluxin

subroutine f90wrap_gen__array__cfluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cfluxout => cfluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cfluxout)) then
        dshape(1:1) = shape(gen_cfluxout)
        dloc = loc(gen_cfluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cfluxout

subroutine f90wrap_gen__array__gfluxtbdy(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gfluxtbdy => gfluxtbdy
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gfluxtbdy)) then
        dshape(1:1) = shape(gen_gfluxtbdy)
        dloc = loc(gen_gfluxtbdy)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gfluxtbdy

subroutine f90wrap_gen__array__gfluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gfluxin => gfluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gfluxin)) then
        dshape(1:1) = shape(gen_gfluxin)
        dloc = loc(gen_gfluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gfluxin

subroutine f90wrap_gen__array__gfluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gfluxout => gfluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gfluxout)) then
        dshape(1:1) = shape(gen_gfluxout)
        dloc = loc(gen_gfluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gfluxout

subroutine f90wrap_gen__array__gafluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gafluxin => gafluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gafluxin)) then
        dshape(1:1) = shape(gen_gafluxin)
        dloc = loc(gen_gafluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gafluxin

subroutine f90wrap_gen__array__gafluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gafluxout => gafluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gafluxout)) then
        dshape(1:1) = shape(gen_gafluxout)
        dloc = loc(gen_gafluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gafluxout

subroutine f90wrap_gen__array__cstordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cstordiff => cstordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cstordiff)) then
        dshape(1:1) = shape(gen_cstordiff)
        dloc = loc(gen_cstordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cstordiff

subroutine f90wrap_gen__array__gdegas(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gdegas => gdegas
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gdegas)) then
        dshape(1:1) = shape(gen_gdegas)
        dloc = loc(gen_gdegas)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gdegas

subroutine f90wrap_gen__array__gstordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gstordiff => gstordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gstordiff)) then
        dshape(1:1) = shape(gen_gstordiff)
        dloc = loc(gen_gstordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gstordiff

subroutine f90wrap_gen__array__ordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_ordiff => ordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_ordiff)) then
        dshape(1:1) = shape(gen_ordiff)
        dloc = loc(gen_ordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__ordiff

subroutine f90wrap_gen__array__dpdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dpdiff => dpdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dpdiff)) then
        dshape(1:1) = shape(gen_dpdiff)
        dloc = loc(gen_dpdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dpdiff

subroutine f90wrap_gen__array__gdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gdiff => gdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gdiff)) then
        dshape(1:1) = shape(gen_gdiff)
        dloc = loc(gen_gdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gdiff

subroutine f90wrap_gen__array__amass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_amass => amass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_amass)) then
        dshape(1:1) = shape(gen_amass)
        dloc = loc(gen_amass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__amass

subroutine f90wrap_gen__array__tmass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_tmass => tmass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_tmass)) then
        dshape(1:1) = shape(gen_tmass)
        dloc = loc(gen_tmass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__tmass

subroutine f90wrap_gen__array__cmass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmass => cmass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cmass)) then
        dshape(1:1) = shape(gen_cmass)
        dloc = loc(gen_cmass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmass

subroutine f90wrap_gen__array__gmass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gmass => gmass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gmass)) then
        dshape(1:1) = shape(gen_gmass)
        dloc = loc(gen_gmass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gmass

subroutine f90wrap_gen__array__cmmass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmmass => cmmass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cmmass)) then
        dshape(1:1) = shape(gen_cmmass)
        dloc = loc(gen_cmmass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmmass

subroutine f90wrap_gen__array__csbmass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_csbmass => csbmass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_csbmass)) then
        dshape(1:1) = shape(gen_csbmass)
        dloc = loc(gen_csbmass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__csbmass

subroutine f90wrap_gen__array__csbmass_c(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_csbmass_c => csbmass_c
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_csbmass_c)) then
        dshape(1:1) = shape(gen_csbmass_c)
        dloc = loc(gen_csbmass_c)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__csbmass_c

subroutine f90wrap_gen__array__cculabsbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cculabsbal => cculabsbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cculabsbal)) then
        dshape(1:1) = shape(gen_cculabsbal)
        dloc = loc(gen_cculabsbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cculabsbal

subroutine f90wrap_gen__array__cculrelbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cculrelbal => cculrelbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cculrelbal)) then
        dshape(1:1) = shape(gen_cculrelbal)
        dloc = loc(gen_cculrelbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cculrelbal

subroutine f90wrap_gen__array__gculabsbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gculabsbal => gculabsbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gculabsbal)) then
        dshape(1:1) = shape(gen_gculabsbal)
        dloc = loc(gen_gculabsbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gculabsbal

subroutine f90wrap_gen__array__gculrelbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_gculrelbal => gculrelbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_gculrelbal)) then
        dshape(1:1) = shape(gen_gculrelbal)
        dloc = loc(gen_gculrelbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__gculrelbal

subroutine f90wrap_gen__array__cmculabsbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmculabsbal => cmculabsbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cmculabsbal)) then
        dshape(1:1) = shape(gen_cmculabsbal)
        dloc = loc(gen_cmculabsbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmculabsbal

subroutine f90wrap_gen__array__cmculrelbal(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cmculrelbal => cmculrelbal
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cmculrelbal)) then
        dshape(1:1) = shape(gen_cmculrelbal)
        dloc = loc(gen_cmculrelbal)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cmculrelbal

subroutine f90wrap_gen__array__smass(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_smass => smass
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_smass)) then
        dshape(1:1) = shape(gen_smass)
        dloc = loc(gen_smass)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__smass

subroutine f90wrap_gen__array__sbdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sbdiff => sbdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sbdiff)) then
        dshape(1:1) = shape(gen_sbdiff)
        dloc = loc(gen_sbdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sbdiff

subroutine f90wrap_gen__array__rateaqtot(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_rateaqtot => rateaqtot
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_rateaqtot)) then
        dshape(1:1) = shape(gen_rateaqtot)
        dloc = loc(gen_rateaqtot)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__rateaqtot

subroutine f90wrap_gen__array__contaqtot(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_contaqtot => contaqtot
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_contaqtot)) then
        dshape(1:1) = shape(gen_contaqtot)
        dloc = loc(gen_contaqtot)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__contaqtot

subroutine f90wrap_gen__array__contmintot(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_contmintot => contmintot
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_contmintot)) then
        dshape(1:1) = shape(gen_contmintot)
        dloc = loc(gen_contmintot)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__contmintot

subroutine f90wrap_gen__array__totcfluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcfluxin => totcfluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totcfluxin)) then
        dshape(1:1) = shape(gen_totcfluxin)
        dloc = loc(gen_totcfluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcfluxin

subroutine f90wrap_gen__array__totcfluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcfluxout => totcfluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totcfluxout)) then
        dshape(1:1) = shape(gen_totcfluxout)
        dloc = loc(gen_totcfluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcfluxout

subroutine f90wrap_gen__array__totcstordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totcstordiff => totcstordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totcstordiff)) then
        dshape(1:1) = shape(gen_totcstordiff)
        dloc = loc(gen_totcstordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totcstordiff

subroutine f90wrap_gen__array__totordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totordiff => totordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totordiff)) then
        dshape(1:1) = shape(gen_totordiff)
        dloc = loc(gen_totordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totordiff

subroutine f90wrap_gen__array__totdpdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totdpdiff => totdpdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totdpdiff)) then
        dshape(1:1) = shape(gen_totdpdiff)
        dloc = loc(gen_totdpdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totdpdiff

subroutine f90wrap_gen__array__totgdegas(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgdegas => totgdegas
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgdegas)) then
        dshape(1:1) = shape(gen_totgdegas)
        dloc = loc(gen_totgdegas)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgdegas

subroutine f90wrap_gen__array__totgdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgdiff => totgdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgdiff)) then
        dshape(1:1) = shape(gen_totgdiff)
        dloc = loc(gen_totgdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgdiff

subroutine f90wrap_gen__array__totgfluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgfluxin => totgfluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgfluxin)) then
        dshape(1:1) = shape(gen_totgfluxin)
        dloc = loc(gen_totgfluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgfluxin

subroutine f90wrap_gen__array__totgfluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgfluxout => totgfluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgfluxout)) then
        dshape(1:1) = shape(gen_totgfluxout)
        dloc = loc(gen_totgfluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgfluxout

subroutine f90wrap_gen__array__totgafluxin(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgafluxin => totgafluxin
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgafluxin)) then
        dshape(1:1) = shape(gen_totgafluxin)
        dloc = loc(gen_totgafluxin)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgafluxin

subroutine f90wrap_gen__array__totgafluxout(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgafluxout => totgafluxout
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgafluxout)) then
        dshape(1:1) = shape(gen_totgafluxout)
        dloc = loc(gen_totgafluxout)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgafluxout

subroutine f90wrap_gen__array__totgstordiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totgstordiff => totgstordiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totgstordiff)) then
        dshape(1:1) = shape(gen_totgstordiff)
        dloc = loc(gen_totgstordiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totgstordiff

subroutine f90wrap_gen__array__totsbdiff(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totsbdiff => totsbdiff
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totsbdiff)) then
        dshape(1:1) = shape(gen_totsbdiff)
        dloc = loc(gen_totsbdiff)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totsbdiff

subroutine f90wrap_gen__array__dpdiffp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dpdiffp => dpdiffp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dpdiffp)) then
        dshape(1:1) = shape(gen_dpdiffp)
        dloc = loc(gen_dpdiffp)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dpdiffp

subroutine f90wrap_gen__array__totdpdiffp(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_totdpdiffp => totdpdiffp
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_totdpdiffp)) then
        dshape(1:1) = shape(gen_totdpdiffp)
        dloc = loc(gen_totdpdiffp)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__totdpdiffp

subroutine f90wrap_gen__get__sw_star(f90wrap_sw_star)
    use gen, only: gen_sw_star => sw_star
    implicit none
    real(8), intent(out) :: f90wrap_sw_star
    
    f90wrap_sw_star = gen_sw_star
end subroutine f90wrap_gen__get__sw_star

subroutine f90wrap_gen__set__sw_star(f90wrap_sw_star)
    use gen, only: gen_sw_star => sw_star
    implicit none
    real(8), intent(in) :: f90wrap_sw_star
    
    gen_sw_star = f90wrap_sw_star
end subroutine f90wrap_gen__set__sw_star

subroutine f90wrap_gen__get__uvslim(f90wrap_uvslim)
    use gen, only: gen_uvslim => uvslim
    implicit none
    real(8), intent(out) :: f90wrap_uvslim
    
    f90wrap_uvslim = gen_uvslim
end subroutine f90wrap_gen__get__uvslim

subroutine f90wrap_gen__set__uvslim(f90wrap_uvslim)
    use gen, only: gen_uvslim => uvslim
    implicit none
    real(8), intent(in) :: f90wrap_uvslim
    
    gen_uvslim = f90wrap_uvslim
end subroutine f90wrap_gen__set__uvslim

subroutine f90wrap_gen__get__iter_seep(f90wrap_iter_seep)
    use gen, only: gen_iter_seep => iter_seep
    implicit none
    integer(4), intent(out) :: f90wrap_iter_seep
    
    f90wrap_iter_seep = gen_iter_seep
end subroutine f90wrap_gen__get__iter_seep

subroutine f90wrap_gen__set__iter_seep(f90wrap_iter_seep)
    use gen, only: gen_iter_seep => iter_seep
    implicit none
    integer(4), intent(in) :: f90wrap_iter_seep
    
    gen_iter_seep = f90wrap_iter_seep
end subroutine f90wrap_gen__set__iter_seep

subroutine f90wrap_gen__get__itseep_tot(f90wrap_itseep_tot)
    use gen, only: gen_itseep_tot => itseep_tot
    implicit none
    integer(4), intent(out) :: f90wrap_itseep_tot
    
    f90wrap_itseep_tot = gen_itseep_tot
end subroutine f90wrap_gen__get__itseep_tot

subroutine f90wrap_gen__set__itseep_tot(f90wrap_itseep_tot)
    use gen, only: gen_itseep_tot => itseep_tot
    implicit none
    integer(4), intent(in) :: f90wrap_itseep_tot
    
    gen_itseep_tot = f90wrap_itseep_tot
end subroutine f90wrap_gen__set__itseep_tot

subroutine f90wrap_gen__get__itsolvtot_vs(f90wrap_itsolvtot_vs)
    use gen, only: gen_itsolvtot_vs => itsolvtot_vs
    implicit none
    integer(4), intent(out) :: f90wrap_itsolvtot_vs
    
    f90wrap_itsolvtot_vs = gen_itsolvtot_vs
end subroutine f90wrap_gen__get__itsolvtot_vs

subroutine f90wrap_gen__set__itsolvtot_vs(f90wrap_itsolvtot_vs)
    use gen, only: gen_itsolvtot_vs => itsolvtot_vs
    implicit none
    integer(4), intent(in) :: f90wrap_itsolvtot_vs
    
    gen_itsolvtot_vs = f90wrap_itsolvtot_vs
end subroutine f90wrap_gen__set__itsolvtot_vs

subroutine f90wrap_gen__get__nseep_first(f90wrap_nseep_first)
    use gen, only: gen_nseep_first => nseep_first
    implicit none
    integer(4), intent(out) :: f90wrap_nseep_first
    
    f90wrap_nseep_first = gen_nseep_first
end subroutine f90wrap_gen__get__nseep_first

subroutine f90wrap_gen__set__nseep_first(f90wrap_nseep_first)
    use gen, only: gen_nseep_first => nseep_first
    implicit none
    integer(4), intent(in) :: f90wrap_nseep_first
    
    gen_nseep_first = f90wrap_nseep_first
end subroutine f90wrap_gen__set__nseep_first

subroutine f90wrap_gen__get__pressure_head(f90wrap_pressure_head)
    use gen, only: gen_pressure_head => pressure_head
    implicit none
    logical, intent(out) :: f90wrap_pressure_head
    
    f90wrap_pressure_head = gen_pressure_head
end subroutine f90wrap_gen__get__pressure_head

subroutine f90wrap_gen__set__pressure_head(f90wrap_pressure_head)
    use gen, only: gen_pressure_head => pressure_head
    implicit none
    logical, intent(in) :: f90wrap_pressure_head
    
    gen_pressure_head = f90wrap_pressure_head
end subroutine f90wrap_gen__set__pressure_head

subroutine f90wrap_gen__get__hydraulic_head(f90wrap_hydraulic_head)
    use gen, only: gen_hydraulic_head => hydraulic_head
    implicit none
    logical, intent(out) :: f90wrap_hydraulic_head
    
    f90wrap_hydraulic_head = gen_hydraulic_head
end subroutine f90wrap_gen__get__hydraulic_head

subroutine f90wrap_gen__set__hydraulic_head(f90wrap_hydraulic_head)
    use gen, only: gen_hydraulic_head => hydraulic_head
    implicit none
    logical, intent(in) :: f90wrap_hydraulic_head
    
    gen_hydraulic_head = f90wrap_hydraulic_head
end subroutine f90wrap_gen__set__hydraulic_head

subroutine f90wrap_gen__get__seepage_face(f90wrap_seepage_face)
    use gen, only: gen_seepage_face => seepage_face
    implicit none
    logical, intent(out) :: f90wrap_seepage_face
    
    f90wrap_seepage_face = gen_seepage_face
end subroutine f90wrap_gen__get__seepage_face

subroutine f90wrap_gen__set__seepage_face(f90wrap_seepage_face)
    use gen, only: gen_seepage_face => seepage_face
    implicit none
    logical, intent(in) :: f90wrap_seepage_face
    
    gen_seepage_face = f90wrap_seepage_face
end subroutine f90wrap_gen__set__seepage_face

subroutine f90wrap_gen__get__seep_iter(f90wrap_seep_iter)
    use gen, only: gen_seep_iter => seep_iter
    implicit none
    logical, intent(out) :: f90wrap_seep_iter
    
    f90wrap_seep_iter = gen_seep_iter
end subroutine f90wrap_gen__get__seep_iter

subroutine f90wrap_gen__set__seep_iter(f90wrap_seep_iter)
    use gen, only: gen_seep_iter => seep_iter
    implicit none
    logical, intent(in) :: f90wrap_seep_iter
    
    gen_seep_iter = f90wrap_seep_iter
end subroutine f90wrap_gen__set__seep_iter

subroutine f90wrap_gen__get__mass_balance_vs(f90wrap_mass_balance_vs)
    use gen, only: gen_mass_balance_vs => mass_balance_vs
    implicit none
    logical, intent(out) :: f90wrap_mass_balance_vs
    
    f90wrap_mass_balance_vs = gen_mass_balance_vs
end subroutine f90wrap_gen__get__mass_balance_vs

subroutine f90wrap_gen__set__mass_balance_vs(f90wrap_mass_balance_vs)
    use gen, only: gen_mass_balance_vs => mass_balance_vs
    implicit none
    logical, intent(in) :: f90wrap_mass_balance_vs
    
    gen_mass_balance_vs = f90wrap_mass_balance_vs
end subroutine f90wrap_gen__set__mass_balance_vs

subroutine f90wrap_gen__array__uvsnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_uvsnew => uvsnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_uvsnew)) then
        dshape(1:1) = shape(gen_uvsnew)
        dloc = loc(gen_uvsnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__uvsnew

subroutine f90wrap_gen__array__uvsold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_uvsold => uvsold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_uvsold)) then
        dshape(1:1) = shape(gen_uvsold)
        dloc = loc(gen_uvsold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__uvsold

subroutine f90wrap_gen__array__uvsinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_uvsinc => uvsinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_uvsinc)) then
        dshape(1:1) = shape(gen_uvsinc)
        dloc = loc(gen_uvsinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__uvsinc

subroutine f90wrap_gen__array__hhead(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_hhead => hhead
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_hhead)) then
        dshape(1:1) = shape(gen_hhead)
        dloc = loc(gen_hhead)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__hhead

subroutine f90wrap_gen__array__saold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_saold => saold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_saold)) then
        dshape(1:1) = shape(gen_saold)
        dloc = loc(gen_saold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__saold

subroutine f90wrap_gen__array__sanew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sanew => sanew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sanew)) then
        dshape(1:1) = shape(gen_sanew)
        dloc = loc(gen_sanew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sanew

subroutine f90wrap_gen__array__sgold(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sgold => sgold
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sgold)) then
        dshape(1:1) = shape(gen_sgold)
        dloc = loc(gen_sgold)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sgold

subroutine f90wrap_gen__array__sgnew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sgnew => sgnew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sgnew)) then
        dshape(1:1) = shape(gen_sgnew)
        dloc = loc(gen_sgnew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sgnew

subroutine f90wrap_gen__array__sainc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sainc => sainc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sainc)) then
        dshape(1:1) = shape(gen_sainc)
        dloc = loc(gen_sainc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sainc

subroutine f90wrap_gen__array__sonew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_sonew => sonew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_sonew)) then
        dshape(1:1) = shape(gen_sonew)
        dloc = loc(gen_sonew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__sonew

subroutine f90wrap_gen__array__relperm(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_relperm => relperm
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_relperm)) then
        dshape(1:1) = shape(gen_relperm)
        dloc = loc(gen_relperm)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__relperm

subroutine f90wrap_gen__array__relpinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_relpinc => relpinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_relpinc)) then
        dshape(1:1) = shape(gen_relpinc)
        dloc = loc(gen_relpinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__relpinc

subroutine f90wrap_gen__array__pornew(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_pornew => pornew
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_pornew)) then
        dshape(1:1) = shape(gen_pornew)
        dloc = loc(gen_pornew)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__pornew

subroutine f90wrap_gen__array__por_init(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_por_init => por_init
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_por_init)) then
        dshape(1:1) = shape(gen_por_init)
        dloc = loc(gen_por_init)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__por_init

subroutine f90wrap_gen__array__perm_fac(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_perm_fac => perm_fac
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_perm_fac)) then
        dshape(1:1) = shape(gen_perm_fac)
        dloc = loc(gen_perm_fac)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__perm_fac

subroutine f90wrap_gen__array__cinfvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfvs => cinfvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfvs)) then
        dshape(1:1) = shape(gen_cinfvs)
        dloc = loc(gen_cinfvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfvs

subroutine f90wrap_gen__array__permij(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_permij => permij
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_permij)) then
        dshape(1:1) = shape(gen_permij)
        dloc = loc(gen_permij)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__permij

subroutine f90wrap_gen__array__relpermg(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_relpermg => relpermg
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_relpermg)) then
        dshape(1:1) = shape(gen_relpermg)
        dloc = loc(gen_relpermg)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__relpermg

subroutine f90wrap_gen__array__cinfvs_a(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfvs_a => cinfvs_a
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfvs_a)) then
        dshape(1:1) = shape(gen_cinfvs_a)
        dloc = loc(gen_cinfvs_a)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfvs_a

subroutine f90wrap_gen__array__cinfvs_g(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_cinfvs_g => cinfvs_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_cinfvs_g)) then
        dshape(1:1) = shape(gen_cinfvs_g)
        dloc = loc(gen_cinfvs_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__cinfvs_g

subroutine f90wrap_gen__array__tauivol(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_tauivol => tauivol
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_tauivol)) then
        dshape(1:1) = shape(gen_tauivol)
        dloc = loc(gen_tauivol)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__tauivol

subroutine f90wrap_gen__array__mpropvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_mpropvs => mpropvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_mpropvs)) then
        dshape(1:1) = shape(gen_mpropvs)
        dloc = loc(gen_mpropvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__mpropvs

subroutine f90wrap_gen__array__binev(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_binev => binev
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_binev)) then
        dshape(1:1) = shape(gen_binev)
        dloc = loc(gen_binev)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__binev

subroutine f90wrap_gen__array__bint(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bint => bint
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_bint)) then
        dshape(1:1) = shape(gen_bint)
        dloc = loc(gen_bint)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bint

subroutine f90wrap_gen__array__qroot(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_qroot => qroot
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_qroot)) then
        dshape(1:1) = shape(gen_qroot)
        dloc = loc(gen_qroot)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__qroot

subroutine f90wrap_gen__array__qrootinc(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_qrootinc => qrootinc
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_qrootinc)) then
        dshape(1:1) = shape(gen_qrootinc)
        dloc = loc(gen_qrootinc)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__qrootinc

subroutine f90wrap_gen__array__dqroot(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_dqroot => dqroot
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_dqroot)) then
        dshape(1:1) = shape(gen_dqroot)
        dloc = loc(gen_dqroot)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__dqroot

subroutine f90wrap_gen__get__totvsmass(f90wrap_totvsmass)
    use gen, only: gen_totvsmass => totvsmass
    implicit none
    real(8), intent(out) :: f90wrap_totvsmass
    
    f90wrap_totvsmass = gen_totvsmass
end subroutine f90wrap_gen__get__totvsmass

subroutine f90wrap_gen__set__totvsmass(f90wrap_totvsmass)
    use gen, only: gen_totvsmass => totvsmass
    implicit none
    real(8), intent(in) :: f90wrap_totvsmass
    
    gen_totvsmass = f90wrap_totvsmass
end subroutine f90wrap_gen__set__totvsmass

subroutine f90wrap_gen__get__culabsbalvs(f90wrap_culabsbalvs)
    use gen, only: gen_culabsbalvs => culabsbalvs
    implicit none
    real(8), intent(out) :: f90wrap_culabsbalvs
    
    f90wrap_culabsbalvs = gen_culabsbalvs
end subroutine f90wrap_gen__get__culabsbalvs

subroutine f90wrap_gen__set__culabsbalvs(f90wrap_culabsbalvs)
    use gen, only: gen_culabsbalvs => culabsbalvs
    implicit none
    real(8), intent(in) :: f90wrap_culabsbalvs
    
    gen_culabsbalvs = f90wrap_culabsbalvs
end subroutine f90wrap_gen__set__culabsbalvs

subroutine f90wrap_gen__get__time_bcvs(f90wrap_time_bcvs)
    use gen, only: gen_time_bcvs => time_bcvs
    implicit none
    real(8), intent(out) :: f90wrap_time_bcvs
    
    f90wrap_time_bcvs = gen_time_bcvs
end subroutine f90wrap_gen__get__time_bcvs

subroutine f90wrap_gen__set__time_bcvs(f90wrap_time_bcvs)
    use gen, only: gen_time_bcvs => time_bcvs
    implicit none
    real(8), intent(in) :: f90wrap_time_bcvs
    
    gen_time_bcvs = f90wrap_time_bcvs
end subroutine f90wrap_gen__set__time_bcvs

subroutine f90wrap_gen__array__bcondvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bcondvs => bcondvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_bcondvs)) then
        dshape(1:1) = shape(gen_bcondvs)
        dloc = loc(gen_bcondvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bcondvs

subroutine f90wrap_gen__array__iabvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iabvs => iabvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iabvs)) then
        dshape(1:1) = shape(gen_iabvs)
        dloc = loc(gen_iabvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iabvs

subroutine f90wrap_gen__get__nbvs(f90wrap_nbvs)
    use gen, only: gen_nbvs => nbvs
    implicit none
    integer(4), intent(out) :: f90wrap_nbvs
    
    f90wrap_nbvs = gen_nbvs
end subroutine f90wrap_gen__get__nbvs

subroutine f90wrap_gen__set__nbvs(f90wrap_nbvs)
    use gen, only: gen_nbvs => nbvs
    implicit none
    integer(4), intent(in) :: f90wrap_nbvs
    
    gen_nbvs = f90wrap_nbvs
end subroutine f90wrap_gen__set__nbvs

subroutine f90wrap_gen__get__ibcvs(f90wrap_ibcvs)
    use gen, only: gen_ibcvs => ibcvs
    implicit none
    integer(4), intent(out) :: f90wrap_ibcvs
    
    f90wrap_ibcvs = gen_ibcvs
end subroutine f90wrap_gen__get__ibcvs

subroutine f90wrap_gen__set__ibcvs(f90wrap_ibcvs)
    use gen, only: gen_ibcvs => ibcvs
    implicit none
    integer(4), intent(in) :: f90wrap_ibcvs
    
    gen_ibcvs = f90wrap_ibcvs
end subroutine f90wrap_gen__set__ibcvs

subroutine f90wrap_gen__get__ibcrt(f90wrap_ibcrt)
    use gen, only: gen_ibcrt => ibcrt
    implicit none
    integer(4), intent(out) :: f90wrap_ibcrt
    
    f90wrap_ibcrt = gen_ibcrt
end subroutine f90wrap_gen__get__ibcrt

subroutine f90wrap_gen__set__ibcrt(f90wrap_ibcrt)
    use gen, only: gen_ibcrt => ibcrt
    implicit none
    integer(4), intent(in) :: f90wrap_ibcrt
    
    gen_ibcrt = f90wrap_ibcrt
end subroutine f90wrap_gen__set__ibcrt

subroutine f90wrap_gen__get__update_bcvs(f90wrap_update_bcvs)
    use gen, only: gen_update_bcvs => update_bcvs
    implicit none
    logical, intent(out) :: f90wrap_update_bcvs
    
    f90wrap_update_bcvs = gen_update_bcvs
end subroutine f90wrap_gen__get__update_bcvs

subroutine f90wrap_gen__set__update_bcvs(f90wrap_update_bcvs)
    use gen, only: gen_update_bcvs => update_bcvs
    implicit none
    logical, intent(in) :: f90wrap_update_bcvs
    
    gen_update_bcvs = f90wrap_update_bcvs
end subroutine f90wrap_gen__set__update_bcvs

subroutine f90wrap_gen__array__vsflux(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_vsflux => vsflux
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_vsflux)) then
        dshape(1:1) = shape(gen_vsflux)
        dloc = loc(gen_vsflux)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__vsflux

subroutine f90wrap_gen__get__dinc_vs(f90wrap_dinc_vs)
    use gen, only: gen_dinc_vs => dinc_vs
    implicit none
    real(8), intent(out) :: f90wrap_dinc_vs
    
    f90wrap_dinc_vs = gen_dinc_vs
end subroutine f90wrap_gen__get__dinc_vs

subroutine f90wrap_gen__set__dinc_vs(f90wrap_dinc_vs)
    use gen, only: gen_dinc_vs => dinc_vs
    implicit none
    real(8), intent(in) :: f90wrap_dinc_vs
    
    gen_dinc_vs = f90wrap_dinc_vs
end subroutine f90wrap_gen__set__dinc_vs

subroutine f90wrap_gen__get__tol_vs(f90wrap_tol_vs)
    use gen, only: gen_tol_vs => tol_vs
    implicit none
    real(8), intent(out) :: f90wrap_tol_vs
    
    f90wrap_tol_vs = gen_tol_vs
end subroutine f90wrap_gen__get__tol_vs

subroutine f90wrap_gen__set__tol_vs(f90wrap_tol_vs)
    use gen, only: gen_tol_vs => tol_vs
    implicit none
    real(8), intent(in) :: f90wrap_tol_vs
    
    gen_tol_vs = f90wrap_tol_vs
end subroutine f90wrap_gen__set__tol_vs

subroutine f90wrap_gen__get__uvsmaxold(f90wrap_uvsmaxold)
    use gen, only: gen_uvsmaxold => uvsmaxold
    implicit none
    real(8), intent(out) :: f90wrap_uvsmaxold
    
    f90wrap_uvsmaxold = gen_uvsmaxold
end subroutine f90wrap_gen__get__uvsmaxold

subroutine f90wrap_gen__set__uvsmaxold(f90wrap_uvsmaxold)
    use gen, only: gen_uvsmaxold => uvsmaxold
    implicit none
    real(8), intent(in) :: f90wrap_uvsmaxold
    
    gen_uvsmaxold = f90wrap_uvsmaxold
end subroutine f90wrap_gen__set__uvsmaxold

subroutine f90wrap_gen__get__relfacold(f90wrap_relfacold)
    use gen, only: gen_relfacold => relfacold
    implicit none
    real(8), intent(out) :: f90wrap_relfacold
    
    f90wrap_relfacold = gen_relfacold
end subroutine f90wrap_gen__get__relfacold

subroutine f90wrap_gen__set__relfacold(f90wrap_relfacold)
    use gen, only: gen_relfacold => relfacold
    implicit none
    real(8), intent(in) :: f90wrap_relfacold
    
    gen_relfacold = f90wrap_relfacold
end subroutine f90wrap_gen__set__relfacold

subroutine f90wrap_gen__get__srelfac_vs(f90wrap_srelfac_vs)
    use gen, only: gen_srelfac_vs => srelfac_vs
    implicit none
    real(8), intent(out) :: f90wrap_srelfac_vs
    
    f90wrap_srelfac_vs = gen_srelfac_vs
end subroutine f90wrap_gen__get__srelfac_vs

subroutine f90wrap_gen__set__srelfac_vs(f90wrap_srelfac_vs)
    use gen, only: gen_srelfac_vs => srelfac_vs
    implicit none
    real(8), intent(in) :: f90wrap_srelfac_vs
    
    gen_srelfac_vs = f90wrap_srelfac_vs
end subroutine f90wrap_gen__set__srelfac_vs

subroutine f90wrap_gen__get__maxit_vs(f90wrap_maxit_vs)
    use gen, only: gen_maxit_vs => maxit_vs
    implicit none
    integer(4), intent(out) :: f90wrap_maxit_vs
    
    f90wrap_maxit_vs = gen_maxit_vs
end subroutine f90wrap_gen__get__maxit_vs

subroutine f90wrap_gen__set__maxit_vs(f90wrap_maxit_vs)
    use gen, only: gen_maxit_vs => maxit_vs
    implicit none
    integer(4), intent(in) :: f90wrap_maxit_vs
    
    gen_maxit_vs = f90wrap_maxit_vs
end subroutine f90wrap_gen__set__maxit_vs

subroutine f90wrap_gen__get__iter_vs(f90wrap_iter_vs)
    use gen, only: gen_iter_vs => iter_vs
    implicit none
    integer(4), intent(out) :: f90wrap_iter_vs
    
    f90wrap_iter_vs = gen_iter_vs
end subroutine f90wrap_gen__get__iter_vs

subroutine f90wrap_gen__set__iter_vs(f90wrap_iter_vs)
    use gen, only: gen_iter_vs => iter_vs
    implicit none
    integer(4), intent(in) :: f90wrap_iter_vs
    
    gen_iter_vs = f90wrap_iter_vs
end subroutine f90wrap_gen__set__iter_vs

subroutine f90wrap_gen__get__ittot_vs(f90wrap_ittot_vs)
    use gen, only: gen_ittot_vs => ittot_vs
    implicit none
    integer(4), intent(out) :: f90wrap_ittot_vs
    
    f90wrap_ittot_vs = gen_ittot_vs
end subroutine f90wrap_gen__get__ittot_vs

subroutine f90wrap_gen__set__ittot_vs(f90wrap_ittot_vs)
    use gen, only: gen_ittot_vs => ittot_vs
    implicit none
    integer(4), intent(in) :: f90wrap_ittot_vs
    
    gen_ittot_vs = f90wrap_ittot_vs
end subroutine f90wrap_gen__set__ittot_vs

subroutine f90wrap_gen__get__upstream(f90wrap_upstream)
    use gen, only: gen_upstream => upstream
    implicit none
    logical, intent(out) :: f90wrap_upstream
    
    f90wrap_upstream = gen_upstream
end subroutine f90wrap_gen__get__upstream

subroutine f90wrap_gen__set__upstream(f90wrap_upstream)
    use gen, only: gen_upstream => upstream
    implicit none
    logical, intent(in) :: f90wrap_upstream
    
    gen_upstream = f90wrap_upstream
end subroutine f90wrap_gen__set__upstream

subroutine f90wrap_gen__get__under_relax(f90wrap_under_relax)
    use gen, only: gen_under_relax => under_relax
    implicit none
    logical, intent(out) :: f90wrap_under_relax
    
    f90wrap_under_relax = gen_under_relax
end subroutine f90wrap_gen__get__under_relax

subroutine f90wrap_gen__set__under_relax(f90wrap_under_relax)
    use gen, only: gen_under_relax => under_relax
    implicit none
    logical, intent(in) :: f90wrap_under_relax
    
    gen_under_relax = f90wrap_under_relax
end subroutine f90wrap_gen__set__under_relax

subroutine f90wrap_gen__get__comp_relax(f90wrap_comp_relax)
    use gen, only: gen_comp_relax => comp_relax
    implicit none
    logical, intent(out) :: f90wrap_comp_relax
    
    f90wrap_comp_relax = gen_comp_relax
end subroutine f90wrap_gen__get__comp_relax

subroutine f90wrap_gen__set__comp_relax(f90wrap_comp_relax)
    use gen, only: gen_comp_relax => comp_relax
    implicit none
    logical, intent(in) :: f90wrap_comp_relax
    
    gen_comp_relax = f90wrap_comp_relax
end subroutine f90wrap_gen__set__comp_relax

subroutine f90wrap_gen__array__avs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_avs => avs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_avs)) then
        dshape(1:1) = shape(gen_avs)
        dloc = loc(gen_avs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__avs

subroutine f90wrap_gen__array__bvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_bvs => bvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_bvs)) then
        dshape(1:1) = shape(gen_bvs)
        dloc = loc(gen_bvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__bvs

subroutine f90wrap_gen__array__uvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_uvs => uvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_uvs)) then
        dshape(1:1) = shape(gen_uvs)
        dloc = loc(gen_uvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__uvs

subroutine f90wrap_gen__array__resvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_resvs => resvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_resvs)) then
        dshape(1:1) = shape(gen_resvs)
        dloc = loc(gen_resvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__resvs

subroutine f90wrap_gen__array__afvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_afvs => afvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_afvs)) then
        dshape(1:1) = shape(gen_afvs)
        dloc = loc(gen_afvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__afvs

subroutine f90wrap_gen__get__restol_vs(f90wrap_restol_vs)
    use gen, only: gen_restol_vs => restol_vs
    implicit none
    real(8), intent(out) :: f90wrap_restol_vs
    
    f90wrap_restol_vs = gen_restol_vs
end subroutine f90wrap_gen__get__restol_vs

subroutine f90wrap_gen__set__restol_vs(f90wrap_restol_vs)
    use gen, only: gen_restol_vs => restol_vs
    implicit none
    real(8), intent(in) :: f90wrap_restol_vs
    
    gen_restol_vs = f90wrap_restol_vs
end subroutine f90wrap_gen__set__restol_vs

subroutine f90wrap_gen__get__deltol_vs(f90wrap_deltol_vs)
    use gen, only: gen_deltol_vs => deltol_vs
    implicit none
    real(8), intent(out) :: f90wrap_deltol_vs
    
    f90wrap_deltol_vs = gen_deltol_vs
end subroutine f90wrap_gen__get__deltol_vs

subroutine f90wrap_gen__set__deltol_vs(f90wrap_deltol_vs)
    use gen, only: gen_deltol_vs => deltol_vs
    implicit none
    real(8), intent(in) :: f90wrap_deltol_vs
    
    gen_deltol_vs = f90wrap_deltol_vs
end subroutine f90wrap_gen__set__deltol_vs

subroutine f90wrap_gen__array__iavs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iavs => iavs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iavs)) then
        dshape(1:1) = shape(gen_iavs)
        dloc = loc(gen_iavs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iavs

subroutine f90wrap_gen__array__javs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_javs => javs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_javs)) then
        dshape(1:1) = shape(gen_javs)
        dloc = loc(gen_javs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__javs

subroutine f90wrap_gen__array__iafvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iafvs => iafvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iafvs)) then
        dshape(1:1) = shape(gen_iafvs)
        dloc = loc(gen_iafvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iafvs

subroutine f90wrap_gen__array__jafvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_jafvs => jafvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_jafvs)) then
        dshape(1:1) = shape(gen_jafvs)
        dloc = loc(gen_jafvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__jafvs

subroutine f90wrap_gen__array__iafdvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iafdvs => iafdvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iafdvs)) then
        dshape(1:1) = shape(gen_iafdvs)
        dloc = loc(gen_iafdvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iafdvs

subroutine f90wrap_gen__array__isymvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_isymvs => isymvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_isymvs)) then
        dshape(1:1) = shape(gen_isymvs)
        dloc = loc(gen_isymvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__isymvs

subroutine f90wrap_gen__array__lordervs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_lordervs => lordervs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_lordervs)) then
        dshape(1:1) = shape(gen_lordervs)
        dloc = loc(gen_lordervs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__lordervs

subroutine f90wrap_gen__array__invordvs(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_invordvs => invordvs
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_invordvs)) then
        dshape(1:1) = shape(gen_invordvs)
        dloc = loc(gen_invordvs)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__invordvs

subroutine f90wrap_gen__get__mnjavs(f90wrap_mnjavs)
    use gen, only: gen_mnjavs => mnjavs
    implicit none
    integer(4), intent(out) :: f90wrap_mnjavs
    
    f90wrap_mnjavs = gen_mnjavs
end subroutine f90wrap_gen__get__mnjavs

subroutine f90wrap_gen__set__mnjavs(f90wrap_mnjavs)
    use gen, only: gen_mnjavs => mnjavs
    implicit none
    integer(4), intent(in) :: f90wrap_mnjavs
    
    gen_mnjavs = f90wrap_mnjavs
end subroutine f90wrap_gen__set__mnjavs

subroutine f90wrap_gen__get__mnjafvs(f90wrap_mnjafvs)
    use gen, only: gen_mnjafvs => mnjafvs
    implicit none
    integer(4), intent(out) :: f90wrap_mnjafvs
    
    f90wrap_mnjafvs = gen_mnjafvs
end subroutine f90wrap_gen__get__mnjafvs

subroutine f90wrap_gen__set__mnjafvs(f90wrap_mnjafvs)
    use gen, only: gen_mnjafvs => mnjafvs
    implicit none
    integer(4), intent(in) :: f90wrap_mnjafvs
    
    gen_mnjafvs = f90wrap_mnjafvs
end subroutine f90wrap_gen__set__mnjafvs

subroutine f90wrap_gen__get__njavs(f90wrap_njavs)
    use gen, only: gen_njavs => njavs
    implicit none
    integer(4), intent(out) :: f90wrap_njavs
    
    f90wrap_njavs = gen_njavs
end subroutine f90wrap_gen__get__njavs

subroutine f90wrap_gen__set__njavs(f90wrap_njavs)
    use gen, only: gen_njavs => njavs
    implicit none
    integer(4), intent(in) :: f90wrap_njavs
    
    gen_njavs = f90wrap_njavs
end subroutine f90wrap_gen__set__njavs

subroutine f90wrap_gen__get__njafvs(f90wrap_njafvs)
    use gen, only: gen_njafvs => njafvs
    implicit none
    integer(4), intent(out) :: f90wrap_njafvs
    
    f90wrap_njafvs = gen_njafvs
end subroutine f90wrap_gen__get__njafvs

subroutine f90wrap_gen__set__njafvs(f90wrap_njafvs)
    use gen, only: gen_njafvs => njafvs
    implicit none
    integer(4), intent(in) :: f90wrap_njafvs
    
    gen_njafvs = f90wrap_njafvs
end subroutine f90wrap_gen__set__njafvs

subroutine f90wrap_gen__get__level_vs(f90wrap_level_vs)
    use gen, only: gen_level_vs => level_vs
    implicit none
    integer(4), intent(out) :: f90wrap_level_vs
    
    f90wrap_level_vs = gen_level_vs
end subroutine f90wrap_gen__get__level_vs

subroutine f90wrap_gen__set__level_vs(f90wrap_level_vs)
    use gen, only: gen_level_vs => level_vs
    implicit none
    integer(4), intent(in) :: f90wrap_level_vs
    
    gen_level_vs = f90wrap_level_vs
end subroutine f90wrap_gen__set__level_vs

subroutine f90wrap_gen__get__msolvit_vs(f90wrap_msolvit_vs)
    use gen, only: gen_msolvit_vs => msolvit_vs
    implicit none
    integer(4), intent(out) :: f90wrap_msolvit_vs
    
    f90wrap_msolvit_vs = gen_msolvit_vs
end subroutine f90wrap_gen__get__msolvit_vs

subroutine f90wrap_gen__set__msolvit_vs(f90wrap_msolvit_vs)
    use gen, only: gen_msolvit_vs => msolvit_vs
    implicit none
    integer(4), intent(in) :: f90wrap_msolvit_vs
    
    gen_msolvit_vs = f90wrap_msolvit_vs
end subroutine f90wrap_gen__set__msolvit_vs

subroutine f90wrap_gen__get__idetail_vs(f90wrap_idetail_vs)
    use gen, only: gen_idetail_vs => idetail_vs
    implicit none
    integer(4), intent(out) :: f90wrap_idetail_vs
    
    f90wrap_idetail_vs = gen_idetail_vs
end subroutine f90wrap_gen__get__idetail_vs

subroutine f90wrap_gen__set__idetail_vs(f90wrap_idetail_vs)
    use gen, only: gen_idetail_vs => idetail_vs
    implicit none
    integer(4), intent(in) :: f90wrap_idetail_vs
    
    gen_idetail_vs = f90wrap_idetail_vs
end subroutine f90wrap_gen__set__idetail_vs

subroutine f90wrap_gen__get__rcm_ordering_vs(f90wrap_rcm_ordering_vs)
    use gen, only: gen_rcm_ordering_vs => rcm_ordering_vs
    implicit none
    logical, intent(out) :: f90wrap_rcm_ordering_vs
    
    f90wrap_rcm_ordering_vs = gen_rcm_ordering_vs
end subroutine f90wrap_gen__get__rcm_ordering_vs

subroutine f90wrap_gen__set__rcm_ordering_vs(f90wrap_rcm_ordering_vs)
    use gen, only: gen_rcm_ordering_vs => rcm_ordering_vs
    implicit none
    logical, intent(in) :: f90wrap_rcm_ordering_vs
    
    gen_rcm_ordering_vs = f90wrap_rcm_ordering_vs
end subroutine f90wrap_gen__set__rcm_ordering_vs

subroutine f90wrap_gen__array__rwork(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_rwork => rwork
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 2
    dtype = 12
    if (allocated(gen_rwork)) then
        dshape(1:2) = shape(gen_rwork)
        dloc = loc(gen_rwork)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__rwork

subroutine f90wrap_gen__get__rnorm(f90wrap_rnorm)
    use gen, only: gen_rnorm => rnorm
    implicit none
    real(8), intent(out) :: f90wrap_rnorm
    
    f90wrap_rnorm = gen_rnorm
end subroutine f90wrap_gen__get__rnorm

subroutine f90wrap_gen__set__rnorm(f90wrap_rnorm)
    use gen, only: gen_rnorm => rnorm
    implicit none
    real(8), intent(in) :: f90wrap_rnorm
    
    gen_rnorm = f90wrap_rnorm
end subroutine f90wrap_gen__set__rnorm

subroutine f90wrap_gen__get__rmupdate(f90wrap_rmupdate)
    use gen, only: gen_rmupdate => rmupdate
    implicit none
    real(8), intent(out) :: f90wrap_rmupdate
    
    f90wrap_rmupdate = gen_rmupdate
end subroutine f90wrap_gen__get__rmupdate

subroutine f90wrap_gen__set__rmupdate(f90wrap_rmupdate)
    use gen, only: gen_rmupdate => rmupdate
    implicit none
    real(8), intent(in) :: f90wrap_rmupdate
    
    gen_rmupdate = f90wrap_rmupdate
end subroutine f90wrap_gen__set__rmupdate

subroutine f90wrap_gen__array__iwork(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_iwork => iwork
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_iwork)) then
        dshape(1:1) = shape(gen_iwork)
        dloc = loc(gen_iwork)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__iwork

subroutine f90wrap_gen__get__itsolv(f90wrap_itsolv)
    use gen, only: gen_itsolv => itsolv
    implicit none
    integer(4), intent(out) :: f90wrap_itsolv
    
    f90wrap_itsolv = gen_itsolv
end subroutine f90wrap_gen__get__itsolv

subroutine f90wrap_gen__set__itsolv(f90wrap_itsolv)
    use gen, only: gen_itsolv => itsolv
    implicit none
    integer(4), intent(in) :: f90wrap_itsolv
    
    gen_itsolv = f90wrap_itsolv
end subroutine f90wrap_gen__set__itsolv

subroutine f90wrap_gen__array__lwork(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_lwork => lwork
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(gen_lwork)) then
        dshape(1:1) = shape(gen_lwork)
        dloc = loc(gen_lwork)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__lwork

subroutine f90wrap_gen__get__skip(f90wrap_skip)
    use gen, only: gen_skip => skip
    implicit none
    integer(4), intent(out) :: f90wrap_skip
    
    f90wrap_skip = gen_skip
end subroutine f90wrap_gen__get__skip

subroutine f90wrap_gen__set__skip(f90wrap_skip)
    use gen, only: gen_skip => skip
    implicit none
    integer(4), intent(in) :: f90wrap_skip
    
    gen_skip = f90wrap_skip
end subroutine f90wrap_gen__set__skip

subroutine f90wrap_gen__get__nskip(f90wrap_nskip)
    use gen, only: gen_nskip => nskip
    implicit none
    integer(4), intent(out) :: f90wrap_nskip
    
    f90wrap_nskip = gen_nskip
end subroutine f90wrap_gen__get__nskip

subroutine f90wrap_gen__set__nskip(f90wrap_nskip)
    use gen, only: gen_nskip => nskip
    implicit none
    integer(4), intent(in) :: f90wrap_nskip
    
    gen_nskip = f90wrap_nskip
end subroutine f90wrap_gen__set__nskip

subroutine f90wrap_gen__get__chemical_water(f90wrap_chemical_water)
    use gen, only: gen_chemical_water => chemical_water
    implicit none
    logical, intent(out) :: f90wrap_chemical_water
    
    f90wrap_chemical_water = gen_chemical_water
end subroutine f90wrap_gen__get__chemical_water

subroutine f90wrap_gen__set__chemical_water(f90wrap_chemical_water)
    use gen, only: gen_chemical_water => chemical_water
    implicit none
    logical, intent(in) :: f90wrap_chemical_water
    
    gen_chemical_water = f90wrap_chemical_water
end subroutine f90wrap_gen__set__chemical_water

subroutine f90wrap_gen__array__qwater(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use gen, only: gen_qwater => qwater
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(gen_qwater)) then
        dshape(1:1) = shape(gen_qwater)
        dloc = loc(gen_qwater)
    else
        dloc = 0
    end if
end subroutine f90wrap_gen__array__qwater

subroutine f90wrap_gen__get__rsrt_cnt(f90wrap_rsrt_cnt)
    use gen, only: gen_rsrt_cnt => rsrt_cnt
    implicit none
    integer(4), intent(out) :: f90wrap_rsrt_cnt
    
    f90wrap_rsrt_cnt = gen_rsrt_cnt
end subroutine f90wrap_gen__get__rsrt_cnt

subroutine f90wrap_gen__set__rsrt_cnt(f90wrap_rsrt_cnt)
    use gen, only: gen_rsrt_cnt => rsrt_cnt
    implicit none
    integer(4), intent(in) :: f90wrap_rsrt_cnt
    
    gen_rsrt_cnt = f90wrap_rsrt_cnt
end subroutine f90wrap_gen__set__rsrt_cnt

subroutine f90wrap_gen__get__irsrt(f90wrap_irsrt)
    use gen, only: gen_irsrt => irsrt
    implicit none
    integer(4), intent(out) :: f90wrap_irsrt
    
    f90wrap_irsrt = gen_irsrt
end subroutine f90wrap_gen__get__irsrt

subroutine f90wrap_gen__set__irsrt(f90wrap_irsrt)
    use gen, only: gen_irsrt => irsrt
    implicit none
    integer(4), intent(in) :: f90wrap_irsrt
    
    gen_irsrt = f90wrap_irsrt
end subroutine f90wrap_gen__set__irsrt

subroutine f90wrap_gen__get__backup_frequency(f90wrap_backup_frequency)
    use gen, only: gen_backup_frequency => backup_frequency
    implicit none
    integer(4), intent(out) :: f90wrap_backup_frequency
    
    f90wrap_backup_frequency = gen_backup_frequency
end subroutine f90wrap_gen__get__backup_frequency

subroutine f90wrap_gen__set__backup_frequency(f90wrap_backup_frequency)
    use gen, only: gen_backup_frequency => backup_frequency
    implicit none
    integer(4), intent(in) :: f90wrap_backup_frequency
    
    gen_backup_frequency = f90wrap_backup_frequency
end subroutine f90wrap_gen__set__backup_frequency

subroutine f90wrap_gen__get__restart_sim(f90wrap_restart_sim)
    use gen, only: gen_restart_sim => restart_sim
    implicit none
    logical, intent(out) :: f90wrap_restart_sim
    
    f90wrap_restart_sim = gen_restart_sim
end subroutine f90wrap_gen__get__restart_sim

subroutine f90wrap_gen__set__restart_sim(f90wrap_restart_sim)
    use gen, only: gen_restart_sim => restart_sim
    implicit none
    logical, intent(in) :: f90wrap_restart_sim
    
    gen_restart_sim = f90wrap_restart_sim
end subroutine f90wrap_gen__set__restart_sim

subroutine f90wrap_gen__get__ovr_sat(f90wrap_ovr_sat)
    use gen, only: gen_ovr_sat => ovr_sat
    implicit none
    logical, intent(out) :: f90wrap_ovr_sat
    
    f90wrap_ovr_sat = gen_ovr_sat
end subroutine f90wrap_gen__get__ovr_sat

subroutine f90wrap_gen__set__ovr_sat(f90wrap_ovr_sat)
    use gen, only: gen_ovr_sat => ovr_sat
    implicit none
    logical, intent(in) :: f90wrap_ovr_sat
    
    gen_ovr_sat = f90wrap_ovr_sat
end subroutine f90wrap_gen__set__ovr_sat

! End of module gen defined in file ../src/gen.f

