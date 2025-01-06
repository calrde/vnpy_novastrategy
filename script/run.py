from vnpy_evo.event import EventEngine
from vnpy_evo.trader.engine import MainEngine
from vnpy_evo.trader.ui import MainWindow, create_qapp

from vnpy_binance import BinanceLinearGateway
from vnpy_okx import OkxGateway
from vnpy_novastrategy import NovaStrategyApp


def main():
    """主入口函数"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(OkxGateway, "okx")

    main_engine.add_app(NovaStrategyApp)
    setting = {
        "API Key": "209b54f5-bce2-4aea-ac0f-2a261f83ae2f",
        "Secret Key": "7C48F1E2C61B202994A6B7397BAD62FF",
        "Passphrase": "AAA#4323f",
        "Server": "REAL",
        "Kline Stream": False,
        "Proxy Host": "127.0.0.1",
        "Proxy Port": "1074"
    }
    main_engine.get_gateway("okx").connect(setting)
    # main_engine.get_gateway("binance_swap").connect("REAL",kline_stream=False, "127.0.0.1", 1074)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
