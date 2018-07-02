#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fitbitScraper
Version  : 0.1.8
Release  : 1
URL      : https://cran.r-project.org/src/contrib/fitbitScraper_0.1.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fitbitScraper_0.1.8.tar.gz
Summary  : Scrapes Data from Fitbit
Group    : Development/Tools
License  : MIT
Requires: R-httr
Requires: R-jsonlite
Requires: R-stringi
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
API, but instead uses the API that the web dashboard uses to generate the graphs

%prep
%setup -q -c -n fitbitScraper

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530512227

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530512227
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitbitScraper
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitbitScraper
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fitbitScraper
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fitbitScraper|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fitbitScraper/DESCRIPTION
/usr/lib64/R/library/fitbitScraper/INDEX
/usr/lib64/R/library/fitbitScraper/LICENSE
/usr/lib64/R/library/fitbitScraper/Meta/Rd.rds
/usr/lib64/R/library/fitbitScraper/Meta/features.rds
/usr/lib64/R/library/fitbitScraper/Meta/hsearch.rds
/usr/lib64/R/library/fitbitScraper/Meta/links.rds
/usr/lib64/R/library/fitbitScraper/Meta/nsInfo.rds
/usr/lib64/R/library/fitbitScraper/Meta/package.rds
/usr/lib64/R/library/fitbitScraper/Meta/vignette.rds
/usr/lib64/R/library/fitbitScraper/NAMESPACE
/usr/lib64/R/library/fitbitScraper/NEWS.md
/usr/lib64/R/library/fitbitScraper/R/fitbitScraper
/usr/lib64/R/library/fitbitScraper/R/fitbitScraper.rdb
/usr/lib64/R/library/fitbitScraper/R/fitbitScraper.rdx
/usr/lib64/R/library/fitbitScraper/doc/fitbitScraper-examples.R
/usr/lib64/R/library/fitbitScraper/doc/fitbitScraper-examples.Rmd
/usr/lib64/R/library/fitbitScraper/doc/fitbitScraper-examples.html
/usr/lib64/R/library/fitbitScraper/doc/index.html
/usr/lib64/R/library/fitbitScraper/help/AnIndex
/usr/lib64/R/library/fitbitScraper/help/aliases.rds
/usr/lib64/R/library/fitbitScraper/help/fitbitScraper.rdb
/usr/lib64/R/library/fitbitScraper/help/fitbitScraper.rdx
/usr/lib64/R/library/fitbitScraper/help/paths.rds
/usr/lib64/R/library/fitbitScraper/html/00Index.html
/usr/lib64/R/library/fitbitScraper/html/R.css