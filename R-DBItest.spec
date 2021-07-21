#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DBItest
Version  : 1.7.0
Release  : 41
URL      : https://cran.r-project.org/src/contrib/DBItest_1.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DBItest_1.7.0.tar.gz
Summary  : Testing 'DBI' 'Backends'
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-DBI
Requires: R-R6
Requires: R-RSQLite
Requires: R-blob
Requires: R-callr
Requires: R-desc
Requires: R-hms
Requires: R-lubridate
Requires: R-rlang
Requires: R-testthat
Requires: R-withr
BuildRequires : R-DBI
BuildRequires : R-R6
BuildRequires : R-RSQLite
BuildRequires : R-blob
BuildRequires : R-callr
BuildRequires : R-desc
BuildRequires : R-hms
BuildRequires : R-lubridate
BuildRequires : R-rlang
BuildRequires : R-testthat
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
to the interface.

%prep
%setup -q -c -n DBItest
cd %{_builddir}/DBItest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589759389

%install
export SOURCE_DATE_EPOCH=1589759389
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBItest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBItest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library DBItest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc DBItest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DBItest/DESCRIPTION
/usr/lib64/R/library/DBItest/INDEX
/usr/lib64/R/library/DBItest/Meta/Rd.rds
/usr/lib64/R/library/DBItest/Meta/features.rds
/usr/lib64/R/library/DBItest/Meta/hsearch.rds
/usr/lib64/R/library/DBItest/Meta/links.rds
/usr/lib64/R/library/DBItest/Meta/nsInfo.rds
/usr/lib64/R/library/DBItest/Meta/package.rds
/usr/lib64/R/library/DBItest/Meta/vignette.rds
/usr/lib64/R/library/DBItest/NAMESPACE
/usr/lib64/R/library/DBItest/NEWS.md
/usr/lib64/R/library/DBItest/R/DBItest
/usr/lib64/R/library/DBItest/R/DBItest.rdb
/usr/lib64/R/library/DBItest/R/DBItest.rdx
/usr/lib64/R/library/DBItest/doc/DBItest.R
/usr/lib64/R/library/DBItest/doc/DBItest.Rmd
/usr/lib64/R/library/DBItest/doc/DBItest.html
/usr/lib64/R/library/DBItest/doc/index.html
/usr/lib64/R/library/DBItest/help/AnIndex
/usr/lib64/R/library/DBItest/help/DBItest.rdb
/usr/lib64/R/library/DBItest/help/DBItest.rdx
/usr/lib64/R/library/DBItest/help/aliases.rds
/usr/lib64/R/library/DBItest/help/paths.rds
/usr/lib64/R/library/DBItest/html/00Index.html
/usr/lib64/R/library/DBItest/html/R.css
/usr/lib64/R/library/DBItest/tests/testthat.R
/usr/lib64/R/library/DBItest/tests/testthat/test-consistency.R
/usr/lib64/R/library/DBItest/tests/testthat/test-context.R
/usr/lib64/R/library/DBItest/tests/testthat/test-lint.R
/usr/lib64/R/library/DBItest/tests/testthat/test-tweaks.R
