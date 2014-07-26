 #!/bin/sh

rm -rf dist
mkdir dist

export version=`date +%Y%m%d%H%M%S`

rm -rf moonbow-backend/opt/moonbow-backend
mkdir -p moonbow-backend/opt/moonbow-backend
cp ../src/main/* moonbow-backend/opt/moonbow-backend
sed "s/%DATE%/$version/g" moonbow-backend/CONTROL/control.template > moonbow-backend/CONTROL/control

pushd dist
../ipkg-build ../moonbow-backend .
popd 


