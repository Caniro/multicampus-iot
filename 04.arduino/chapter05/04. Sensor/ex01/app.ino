// DTH11 온습도 센서

#include <MiniCom.h>
#include <DHT.h>

MiniCom com;
DHT dht11(12, DHT11);

void check()
{
    float fh = dht11.readHumidity();
    float fc = dht11.readTemperature(); // 섭씨
    float ff = dht11.readTemperature(true); // 화씨

    if (isnan(fh) || isnan(fc) || isnan(ff))
    {
        com.print(1, "Failed");
        return ;
    }
    com.print(1, "T:", fc, " H:", fh);
}

void setup()
{
    com.init();
    com.setInterval(2000, check);
    dht11.begin();
    com.print(0, "[[DHT11]]");
    com.print(1, "Preparing DHT11");
}

void loop()
{
    com.run();
}
