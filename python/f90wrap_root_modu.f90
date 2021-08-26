! Module root_modu defined in file ../src/root_modu.f

subroutine f90wrap_root_modu__array__rsd_archi(dummy_this, nd, dtype, dshape, &
    dloc)
    use gen
    use root_modu, only: root_modu_rsd_archi => rsd_archi
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(root_modu_rsd_archi)) then
        dshape(1:1) = shape(root_modu_rsd_archi)
        dloc = loc(root_modu_rsd_archi)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__rsd_archi

subroutine f90wrap_root_modu__array__rsd_bonsens(dummy_this, nd, dtype, dshape, &
    dloc)
    use gen
    use root_modu, only: root_modu_rsd_bonsens => rsd_bonsens
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(root_modu_rsd_bonsens)) then
        dshape(1:1) = shape(root_modu_rsd_bonsens)
        dloc = loc(root_modu_rsd_bonsens)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__rsd_bonsens

subroutine f90wrap_root_modu__array__x_g(dummy_this, nd, dtype, dshape, dloc)
    use gen
    use root_modu, only: root_modu_x_g => x_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(root_modu_x_g)) then
        dshape(1:1) = shape(root_modu_x_g)
        dloc = loc(root_modu_x_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__x_g

subroutine f90wrap_root_modu__array__y_g(dummy_this, nd, dtype, dshape, dloc)
    use gen
    use root_modu, only: root_modu_y_g => y_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(root_modu_y_g)) then
        dshape(1:1) = shape(root_modu_y_g)
        dloc = loc(root_modu_y_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__y_g

subroutine f90wrap_root_modu__array__z_g(dummy_this, nd, dtype, dshape, dloc)
    use gen
    use root_modu, only: root_modu_z_g => z_g
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(root_modu_z_g)) then
        dshape(1:1) = shape(root_modu_z_g)
        dloc = loc(root_modu_z_g)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__z_g

subroutine f90wrap_root_modu__array__humidity(dummy_this, nd, dtype, dshape, &
    dloc)
    use gen
    use root_modu, only: root_modu_humidity => humidity
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 11
    if (allocated(root_modu_humidity)) then
        dshape(1:1) = shape(root_modu_humidity)
        dloc = loc(root_modu_humidity)
    else
        dloc = 0
    end if
end subroutine f90wrap_root_modu__array__humidity

! End of module root_modu defined in file ../src/root_modu.f

