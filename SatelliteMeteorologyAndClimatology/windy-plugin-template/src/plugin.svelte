<div class="plugin__mobile-header">
    {title}
</div>
<section class="plugin__content">
    <div
        class="plugin__title plugin__title--chevron-back"
        on:click={() => bcast.emit('rqstOpen', 'menu')}
    >
        {title}
    </div>

    <p class="intro">Pick a location on the map and send it to GeoAI for analysis.</p>

    <div class="card">
        {#if selected}
            <div class="coord-row">
                <span class="coord-row__label">Latitude</span>
                <span class="coord-row__value">{formatCoord(selected.lat, 'N', 'S')}</span>
            </div>
            <div class="coord-row">
                <span class="coord-row__label">Longitude</span>
                <span class="coord-row__value">{formatCoord(selected.lon, 'E', 'W')}</span>
            </div>

            <button class="button button--primary" disabled={sending} on:click={submit}>
                {sending ? 'Sending…' : 'Submit point'}
            </button>
        {:else}
            <div class="empty">
                <div class="empty__icon">📍</div>
                <div class="empty__text">
                    Click anywhere on the map<br />to select a point.
                </div>
            </div>
        {/if}

        {#if message}
            <p class="status" class:status--error={isError}>
                {isError ? '✕' : '✓'}
                {message}
            </p>
        {/if}
    </div>

    <div class="footer">
        <div class="footer__divider"></div>
        <a
            class="button button--secondary"
            href={GEOAI_APP_URL}
            target="_blank"
            rel="noopener noreferrer"
        >
            Open GeoAI application&nbsp;↗
        </a>
        <p class="footer__hint">
            You can also add a point manually there by entering its coordinates.
        </p>
    </div>
</section>

<script lang="ts">
    import bcast from '@windy/broadcast';
    import { singleclick } from '@windy/singleclick';
    import { onDestroy, onMount } from 'svelte';

    import { GEOAI_APP_URL } from './config/consts';
    import { removePin, showPin } from './map/marker';
    import config from './pluginConfig';
    import { submitPoint } from './services/geoApi';
    import { formatCoord } from './utils/format';

    import type { LatLon } from '@windy/interfaces';

    const { name, title } = config;

    let selected: LatLon | null = null;
    let sending = false;
    let message = '';
    let isError = false;

    const setLocation = ({ lat, lon }: LatLon) => {
        selected = { lat, lon };
        message = '';
        showPin(selected);
    };

    const submit = async () => {
        if (!selected || sending) {
            return;
        }

        sending = true;
        message = '';

        try {
            await submitPoint(selected);
            message = 'Point submitted successfully.';
            isError = false;

        } catch (error) {
            message = `Request failed: ${error instanceof Error ? error.message : String(error)}`;
            isError = true;

        } finally {
            sending = false;
        }
    };

    export const onopen = (params?: LatLon) => {
        // Plugin was opened from the contextmenu (RH mouse click on map)
        // with a LatLon object, or from URL with lat/lon parameters
        if (params && typeof params.lat === 'number' && typeof params.lon === 'number') {
            setLocation(params);
        }
    };

    onMount(() => {
        singleclick.on(name, setLocation);
    });

    onDestroy(() => {
        singleclick.off(name, setLocation);
        removePin();
    });
</script>

<style lang="less">
    .intro {
        margin: 0 0 15px;
        color: rgba(255, 255, 255, 0.6);
        font-size: 12px;
        line-height: 1.5;
    }

    .card {
        padding: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.05);
    }

    .coord-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        padding: 6px 0;

        & + & {
            border-top: 1px solid rgba(255, 255, 255, 0.07);
        }

        &__label {
            color: rgba(255, 255, 255, 0.55);
            font-size: 11px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        &__value {
            font-family: 'Consolas', 'Menlo', monospace;
            font-size: 15px;
            font-weight: 600;
            color: #fff;
        }
    }

    .empty {
        padding: 18px 0;
        text-align: center;

        &__icon {
            margin-bottom: 8px;
            font-size: 26px;
        }

        &__text {
            color: rgba(255, 255, 255, 0.6);
            font-size: 12px;
            line-height: 1.5;
        }
    }

    .button {
        display: block;
        box-sizing: border-box;
        width: 100%;
        padding: 9px 16px;
        border: 0;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 600;
        text-align: center;
        text-decoration: none;
        cursor: pointer;
        transition:
            background-color 0.15s ease,
            opacity 0.15s ease;

        &--primary {
            margin-top: 14px;
            background-color: #4a7fd6;
            color: #fff;

            &:hover:not(:disabled) {
                background-color: #5b8fe4;
            }

            &:disabled {
                opacity: 0.55;
                cursor: default;
            }
        }

        &--secondary {
            background-color: transparent;
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: rgba(255, 255, 255, 0.85);

            &:hover {
                background-color: rgba(255, 255, 255, 0.08);
                color: #fff;
            }
        }
    }

    .status {
        margin: 12px 0 0;
        font-size: 12px;
        line-height: 1.4;
        color: #7ed29a;

        &--error {
            color: #ff8a8a;
        }
    }

    .footer {
        margin-top: 20px;

        &__divider {
            margin-bottom: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        &__hint {
            margin: 8px 0 0;
            color: rgba(255, 255, 255, 0.45);
            font-size: 11px;
            line-height: 1.5;
        }
    }
</style>
