#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-DBItest
Version  : 1.5.2
Release  : 18
URL      : https://cran.r-project.org/src/contrib/DBItest_1.5-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DBItest_1.5-2.tar.gz
Summary  : Testing 'DBI' Back Ends
Group    : Development/Tools
License  : LGPL-2.0+
Requires: R-DBI
Requires: R-assertthat
Requires: R-blob
Requires: R-desc
Requires: R-hms
Requires: R-rprojroot
Requires: R-withr
BuildRequires : R-DBI
BuildRequires : R-assertthat
BuildRequires : R-blob
BuildRequires : R-desc
BuildRequires : R-hms
BuildRequires : R-rprojroot
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# DBItest [![Travis-CI Build Status](https://travis-ci.org/rstats-db/DBItest.svg?branch=master)](https://travis-ci.org/rstats-db/DBItest) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/rstats-db/DBItest?branch=master&svg=true)](https://ci.appveyor.com/project/rstats-db/DBItest) [![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/DBItest)](https://cran.r-project.org/package=DBItest)

%prep
%setup -q -c -n DBItest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552840240

%install
export SOURCE_DATE_EPOCH=1552840240
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  DBItest || :


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
/usr/lib64/R/library/DBItest/doc/index.html
/usr/lib64/R/library/DBItest/doc/test.Rmd
/usr/lib64/R/library/DBItest/doc/test.html
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
