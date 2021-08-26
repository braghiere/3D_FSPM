! Module dual defined in file ../src/dual.f

subroutine f90wrap_dual__get__idual_type(f90wrap_idual_type)
    use dual, only: dual_idual_type => idual_type
    implicit none
    integer(4), intent(out) :: f90wrap_idual_type
    
    f90wrap_idual_type = dual_idual_type
end subroutine f90wrap_dual__get__idual_type

subroutine f90wrap_dual__set__idual_type(f90wrap_idual_type)
    use dual, only: dual_idual_type => idual_type
    implicit none
    integer(4), intent(in) :: f90wrap_idual_type
    
    dual_idual_type = f90wrap_idual_type
end subroutine f90wrap_dual__set__idual_type

subroutine f90wrap_dual__get__dual_perm(f90wrap_dual_perm)
    use dual, only: dual_dual_perm => dual_perm
    implicit none
    logical, intent(out) :: f90wrap_dual_perm
    
    f90wrap_dual_perm = dual_dual_perm
end subroutine f90wrap_dual__get__dual_perm

subroutine f90wrap_dual__set__dual_perm(f90wrap_dual_perm)
    use dual, only: dual_dual_perm => dual_perm
    implicit none
    logical, intent(in) :: f90wrap_dual_perm
    
    dual_dual_perm = f90wrap_dual_perm
end subroutine f90wrap_dual__set__dual_perm

subroutine f90wrap_dual__get__dual_perm1(f90wrap_dual_perm1)
    use dual, only: dual_dual_perm1 => dual_perm1
    implicit none
    logical, intent(out) :: f90wrap_dual_perm1
    
    f90wrap_dual_perm1 = dual_dual_perm1
end subroutine f90wrap_dual__get__dual_perm1

subroutine f90wrap_dual__set__dual_perm1(f90wrap_dual_perm1)
    use dual, only: dual_dual_perm1 => dual_perm1
    implicit none
    logical, intent(in) :: f90wrap_dual_perm1
    
    dual_dual_perm1 = f90wrap_dual_perm1
end subroutine f90wrap_dual__set__dual_perm1

subroutine f90wrap_dual__get__dual_perm2(f90wrap_dual_perm2)
    use dual, only: dual_dual_perm2 => dual_perm2
    implicit none
    logical, intent(out) :: f90wrap_dual_perm2
    
    f90wrap_dual_perm2 = dual_dual_perm2
end subroutine f90wrap_dual__get__dual_perm2

subroutine f90wrap_dual__set__dual_perm2(f90wrap_dual_perm2)
    use dual, only: dual_dual_perm2 => dual_perm2
    implicit none
    logical, intent(in) :: f90wrap_dual_perm2
    
    dual_dual_perm2 = f90wrap_dual_perm2
end subroutine f90wrap_dual__set__dual_perm2

subroutine f90wrap_dual__get__cpuint(f90wrap_cpuint)
    use dual, only: dual_cpuint => cpuint
    implicit none
    real(8), intent(out) :: f90wrap_cpuint
    
    f90wrap_cpuint = dual_cpuint
end subroutine f90wrap_dual__get__cpuint

subroutine f90wrap_dual__set__cpuint(f90wrap_cpuint)
    use dual, only: dual_cpuint => cpuint
    implicit none
    real(8), intent(in) :: f90wrap_cpuint
    
    dual_cpuint = f90wrap_cpuint
end subroutine f90wrap_dual__set__cpuint

subroutine f90wrap_dual__get__csec(f90wrap_csec)
    use dual, only: dual_csec => csec
    implicit none
    real(8), intent(out) :: f90wrap_csec
    
    f90wrap_csec = dual_csec
end subroutine f90wrap_dual__get__csec

subroutine f90wrap_dual__set__csec(f90wrap_csec)
    use dual, only: dual_csec => csec
    implicit none
    real(8), intent(in) :: f90wrap_csec
    
    dual_csec = f90wrap_csec
end subroutine f90wrap_dual__set__csec

subroutine f90wrap_dual__array__rkinter (dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_rkinter  => rkinter
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(dual_rkinter )) then
        dshape(1:1) = shape(dual_rkinter )
        dloc = loc(dual_rkinter )
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__rkinter

subroutine f90wrap_dual__array__dualhcrit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_dualhcrit => dualhcrit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(dual_dualhcrit)) then
        dshape(1:1) = shape(dual_dualhcrit)
        dloc = loc(dual_dualhcrit)
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__dualhcrit

subroutine f90wrap_dual__array__satwcrit(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_satwcrit => satwcrit
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(dual_satwcrit)) then
        dshape(1:1) = shape(dual_satwcrit)
        dloc = loc(dual_satwcrit)
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__satwcrit

subroutine f90wrap_dual__array__dualmag(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_dualmag => dualmag
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(dual_dualmag)) then
        dshape(1:1) = shape(dual_dualmag)
        dloc = loc(dual_dualmag)
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__dualmag

subroutine f90wrap_dual__array__wf (dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_wf  => wf
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 12
    if (allocated(dual_wf )) then
        dshape(1:1) = shape(dual_wf )
        dloc = loc(dual_wf )
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__wf

subroutine f90wrap_dual__array__mat(dummy_this, nd, dtype, dshape, dloc)
    use parm
    use dual, only: dual_mat => mat
    implicit none
    integer, intent(in) :: dummy_this(2)
    integer, intent(out) :: nd
    integer, intent(out) :: dtype
    integer, dimension(10), intent(out) :: dshape
    integer*8, intent(out) :: dloc
    
    nd = 1
    dtype = 5
    if (allocated(dual_mat)) then
        dshape(1:1) = shape(dual_mat)
        dloc = loc(dual_mat)
    else
        dloc = 0
    end if
end subroutine f90wrap_dual__array__mat

! End of module dual defined in file ../src/dual.f

