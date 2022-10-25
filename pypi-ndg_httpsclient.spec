#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ndg_httpsclient
Version  : 0.5.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/b9/f8/8f49278581cb848fb710a362bfc3028262a82044167684fb64ad068dbf92/ndg_httpsclient-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/f8/8f49278581cb848fb710a362bfc3028262a82044167684fb64ad068dbf92/ndg_httpsclient-0.5.1.tar.gz
Summary  : Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ndg_httpsclient-bin = %{version}-%{release}
Requires: pypi-ndg_httpsclient-license = %{version}-%{release}
Requires: pypi-ndg_httpsclient-python = %{version}-%{release}
Requires: pypi-ndg_httpsclient-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyasn1)
BuildRequires : pypi(pyopenssl)

%description
* ``httplib`` (Python 2), ``http.client`` (Python 3) and 
         * ``urllib2`` (Python 2) and ``urllib`` (Python 3)
        
        ... based on PyOpenSSL.  PyOpenSSL provides a more fully featured SSL implementation 
        over the default provided with Python and importantly enables full verification 
        of the SSL peer using ``pyasn1``.
        
        Releases
        ========
        0.5.1
        -----
         * Clean up handling for description file - pull in content from this file into setup()
         * Allows the nightly build to fail
         * Add Trove version classifiers to make it explicit what is supported
         * Add python_requires to help pip
         * Drop support for EOL Python 2.6 and 3.3  
          
        Thanks to @hugovk for contributions
        
        0.5.0
        -----
         * Fix to Subject Alternative Name handling to allow for certificates with
           more than 64 names (max now 1024).  Thanks to Matt Pegler
         * Fix to subjectAltName string to use byte type for correct matching 
         * Updated SSL Context objects to default to TLS 1.2
        
        0.4.4
        -----
         * Updated test certificates
        
        0.4.3
        -----

%package bin
Summary: bin components for the pypi-ndg_httpsclient package.
Group: Binaries
Requires: pypi-ndg_httpsclient-license = %{version}-%{release}

%description bin
bin components for the pypi-ndg_httpsclient package.


%package license
Summary: license components for the pypi-ndg_httpsclient package.
Group: Default

%description license
license components for the pypi-ndg_httpsclient package.


%package python
Summary: python components for the pypi-ndg_httpsclient package.
Group: Default
Requires: pypi-ndg_httpsclient-python3 = %{version}-%{release}

%description python
python components for the pypi-ndg_httpsclient package.


%package python3
Summary: python3 components for the pypi-ndg_httpsclient package.
Group: Default
Requires: python3-core
Provides: pypi(ndg_httpsclient)
Requires: pypi(pyasn1)
Requires: pypi(pyopenssl)

%description python3
python3 components for the pypi-ndg_httpsclient package.


%prep
%setup -q -n ndg_httpsclient-0.5.1
cd %{_builddir}/ndg_httpsclient-0.5.1
pushd ..
cp -a ndg_httpsclient-0.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392024
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
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ndg_httpsclient
cp %{_builddir}/ndg_httpsclient-0.5.1/ndg/httpsclient/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ndg_httpsclient/e0de95c235bf947465c907c614e8a522062efb1c
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
/usr/bin/ndg_httpclient

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ndg_httpsclient/e0de95c235bf947465c907c614e8a522062efb1c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
