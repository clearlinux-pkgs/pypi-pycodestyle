#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pycodestyle
Version  : 2.11.0
Release  : 81
URL      : https://files.pythonhosted.org/packages/c1/2d/022c78a6b3f591205e52b4d25c93b7329280f752b36ba2fc1377cbf016cd/pycodestyle-2.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c1/2d/022c78a6b3f591205e52b4d25c93b7329280f752b36ba2fc1377cbf016cd/pycodestyle-2.11.0.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pypi-pycodestyle-bin = %{version}-%{release}
Requires: pypi-pycodestyle-license = %{version}-%{release}
Requires: pypi-pycodestyle-python = %{version}-%{release}
Requires: pypi-pycodestyle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n pycodestyle-2.11.0
cd %{_builddir}/pycodestyle-2.11.0
pushd ..
cp -a pycodestyle-2.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695153651
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycodestyle
cp %{_builddir}/pycodestyle-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pycodestyle/0b3a0b386cf2762bc7b475c9855cdec47dd70a38 || :
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
