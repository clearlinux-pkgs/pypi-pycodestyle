#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pycodestyle
Version  : 2.9.1
Release  : 72
URL      : https://files.pythonhosted.org/packages/b6/83/5bcaedba1f47200f0665ceb07bcb00e2be123192742ee0edfb66b600e5fd/pycodestyle-2.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/83/5bcaedba1f47200f0665ceb07bcb00e2be123192742ee0edfb66b600e5fd/pycodestyle-2.9.1.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pypi-pycodestyle-bin = %{version}-%{release}
Requires: pypi-pycodestyle-license = %{version}-%{release}
Requires: pypi-pycodestyle-python = %{version}-%{release}
Requires: pypi-pycodestyle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pycodestyle (formerly called pep8) - Python style guide checker
===============================================================

%package bin
Summary: bin components for the pypi-pycodestyle package.
Group: Binaries
Requires: pypi-pycodestyle-license = %{version}-%{release}

%description bin
bin components for the pypi-pycodestyle package.


%package license
Summary: license components for the pypi-pycodestyle package.
Group: Default

%description license
license components for the pypi-pycodestyle package.


%package python
Summary: python components for the pypi-pycodestyle package.
Group: Default
Requires: pypi-pycodestyle-python3 = %{version}-%{release}

%description python
python components for the pypi-pycodestyle package.


%package python3
Summary: python3 components for the pypi-pycodestyle package.
Group: Default
Requires: python3-core
Provides: pypi(pycodestyle)

%description python3
python3 components for the pypi-pycodestyle package.


%prep
%setup -q -n pycodestyle-2.9.1
cd %{_builddir}/pycodestyle-2.9.1
pushd ..
cp -a pycodestyle-2.9.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659587465
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover testsuite -vv

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycodestyle
cp %{_builddir}/pycodestyle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pycodestyle/0b3a0b386cf2762bc7b475c9855cdec47dd70a38
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycodestyle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pycodestyle/0b3a0b386cf2762bc7b475c9855cdec47dd70a38

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
